"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class CompilationEngine:
    """Gets token from a JackTokenizer and emits its parsed structure into an
    output stream.
    """
    def __init__(self, token_stream, writer, table) -> None:
        """
        Creates a new compilation engine with the given token and output. The
        next routine called must be compileClass()
        :param token_stream: The token stream.
        :param output_stream: The output stream.
        """
        self.token_stream = token_stream 
        self.writer = writer
        self.table = table
        self.label_counter = 0
        self.class_name = ''

    def generate_label(self) -> str:
        res = self.class_name + 'Label' + str(self.label_counter)
        self.label_counter += 1
        return res

    def write_identifier(self,identifier) -> None:
        self.write(f"<identifier> {identifier} </identifier>")
        self.token_stream.advance()

    def handle_varName(self) -> None:
        """
        handles the writing of a predeclared variable.
        """
        var_name = self.token_stream.identifier()
        var_kind = self.table.kind_of(var_name)
        var_index = self.table.index_of(var_name)
        self.writer.write_push(var_kind,var_index)

    def handle_type(self) -> None:
        var_type = self.token_stream.token_type()
        if var_type == "KEYWORD":
            var_kind = self.token_stream.keyword().lower()
            self.process(var_kind)
        else:
            var_kind = self.token_stream.identifier()
            self.write_identifier(var_kind)

    def compile_class(self) -> None:
        """Compiles a complete class."""

        self.process("class")

        class_name = self.token_stream.identifier() 
        self.class_name = class_name
        self.write_identifier(class_name)

        self.process("{")

        while self.token_stream.token_type() == "KEYWORD":
            token_value = self.token_stream.keyword().lower()
            if token_value in {"field","static"}:
                self.compile_class_var_dec()
            elif token_value in {"method", "constructor","function"}:
                self.compile_subroutine()
            else:
                print("syntax error - class function that isnt varDec or subroutine.")
                print('got: ' + token_value)
        self.process("}")     

    def process(self, token: str) -> None:
        type = self.token_stream.token_type()
        if type == "KEYWORD":
            current = self.token_stream.keyword().lower()
        elif type == "SYMBOL":
            current = self.token_stream.symbol()
        if current != token: print('expected ' + token + ' got '+ current)
        if self.token_stream.has_more_tokens(): self.token_stream.advance()

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        
        # handles (static|field) section
        var_kind = self.token_stream.keyword().lower()
        var_type = self.token_stream.keyword().lower()
        var_name = self.token_stream.identifier()

        self.table.define(var_name,var_type,var_kind.upper())

        # handles possible other varNames
        symbol_value = self.token_stream.symbol()
        while symbol_value != ";":
            self.process(",")
            self.table.define(var_name,var_type,var_kind.upper())
            self.token_stream.advance()
            symbol_value = self.token_stream.symbol()
        self.process(";")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        self.token_stream.advance()

        self.token_stream.advance()

        subroutine_name = self.token_stream.identifier()
        self.token_stream.advance()

        subroutine_name = self.token_stream.identifier()
        self.write_identifier(subroutine_name)

        self.process("(")
        self.compile_parameter_list()
        self.process(")")

        self.process("{")
        n_vars = 0
        while self.token_stream.token_type() == 'KEYWORD' and self.token_stream.keyword()=='VAR':
            self.compile_var_dec()
            n_vars += 1
        self.writer.write_function(subroutine_name, n_vars)
        self.compile_statements()
        self.process("}")

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the 
        enclosing "()".
        """
        while self.token_stream.token_type()!='SYMBOL' or self.token_stream.symbol()!=')':
            if self.token_stream.token_type() == 'SYMBOL': self.process(',')
            var_type = self.token_stream.symbol()
            self.token_stream.advance()
            var_name = self.token_stream.identifier()
            self.token_stream.advance()
            self.table.define(var_name,var_type,"ARG")

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        self.process("var")
        self.handle_type()
        self.handle_varName()
        symbol = self.token_stream.symbol()
        while symbol == ",":
            self.process(symbol)
            self.handle_varName()
            symbol = self.token_stream.symbol()
        self.process(";")            
        self.tab_number -= 1
        self.write("</varDec>")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing 
        "{}".
        """
        # Your code goes here!
        self.write("<statements>")
        self.tab_number += 1

        token_type = self.token_stream.token_type()
        while token_type == "KEYWORD":
            statement_kind = self.token_stream.keyword().lower()
            if statement_kind == "if":
                self.compile_if()
            elif statement_kind == "while":
                self.compile_while()
            elif statement_kind == "let":
                self.compile_let()
            elif statement_kind == "do":
                self.compile_do()
            elif statement_kind == "return":
                self.compile_return()
            token_type = self.token_stream.token_type()
        
        self.tab_number -= 1
        self.write("</statements>")

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # Your code goes here!
        self.process('do')
        self.compile_term()
        self.writer.write_pop('temp', 0)
        self.process(';')

    def compile_let(self) -> None:
        """Compiles a let statement."""
        # Your code goes here!
        self.process('let')
        array = False
        identifier = self.token_stream.identifier()
        segment, index = self.table.kind_of(identifier), self.table.index_of(identifier)
        self.token_stream.advance()
        s = self.input_stream.symbol()
        if s=='[':
            array = True
            self.process('[')
            self.writer.write_push(segment, index)
            self.compile_expression()
            self.writer.write_arithmetic('add')
            self.process(']')
        self.process('=')
        self.compile_expression()
        if not array:
            self.writer.write_pop(segment, index)
        else:
            self.writer.write_pop('temp', 0)
            self.writer.write_pop('pointer', 1)
            self.writer.write_push('temp', 0)
            self.writer.write_pop('that', 0)
        self.process(';')

    def compile_while(self) -> None:
        """Compiles a while statement."""
        # Your code goes here!
        start_while = self.generate_label()
        end_while = self.generate_label()
        self.process('while')
        self.process('(')
        self.writer.write_label(start_while)
        self.compile_expression()
        self.writer.write_arithmetic('not')
        self.writer.write_if(end_while)
        self.process(')')
        self.process('{')
        self.compile_statements()
        self.writer.write_goto(start_while)
        self.writer.write_label(end_while)
        self.process('}')

    def compile_return(self) -> None:
        """Compiles a return statement."""
        # Your code goes here!
        self.process('return')
        type = self.input_stream.token_type()
        if type == "SYMBOL" and self.input_stream.symbol() == ';':
            self.writer.write_push('constant', 0)
        else:
            self.compile_expression()
        self.writer.write_return()
        self.process(';')

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!
        start_else = self.generate_label()
        end_else = self.generate_label()
        self.process('if')
        self.process('(')
        self.compile_expression()
        self.writer.write_arithmetic('not')
        self.writer.write_if(start_else)
        self.process(')')
        self.process('{')
        self.compile_statements()
        self.writer.write_goto(end_else)
        self.process('}')
        self.writer.write_label(start_else)
        if self.input_stream.token_type()=='KEYWORD':
            if self.input_stream.keyword()=='ELSE':
                self.process('else')
                self.process('{')
                self.compile_statements()
                self.process('}')
        self.writer.write_label(end_else)

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        ops = {'+': 'add', '-': 'sub', '*': '*', '/': '/',
               '&': 'and', '|': 'or', '<': 'lt', '>': 'gt', '=': 'eq'}
        self.compile_term()
        while self.token_stream.token_type()=='SYMBOL' and (self.token_stream.symbol() in ops.keys()):
            op = ops[self.token_stream.symbol()]
            self.token_stream.advance()
            self.compile_term()
            if op == '*': self.writer.write_call('Math.multiply', 2)
            if op == '/': self.writer.write_call('Math.divide', 2)
            self.writer.write_arithmetic(op)

    def compile_string(self) -> None:
        s = self.token_stream.string_val()
        self.writer.write_push('constant', len(s))
        self.writer.write_call('String.new', 1)
        for c in s:
            self.writer.write_push('constant', ord(c))
            self.writer.write_call('String.appendChar', 2)
        self.token_stream.advance()

    def compile_term(self) -> None:
        """Compiles a term. 
        This routine is faced with a slight difficulty when
        trying to decide between some of the alternative parsing rules.
        Specifically, if the current token is an identifier, the routing must
        distinguish between a variable, an array entry, and a subroutine call.
        A single look-ahead token, which may be one of "[", "(", or "." suffices
        to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        # Your code goes here!
        keyword_constants = {'true', 'false', 'this', 'null'}
        unary_ops = {'-': 'neg', '~': 'not', '^': 'shiftright', '#': 'shiftleft'}
        type = self.token_stream.token_type()
        if type == "INT_CONST":
            self.writer.write_push('constant', self.token_stream.int_val())
            self.token_stream.advance()
        if type == "STRING_CONST":
            self.compile_string()
        if type == "KEYWORD" and (self.token_stream.keyword().lower() in keyword_constants):
            keyword_constant = self.token_stream.keyword()
            if keyword_constant == 'TRUE':
                self.writer.write_push('constant', 1)
                self.writer.write_arithmetic('neg')
            elif keyword_constant in {'FALSE', 'NULL'}:
                self.writer.write_push('constant', 0)
            else:
                self.writer.write_push('pointer', 0)
            self.token_stream.advance()
        if type == "SYMBOL":
            if self.token_stream.symbol() in unary_ops.keys():
                op = self.token_stream.symbol()
                self.token_stream.advance()
                self.compile_term()
                self.writer.write_arithmetic(unary_ops[op])
            else:
                self.process('(')
                self.compile_expression()
                self.process(')')
        if type == "IDENTIFIER":
            identifier = self.token_stream.identifier()
            segment, index = self.table.kind_of(identifier), self.table.index_of(identifier)
            object_type = self.table.type_of(identifier)
            self.token_stream.advance()
            if self.token_stream.token_type() == "SYMBOL":
                symbol = self.token_stream.symbol()
                if symbol == '.':
                    self.process('.')
                    self.writer.write_push(segment, index)
                    method_name = self.token_stream.identifier()
                    self.token_stream.advance()
                    self.process('(')
                    n = self.compile_expression_list()
                    self.process(')')
                    self.writer.write_call(object_type + '.' + method_name, n+1)
                    return
                if symbol == '[':
                    self.process('[')
                    self.writer.write_push(segment, index)
                    self.compile_expression()
                    self.writer.write_arithmetic('add')
                    self.writer.write_pop('pointer', 1)
                    self.writer.write_push('that', 0)
                    self.process(']')
                    return
                if symbol == '(':
                    self.writer.write_push('pointer', 0)
                    self.process('(')
                    n = self.compile_expression_list()
                    self.process(')')
                    self.writer.write_call(self.class_name + '.' + identifier, n+1)
                    return
            self.writer.write_push(segment, index)
            
    def compile_expression_list(self) -> int:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # Your code goes here!
        res = 0
        while True:
            if self.token_stream.token_type() == 'SYMBOL' and self.token_stream.symbol()==')':
                break
            if self.token_stream.token_type() == 'SYMBOL' and self.token_stream.symbol()==',':
                self.process(',')
            else:
                self.compile_expression()
                res += 1
        return res