"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def __init__(self, input_stream, output_stream) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        self.input_stream = input_stream 
        self.output_stream = output_stream
                
        self.tab_number = 0 # used to count the number of tabs

    def write(self, string: str) -> None:
        self.output_stream.write(("  " * self.tab_number) + string + "\n")
        print(("  " * self.tab_number) + string)

    def write_identifier(self,identifier) -> None:
        self.write(f"<identifier> {identifier} </identifier>")
        self.input_stream.advance()

    def handle_varName(self) -> None:
        var_name = self.input_stream.identifier()
        self.write_identifier(var_name)

    def handle_type(self) -> None:
        var_type = self.input_stream.token_type()
        if var_type == "KEYWORD":
            var_kind = self.input_stream.keyword().lower()
            self.process(var_kind)
        else:
            var_kind = self.input_stream.identifier()
            self.write_identifier(var_kind)

    def compile_class(self) -> None:
        """Compiles a complete class."""

        self.write("<class>")
        self.tab_number += 1
        
        self.process("class")

        class_name = self.input_stream.identifier() 
        self.write_identifier(class_name)

        self.process("{")

        while self.input_stream.token_type() == "KEYWORD":
            token_value = self.input_stream.keyword().lower()
            if token_value in {"field","static"}:
                self.compile_class_var_dec()
            elif token_value in {"method", "constructor","function"}:
                self.compile_subroutine()
            else:
                print("syntax error - class function that isnt varDec or subroutine.")
                print('got: ' + token_value)
        self.process("}")

        self.tab_number -= 1
        self.write("</class>")     


    def process(self, token: str) -> None:
        type = self.input_stream.token_type()
        if type == "KEYWORD":
            current = self.input_stream.keyword().lower()
            self.write('<keyword> ' + current + ' </keyword>')
        elif type == "SYMBOL":
            current = self.input_stream.symbol()
            self.write('<symbol> ' + current + ' </symbol>')
        if current != token: print('expected ' + token + ' got '+ current)
        if self.input_stream.has_more_tokens(): self.input_stream.advance()

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        self.write("<classVarDec>")
        self.tab_number += 1

        # handles (static|field) section
        dec_type = self.input_stream.keyword().lower()
        self.process(dec_type)

        self.handle_type()

        # handles the first varName
        self.handle_varName()

        # handles possible other varNames
        symbol_value = self.input_stream.symbol()
        while symbol_value != ";":
            self.process(",")
            self.handle_varName()
            symbol_value = self.input_stream.symbol()
        
        self.process(";")

        self.tab_number -= 1
        self.write("</classVarDec>")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        self.write("<subroutineDec>")
        self.tab_number += 1
        
        subroutine_type = self.input_stream.keyword().lower()
        self.process(subroutine_type)
        
        token_type = self.input_stream.token_type()
        if token_type == "KEYWORD":
            subroutine_output_kind = self.input_stream.keyword().lower()
            self.process(subroutine_output_kind)
        else:
            subroutine_output_kind = self.input_stream.identifier()
            self.write_identifier(subroutine_output_kind)

        subroutine_name = self.input_stream.identifier()
        self.write_identifier(subroutine_name)

        self.process("(")
        self.compile_parameter_list()
        self.process(")")

        self.write('<subroutineBody>')
        self.tab_number += 1
        self.process("{")
        while self.input_stream.token_type() == 'KEYWORD' and self.input_stream.keyword()=='VAR':
            self.compile_var_dec()
        self.compile_statements()
        self.process("}")
        self.tab_number -= 1
        self.write('</subroutineBody>')

        self.tab_number -= 1
        self.write("</subroutineDec>")

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the 
        enclosing "()".
        """
        self.write("<parameterList>")
        self.tab_number += 1
        while self.input_stream.token_type()!='SYMBOL' or self.input_stream.symbol()!=')':
            if self.input_stream.token_type() == 'SYMBOL': self.process(',')
            self.handle_type()
            self.handle_varName()
        self.tab_number -= 1
        self.write("</parameterList>")

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        self.write("<varDec>")
        self.tab_number += 1
        self.process("var")
        self.handle_type()
        self.handle_varName()
        symbol = self.input_stream.symbol()
        while symbol == ",":
            self.process(symbol)
            self.handle_varName()
            symbol = self.input_stream.symbol()
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

        token_type = self.input_stream.token_type()
        while token_type == "KEYWORD":
            statement_kind = self.input_stream.keyword().lower()
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
            token_type = self.input_stream.token_type()
        
        self.tab_number -= 1
        self.write("</statements>")

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # Your code goes here!
        self.write('<doStatement>')
        self.tab_number += 1
        self.process('do')
        self.handle_varName()
        s = self.input_stream.symbol()
        while s == '.':
            self.process('.')
            self.handle_varName()
            s = self.input_stream.symbol()
        self.process('(')
        self.compile_expression_list()
        self.process(')')
        self.process(';')
        self.tab_number -= 1
        self.write('</doStatement>')

    def compile_let(self) -> None:
        """Compiles a let statement."""
        # Your code goes here!
        self.write('<letStatement>')
        self.tab_number += 1
        self.process('let')
        self.handle_varName()
        s = self.input_stream.symbol()
        if s=='[':
            self.process('[')
            self.compile_expression()
            self.process(']')
        self.process('=')
        self.compile_expression()
        self.process(';')
        self.tab_number -= 1
        self.write('</letStatement>')

    def compile_while(self) -> None:
        """Compiles a while statement."""
        # Your code goes here!
        self.write('<whileStatement>')
        self.tab_number += 1
        self.process('while')
        self.process('(')
        self.compile_expression()
        self.process(')')
        self.process('{')
        self.compile_statements()
        self.process('}')
        self.tab_number -= 1
        self.write('</whileStatement>')

    def compile_return(self) -> None:
        """Compiles a return statement."""
        # Your code goes here!
        self.write('<returnStatement>')
        self.tab_number += 1
        self.process('return')
        type = self.input_stream.token_type()
        if not (type == "SYMBOL" and self.input_stream.symbol() == ';'):
            self.compile_expression()
        self.process(';')
        self.tab_number -= 1
        self.write('</returnStatement>')

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!
        self.write('<ifStatement>')
        self.tab_number += 1
        self.process('if')
        self.process('(')
        self.compile_expression()
        self.process(')')
        self.process('{')
        self.compile_statements()
        self.process('}')
        if self.input_stream.token_type()=='KEYWORD':
            if self.input_stream.keyword()=='ELSE':
                self.process('else')
                self.process('{')
                self.compile_statements()
                self.process('}')
        self.tab_number -= 1
        self.write('</ifStatement>')

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        ops = {'+', '-', '*', '/', '&', '|', '<', '>', '='}
        self.write('<expression>')
        self.tab_number += 1
        self.compile_term()
        while self.input_stream.token_type()=='SYMBOL' and (self.input_stream.symbol() in ops):
            op = self.input_stream.symbol()
            if op == '<': op = '&lt;'
            if op == '>': op = '&gt;'
            if op == '&': op = '&amp;'
            self.write('<symbol> ' + op + ' </symbol>')
            self.input_stream.advance()
            self.compile_term()
        self.tab_number -= 1
        self.write('</expression>')

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
        unary_ops = {'-', '~', '^', '#'}
        self.write('<term>')
        self.tab_number += 1
        type = self.input_stream.token_type()
        if type == "INT_CONST":
            self.write('<integerConstant> ' + str(self.input_stream.int_val()) + ' </integerConstant>')
            self.input_stream.advance()
        if type == "STRING_CONST":
            self.write('<stringConstant> ' + self.input_stream.string_val() + ' </stringConstant>')
            self.input_stream.advance()
        if type == "KEYWORD" and (self.input_stream.keyword().lower() in keyword_constants):
            self.write('<keyword> ' + self.input_stream.keyword().lower() + ' </keyword>')
            self.input_stream.advance()
        if type == "SYMBOL":
            if self.input_stream.symbol() in unary_ops:
                self.write('<symbol> ' + self.input_stream.symbol() + ' </symbol>')
                self.input_stream.advance()
                self.compile_term()
            else:
                self.process('(')
                self.compile_expression()
                self.process(')')
        if type == "IDENTIFIER":
            self.write('<identifier> ' + self.input_stream.identifier() + ' </identifier>')
            self.input_stream.advance()
            if self.input_stream.token_type() == "SYMBOL":
                symbol = self.input_stream.symbol()
                if symbol == '.':
                    self.process('.')
                    self.write('<identifier> ' + self.input_stream.identifier() + ' </identifier>')
                    self.input_stream.advance()
                    self.process('(')
                    self.compile_expression_list()
                    self.process(')')
                if symbol == '[':
                    self.process('[')
                    self.compile_expression()
                    self.process(']')
                if symbol == '(':
                    self.process('(')
                    self.compile_expression_list()
                    self.process(')')
        self.tab_number -= 1
        self.write('</term>')

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # Your code goes here!
        self.write('<expressionList>')
        self.tab_number += 1
        while True:
            if self.input_stream.token_type() == 'SYMBOL' and self.input_stream.symbol()==')':
                break
            if self.input_stream.token_type() == 'SYMBOL' and self.input_stream.symbol()==',':
                self.process(',')
            else:
                self.compile_expression()
        self.tab_number -= 1
        self.write('</expressionList>')
