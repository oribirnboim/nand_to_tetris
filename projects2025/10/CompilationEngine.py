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
                
        self.recurtion_depth = 0 # used to count the number of tabs

    def write(self, string: str) -> None:
        self.output_stream.write(("\t" * self.recurtion_depth) + string + "/n") 

    def write_identifier(self,identifier) -> None:
        self.write(f"<identifier> {identifier} </identifier>")
        self.input_stream.advance()

    def handle_varName() -> None:
        var_name = self.input_stream.identifier()
        self.write_identifier(var_name)
        self.input_stream.advance()

    def handle_type():
        var_type = self.input_stream.token_type()
        if var_type == "KEYWORD":
            var_kind = self.input_stream.keyword()
            self.write(var_kind)
            self.input_stream.advance()
        else:
            var_kind = self.input_stream.identifier()
            self.write_identifier(var_kind)

    def compile_class(self) -> None:
        """Compiles a complete class."""

        self.write("<class>")
        self.recurtion_depth += 1
        
        self.process("class")
        self.input_stream.advance()

        class_name = self.input_stream.identifier() 
        self.write_identifier(class_name)

        self.process("{")

        while self.output_stream.tokentype() == "KEYWORD":
            token_value = self.input_stream.keyword()
            if token_value in {"field","static"}:
                self.compile_class_var_dec()
            elif token_value in {"method", "constructor","function"}:
                self.compile_subroutine()
            else:
                print("syntax error - class function that isnt varDec or subroutine.")

        self.process("}")

        self.recurtion_depth -= 1
        self.write("</class>")     
        self.input_stream.advance()   
        
    def process(self, token: str) -> None:
        type = self.input_stream.token_type()
        if type == "KEYWORD":
            current = self.input_stream.keyword()
            self.write('<keyword> ' + current + ' </keyword>')
        if type == "SYMBOL":
            current = self.input_stream.symbol()
            self.write('<symbol> ' + current + ' </symbol>')
        if current != token: print('expected ' + token + ', got '+ current)
        self.input_stream.advance()

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        self.write("<classVarDec>")
        self.recurtion_depth += 1

        # handles (static|field) section
        dec_type = self.input_stream.keyword()
        self.process(dec_type)

        self.handle_type()

        # handles the first varName
        self.handle_varName()

        # handles possible other varNames
        symbol_value = self.output_stream.symbol()
        while symbol_value != ";":
            self.process(",")
            self.handle_varName()
            symbol_value = self.input_stream.symbol()
        
        self.process(";")

        self.recurtion_depth -= 1
        self.write("</classVarDec>")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        self.write("<subroutineDec>")
        self.recurtion_depth += 1
        
        subroutine_type = self.input_stream.keyword()
        self.process(subroutine_type)
        
        subroutine_output_type = self.input_stream.token_type()
        if subroutine_output_type == "KEYWORD":
            subroutine_output_kind = self.input_stream.keyword()
        else:
            subroutine_output_kind = self.input_stream.identifier()
        self.write(subroutine_output_kind)
        self.input_stream.advance()

        subroutine_name = self.input_stream.identifier()
        self.write(subroutine_name)
        self.

        self.process("(")
        
        self.compile_parameter_list()

        self.process(")")
        
        self.process("{")

        self.compile_var_dec()

        self.compile_statements()

        self.process("}")
    
        self.recurtion_depth -= 1
        self.write("</subroutineDec>")

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the 
        enclosing "()".
        """


        self.handle_type()
        self.handle_varName()

        symbol = self.output_stream.symbol()
        while symbol == ",":
            self.process(symbol)
            self.handle_type()
            self.handle_varName()
            symbol = self.output_stream.symbol()

        self.process(")")

        self.recurtion_depth -= 1
        self.write("</parameterList>")

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        self.write("<varDec>")
        self.recurtion_depth += 1

        self.write("<parameterList>")
        self.recurtion_depth += 1

        self.process("var")

        self.handle_type()

        self.handle_varName()

        while symbol == ",":
            self.process(symbol)
            self.handle_varName()
            symbol = self.output_stream.symbol()

        self.process(")")            
        

        self.recurtion_depth -= 1
        self.write("</parameterList>")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing 
        "{}".
        """
        # Your code goes here!
        pass

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # Your code goes here!
        self.write('<doStatement>')
        self.recurtion_depth += 1
        self.process('do')
        self.compile_expression()
        self.recurtion_depth -= 1
        self.write('</doStatement>')

    def compile_let(self) -> None:
        """Compiles a let statement."""
        # Your code goes here!
        self.write('<letStatement>')
        self.recurtion_depth += 1
        self.process('let')
        identifier = self.input_stream.identifier()
        self.write('<identifier> ' + identifier + ' </identifier>')
        self.input_stream.advance()
        if self.input_stream.token_type()=='SYMBOL':
            self.process('[')
            self.compile_expression()
            self.process(']')
        self.process('=')
        self.compile_expression()
        self.process(';')
        self.recurtion_depth -= 1
        self.write('</letStatement>')

    def compile_while(self) -> None:
        """Compiles a while statement."""
        # Your code goes here!
        self.write('<whileStatement>')
        self.recurtion_depth += 1
        self.process('while')
        self.process('(')
        self.compile_expression()
        self.process(')')
        self.process('{')
        self.compile_statements()
        self.process('}')
        self.recurtion_depth -= 1
        self.write('</whileStatement>')

    def compile_return(self) -> None:
        """Compiles a return statement."""
        # Your code goes here!
        self.write('<returnStatement>')
        self.recurtion_depth += 1
        self.process('return')
        type = self.input_stream.token_type()
        if type != "SYMBOL":
            self.compile_expression()
        self.process('}')
        self.recurtion_depth -= 1
        self.write('</returnStatement>')

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!
        self.write('<ifStatement>')
        self.recurtion_depth += 1
        self.process('if')
        self.process('(')
        self.compile_expression()
        self.process(')')
        self.process('{')
        self.compile_statements()
        self.process('}')
        if self.input_stream.token_type()=='KEYWORD':
            if self.input_stream.keword()=='ELSE':
                self.process('else')
                self.process('{')
                self.compile_statements()
                self.process('}')
        self.recurtion_depth -= 1
        self.write('</ifStatement>')

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        ops = {'+', '-', '*', '/', '&', '|', '<', '>', '='}
        self.write('<expression>')
        self.recurtion_depth += 1
        self.compile_term()
        while self.input_stream.token_type()=='SYMBOL' and (self.input_stream.symbol() in ops):
            op = self.input_stream.symbol()
            self.process(op)
            self.compile_term()
        self.recurtion_depth -= 1
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
        self.write('<term>')
        self.recurtion_depth += 1
        type = self.input_stream.token_type()
        if type == "INT_CONST":
            self.write('<integerConstant> ' + self.input_stream.int_val() + ' </integerConstant>')
        
        self.recurtion_depth += 1
        self.write('</term>')

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # Your code goes here!
        pass
