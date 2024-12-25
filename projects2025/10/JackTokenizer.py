"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
import os


symbols = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '^', '#'}
keywords = { 'class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'}

class JackTokenizer:
    """Removes all comments from the input stream and breaks it
    into Jack language tokens, as specified by the Jack grammar.
    
    # Jack Language Grammar

    A Jack file is a stream of characters. If the file represents a
    valid program, it can be tokenized into a stream of valid tokens. The
    tokens may be separated by an arbitrary number of whitespace characters, 
    and comments, which are ignored. There are three possible comment formats: 
    /* comment until closing */ , /** API comment until closing */ , and 
    // comment until the line’s end.

    - ‘xxx’: quotes are used for tokens that appear verbatim (‘terminals’).
    - xxx: regular typeface is used for names of language constructs 
           (‘non-terminals’).
    - (): parentheses are used for grouping of language constructs.
    - x | y: indicates that either x or y can appear.
    - x?: indicates that x appears 0 or 1 times.
    - x*: indicates that x appears 0 or more times.

    ## Lexical Elements

    The Jack language includes five types of terminal elements (tokens).

    - keyword: 'class' | 'constructor' | 'function' | 'method' | 'field' | 
               'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' |
               'false' | 'null' | 'this' | 'let' | 'do' | 'if' | 'else' | 
               'while' | 'return'
    - symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' | 
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
    - integerConstant: A decimal number in the range 0-32767.
    - StringConstant: '"' A sequence of Unicode characters not including 
                      double quote or newline '"'
    - identifier: A sequence of letters, digits, and underscore ('_') not 
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.

    ## Program Structure

    A Jack program is a collection of classes, each appearing in a separate 
    file. A compilation unit is a single class. A class is a sequence of tokens 
    structured according to the following context free syntax:
    
    - class: 'class' className '{' classVarDec* subroutineDec* '}'
    - classVarDec: ('static' | 'field') type varName (',' varName)* ';'
    - type: 'int' | 'char' | 'boolean' | className
    - subroutineDec: ('constructor' | 'function' | 'method') ('void' | type) 
    - subroutineName '(' parameterList ')' subroutineBody
    - parameterList: ((type varName) (',' type varName)*)?
    - subroutineBody: '{' varDec* statements '}'
    - varDec: 'var' type varName (',' varName)* ';'
    - className: identifier
    - subroutineName: identifier
    - varName: identifier

    ## Statements

    - statements: statement*
    - statement: letStatement | ifStatement | whileStatement | doStatement | 
                 returnStatement
    - letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
    - ifStatement: 'if' '(' expression ')' '{' statements '}' ('else' '{' 
                   statements '}')?
    - whileStatement: 'while' '(' 'expression' ')' '{' statements '}'
    - doStatement: 'do' subroutineCall ';'
    - returnStatement: 'return' expression? ';'

    ## Expressions
    
    - expression: term (op term)*
    - term: integerConstant | stringConstant | keywordConstant | varName | 
            varName '['expression']' | subroutineCall | '(' expression ')' | 
            unaryOp term
    - subroutineCall: subroutineName '(' expressionList ')' | (className | 
                      varName) '.' subroutineName '(' expressionList ')'
    - expressionList: (expression (',' expression)* )?
    - op: '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
    - unaryOp: '-' | '~' | '^' | '#'
    - keywordConstant: 'true' | 'false' | 'null' | 'this'
    
    Note that ^, # correspond to shiftleft and shiftright, respectively.
    """

    def __init__(self, input_stream: typing.TextIO) -> None:
        """Opens the input stream and gets ready to tokenize it.

        Args:
            input_stream (typing.TextIO): input stream.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:
        # input_lines = input_stream.read().splitlines()
        input = input_stream.read()
        input = self.clean_comments(input)
        self.tokens = self.create_token_list(input)
        self.index = 0
        self.current = self.tokens[0]

    def has_more_tokens(self) -> bool:
        """Do we have more tokens in the input?

        Returns:
            bool: True if there are more tokens, False otherwise.
        """
        # Your code goes here!
        return self.index < len(self.tokens) - 1

    def advance(self) -> None:
        """Gets the next token from the input and makes it the current token. 
        This method should be called if has_more_tokens() is true. 
        Initially there is no current token.
        """
        # Your code goes here!
        self.index += 1
        self.current = self.tokens[self.index]

    def token_type(self) -> str:
        """
        Returns:
            str: the type of the current token, can be
            "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        """
        token = self.current
        if token[0] == '"':
            return 'STRING_CONST'
        if token[0].isdigit():
            return "INT_CONST"
        if token in symbols:
            return "SYMBOL"
        if token in keywords:
            return "KEYWORD"
        return "IDENTIFIER"
        
    def keyword(self) -> str:
        """
        Returns:
            str: the keyword which is the current token.
            Should be called only when token_type() is "KEYWORD".
            Can return "CLASS", "METHOD", "FUNCTION", "CONSTRUCTOR", "INT", 
            "BOOLEAN", "CHAR", "VOID", "VAR", "STATIC", "FIELD", "LET", "DO", 
            "IF", "ELSE", "WHILE", "RETURN", "TRUE", "FALSE", "NULL", "THIS"
        """
        # Your code goes here!
        return self.current.upper()

    def symbol(self) -> str:
        """
        Returns:
            str: the character which is the current token.
            Should be called only when token_type() is "SYMBOL".
            Recall that symbol was defined in the grammar like so:
            symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' | 
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
        """
        # Your code goes here!
        return self.current     

    def identifier(self) -> str:
        """
        Returns:
            str: the identifier which is the current token.
            Should be called only when token_type() is "IDENTIFIER".
            Recall that identifiers were defined in the grammar like so:
            identifier: A sequence of letters, digits, and underscore ('_') not 
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.
        """
        # Your code goes here!
        return self.current

    def int_val(self) -> int:
        """
        Returns:
            str: the integer value of the current token.
            Should be called only when token_type() is "INT_CONST".
            Recall that integerConstant was defined in the grammar like so:
            integerConstant: A decimal number in the range 0-32767.
        """
        # Your code goes here!
        return int(self.current)

    def string_val(self) -> str:
        """
        Returns:
            str: the string value of the current token, without the double 
            quotes. Should be called only when token_type() is "STRING_CONST".
            Recall that StringConstant was defined in the grammar like so:
            StringConstant: '"' A sequence of Unicode characters not including 
                      double quote or newline '"'
        """
        # Your code goes here!
        return self.current[1:-1]

    def clean_comments(self, input: str) -> str:
        comment_blocks = []
        state = 'no_comment'
        for i in range(len(input)-1):
            current = input[i: i+2]
            if state == 'no_comment':
                if current == '/*':
                    comment_begin = i
                    state = 'multi_line'
                if current == '//':
                    comment_begin = i
                    state = 'single_line'
                continue
            if state == 'multi_line':
                if current == '*/':
                    comment_blocks.append((comment_begin, i+2))
                    state = 'no_comment'
                continue
            if state == 'single_line':
                if current[0] == '\n':
                    comment_blocks.append((comment_begin, i+1))
                    state = 'no_comment'
        if state != 'no_comment':
            comment_blocks.append((comment_begin, len(input)))
        for block in comment_blocks[::-1]:
            input = input[:block[0]] + ' ' + input[block[1]:]
        return input
    
    def create_token_list(self, input):
        tokens = []
        words = self.split_except_strings(input)
        words = list(filter(None, words))
        for w in words:
            tokens.extend(self.tokens_from_word(w))
        return tokens
    
    def tokens_from_word(self, word: str):
        by_strings = self.split_by_strings(word)
        by_symbols = []
        for word in by_strings: by_symbols += self.split_by_symbols(word)
        return by_symbols

    def split_by_strings(self, word):
        string_indices = []
        res = []
        for i in range(len(word)):
            if word[i] == '"': string_indices.append(i)
        if len(string_indices) == 0: return [word]
        start = 0
        for i in range(int(len(string_indices)/2)):
            end = string_indices[2*i]
            res.append(word[start:end])
            start = string_indices[2*i+1]+1
            res.append(word[end:start])
        if string_indices[-1] < len(word) - 1:
            res.append(word[start:])
        return res
    
    def split_by_symbols(self, word):
        if not word: return []
        if word[0]=='"': return [word]
        res = []
        symbol_indices = []
        for i in range(len(word)):
            if word[i] in symbols: symbol_indices.append(i)
        start_index = 0
        for s in symbol_indices:
            res.append(word[start_index:s])
            res.append(word[s:s+1])
            start_index = s+1
        res.append(word[start_index:])
        return list(filter(lambda s: s != "", res))

    def split_except_strings(self, input):
        on = False
        for i in range(len(input)):
            c = input[i]
            if c == '"': on = not on
            if c.isspace():
                if on: continue
                return [input[:i]] + self.split_except_strings(input[i+1:])
        return []

    def get_value(self) -> str:
        return self.current

    def write_tokens(self, output_stream) -> None:
        output_stream.write('<tokens>\n')
        while(self.has_more_tokens()):
            if self.token_type() == 'SYMBOL':
                symbol = self.symbol()
                if symbol == '<': symbol = '&lt;'
                if symbol == '>': symbol = '&gt;'
                if symbol == '&': symbol = '&amp;'
                output_stream.write('<symbol> ' + symbol + ' </symbol>\n')
            if self.token_type() == 'IDENTIFIER':
                output_stream.write('<identifier> ' + self.identifier() + ' </identifier>\n')
            if self.token_type() == 'STRING_CONST':
                output_stream.write('<stringConstant> ' + self.string_val() + ' </stringConstant>\n')
            if self.token_type() == 'INT_CONST':
                output_stream.write('<integerConstant> ' + str(self.int_val()) + ' </integerConstant>\n')
            if self.token_type() == 'KEYWORD':
                output_stream.write('<keyword> ' + self.keyword().lower() + ' </keyword>\n')
            self.advance()
        if self.token_type() == 'SYMBOL':
            symbol = self.symbol()
            if symbol == '<': symbol = '&lt;'
            if symbol == '>': symbol = '&gt;'
            if symbol == '&': symbol = '&amp;'
            output_stream.write('<symbol> ' + symbol + ' </symbol>\n')
        if self.token_type() == 'IDENTIFIER':
            output_stream.write('<identifier> ' + self.identifier() + ' </identifier>\n')
        if self.token_type() == 'STRING_CONST':
            output_stream.write('<stringConstant> ' + self.string_val() + ' </stringConstant>\n')
        if self.token_type() == 'INT_CONST':
            output_stream.write('<integerConstant> ' + str(self.int_val()) + ' </integerConstant>\n')
        if self.token_type() == 'KEYWORD':
            output_stream.write('<keyword> ' + self.keyword().lower() + ' </keyword>\n')
        output_stream.write('</tokens>\n')


if __name__ == "__main__":
    argument_path = 'Square\Square.jack'
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".jack":
            continue
        output_path = 'tokens.xml'
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            j = JackTokenizer(input_stream=input_file)
            j.write_tokens(output_file)
