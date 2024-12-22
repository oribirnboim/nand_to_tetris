"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
import os


class CodeWriter:
    """Translates VM commands into Hack assembly code."""

    def __init__(self, output_stream: typing.TextIO, input_filename: str) -> None:
        """Initializes the CodeWriter.

        Args:
            output_stream (typing.TextIO): output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        self.filename = os.path.basename(input_filename)
        self.stream = output_stream
        self.label_counter = 0
        self.functions_called = []
        self.labels = []

    def set_file_name(self, filename: str) -> None:
        """Informs the code writer that the translation of a new VM file is 
        started.

        Args:
            filename (str): The name of the VM file.
        """
        # Your code goes here!
        # This function is useful when translating code that handles the
        # static segment. For example, in order to prevent collisions between two
        # .vm files which push/pop to the static segment, one can use the current
        # file's name in the assembly variable's name and thus differentiate between
        # static variables belonging to different files.
        # To avoid problems with Linux/Windows/MacOS differences with regards
        # to filenames and paths, you are advised to parse the filename in
        # the function "translate_file" in Main.py using python's os library,
        # For example, using code similar to:
        # input_filename, input_extension = os.path.splitext(os.path.basename(input_file.name))
        self.filename = os.path.splitext(os.path.basename(filename))[0]


    def generate_helper_label(self) -> str:
        res = self.filename + '_helper' + str(self.label_counter)
        self.label_counter += 1
        return res
    

    def write(self, line: str) -> None:
        self.stream.write(line + '\n')


    def write_arithmetic(self, command: str) -> None:
            """Writes assembly code that is the translation of the given 
            arithmetic command. For the commands eq, lt, gt, you should correctly
            compare between all numbers our computer supports, and we define the
            value "true" to be -1, and "false" to be 0.

            Args:
                command (str): an arithmetic command.
            """
            # Your code goes here!
            if command in {'add', 'sub', 'and', 'or'}:
                self.write('@SP //add group')
                self.write('M=M-1')
                self.write('A=M')
                self.write('D=M')
                self.write('@SP')
                self.write('A=M-1')
                if command == 'add': self.write('M=D+M //add')
                if command == 'sub': self.write('M=M-D //sub')
                if command == 'and': self.write('M=D&M //and')
                if command == 'or': self.write('M=D|M //or')
            if command in {'neg', 'not'}:
                self.write('@SP //neg group')
                self.write('A=M-1')
                if command == 'neg': self.write('M=-M')
                elif command == 'not': self.write('M=!M')
                elif command == 'shiftleft': self.write('M=M<<')
                elif command == 'shiftright': self.write('M=M>>')
            if command == 'eq':
                end_eq = self.generate_helper_label()
                self.write('@SP')
                self.write('M=M-1')
                self.write('A=M-1')
                self.write('D=M') #D=x
                self.write('A=A+1')
                self.write('D=D-M') #D=x-y
                self.write('A=A-1')
                self.write('M=-1')
                self.write('@' + end_eq)
                if command == 'eq': self.write('D;JEQ')
                else: self.write('D;JLT')
                self.write('@SP')
                self.write('A=M-1')
                self.write('M=!M')
                self.write('(' + end_eq + ')')
                self.write('@3') #dummy line, just for end label

            if command in {'gt', 'lt'}:
                self.write('@SP //gt group')
                self.write('M=M-1')
                self.write('A=M')
                self.write('D=M')
                self.write('@R13') #y
                self.write('M=D')
                self.write('@SP')
                self.write('A=M-1')
                self.write('D=M')
                self.write('@R14') #x
                self.write('M=D')
                x_neg = self.generate_helper_label()
                same = self.generate_helper_label()
                end = self.generate_helper_label()
                self.write('@' + x_neg)
                self.write('D;JLT')

                # case x >= 0
                self.write('@R13') #load y
                self.write('D=M')
                self.write('@' + same) #if y is positive, x, y have the same sign
                self.write('D;JGE')
                self.write('@SP') #y is negative
                self.write('A=M-1')
                if command == 'gt': self.write('M=-1')
                else: self.write('M=0')
                self.write('@' + end)
                self.write('0;JMP')

                # case x < 0
                self.write('(' + x_neg + ')')
                self.write('@R13') #D=y
                self.write('D=M')
                self.write('@' + same)
                self.write('D;JLT')
                self.write('') #now x<0 and y>0 so x<y
                self.write('@SP')
                self.write('A=M-1')
                if command == 'lt': self.write('M=-1')
                else: self.write('M=0')
                self.write('@' + end)
                self.write('0;JMP')

                # case x, y have the same sign
                self.write('(' + same + ')')  
                self.write('@R13') #D=y
                self.write('D=M')
                self.write('@R14')
                self.write('D=M-D') # D=x-y
                self.write('@SP')
                self.write('A=M-1')
                self.write('M=-1')
                self.write('@' + end)
                if command == 'gt': self.write('D;JGT')
                else: self.write('D;JLT')
                self.write('@SP')
                self.write('A=M-1')
                self.write('M=!M')
                self.write('(' + end + ')')
                self.write('@3') #dummy line, just for end label



    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """Writes assembly code that is the translation of the given 
        command, where command is either C_PUSH or C_POP.

        Args:
            command (str): "C_PUSH" or "C_POP".
            segment (str): the memory segment to operate on.
            index (int): the index in the memory segment.
        """
        # Your code goes here!
        # Note: each reference to "static i" appearing in the file Xxx.vm should
        # be translated to the assembly symbol "Xxx.i". In the subsequent
        # assembly process, the Hack assembler will allocate these symbolic
        # variables to the RAM, starting at address 16.
        seg = {'local': 'LCL',
               'argument': 'ARG',
               'this': 'THIS',
               'that': 'THAT'}
        if command == 'C_POP':
            self.write(f'//pop {segment} {index}')
            if segment in seg.keys():
                self.write('@' + str(index))
                self.write('D=A')
                self.write('@' + seg[segment])
                self.write('M=D+M')
                self.write('@SP')
                self.write('M=M-1')
                self.write('A=M')
                self.write('D=M')
                self.write('@' + seg[segment])
                self.write('A=M')
                self.write('M=D')
                self.write('@' + str(index))
                self.write('D=A')
                self.write('@' + seg[segment])
                self.write('M=M-D')
            if segment == 'temp':
                self.write('@SP')
                self.write('M=M-1')
                self.write('A=M')
                self.write('D=M')
                self.write('@' + str(5 + index))
                self.write('M=D')
            if segment == 'static':
                self.write('@SP')
                self.write('M=M-1')
                self.write('A=M')
                self.write('D=M')
                self.write('@' + self.filename + '.' + str(index))
                self.write('M=D')
            if segment == 'pointer':
                if index == 0: th = 'THIS'
                else: th = 'THAT'
                self.write('@SP')
                self.write('M=M-1')
                self.write('A=M')
                self.write('D=M')
                self.write('@' + th)
                self.write('M=D')
        else:
            self.write(f'//push {segment} {index}')
            if segment in seg.keys():
                self.write('@' + str(index))
                self.write('D=A')
                self.write('@' + seg[segment])
                self.write('A=D+M')
                self.write('D=M')
                self.write('@SP')
                self.write('A=M')
                self.write('M=D')
                self.write('@SP')
                self.write('M=M+1')
            if segment == 'temp':
                self.write('@' + str(5 + index))
                self.write('D=M')
                self.write('@SP')
                self.write('A=M')
                self.write('M=D')
                self.write('@SP')
                self.write('M=M+1')
            if segment == 'static':
                self.write('@' + self.filename + '.' + str(index))
                self.write('D=M')
                self.write('@SP')
                self.write('A=M')
                self.write('M=D')
                self.write('@SP')
                self.write('M=M+1')
            if segment == 'pointer':
                if index == 0: th = 'THIS'
                else: th = 'THAT'
                self.write('@' + th)
                self.write('D=M')
                self.write('@SP')
                self.write('A=M')
                self.write('M=D')
                self.write('@SP')
                self.write('M=M+1')
            if segment == 'constant':
                self.write('@' + str(index))
                self.write('D=A')
                self.write('@SP')
                self.write('A=M')
                self.write('M=D')
                self.write('@SP')
                self.write('M=M+1')

    def write_label(self, label: str) -> None:
        """Writes assembly code that affects the label command. 
        Let "Xxx.foo" be a function within the file Xxx.vm. The handling of
        each "label bar" command within "Xxx.foo" generates and injects the symbol
        "Xxx.foo$bar" into the assembly code stream.
        When translating "goto bar" and "if-goto bar" commands within "foo",
        the label "Xxx.foo$bar" must be used instead of "bar".

        Args:
            label (str): the label to write.
        """
        self.write(f'// label {label}')
        file_label = f"{self.filename}.{label}"
        # Write the label to the output stream
        self.write(f"({file_label})")


    def write_goto(self, label: str) -> None:
        """Writes assembly code that affects the goto command.

        Args:
            label (str): the label to go to.
        """
        file_label = f"{self.filename}.{label}"
        self.write(f"//goto {file_label}")
        self.write(f"@{file_label}")
        self.write("0;JMP")


    def write_if(self, label: str) -> None:
        """Writes assembly code that affects the if-goto command. 
        
        Args:
            label (str): the label to go to if the condition is true.
        """
        file_label = f"{self.filename}.{label}"
        self.write(f"// if-goto {file_label}")
        self.write("@SP")
        self.write("M=M-1")
        self.write("A=M")
        self.write("D=M")

        self.write(f"@{file_label}")
        self.write("D;JNE")
        


    def write_function(self, function_name: str, n_vars: int) -> None:
        """Writes assembly code that affects the function command. 
        The handling of each "function Xxx.foo" command within the file Xxx.vm
        generates and injects a symbol "Xxx.foo" into the assembly code stream,
        that labels the entry-point to the function's code.
        In the subsequent assembly process, the assembler translates this 
        symbol into the physical address where the function code starts.

        Args:
            function_name (str): the name of the function.
            n_vars (int): the number of local variables of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "function function_name n_vars" is:
        # (function_name)       // injects a function entry label into the code
        # repeat n_vars times:  // n_vars = number of local variables
        #   push constant 0     // initializes the local variables to 0
    
        self.write(f"({function_name})")
        
        # inits n_vars local vars to 0.
        for var_num in range(n_vars):
            self.write(f"// Inits {var_num} local variable to 0.")
            self.write_push_pop("push", "constant", 0)


    def write_call(self, function_name: str, n_args: int) -> None:
        """Writes assembly code that affects the call command. 
        Let "Xxx.foo" be a function within the file Xxx.vm.
        The handling of each "call" command within Xxx.foo's code generates and
        injects a symbol "Xxx.foo$ret.i" into the assembly code stream, where
        "i" is a running integer (one such symbol is generated for each "call"
        command within "Xxx.foo").
        This symbol is used to mark the return address within the caller's 
        code. In the subsequent assembly process, the assembler translates this
        symbol into the physical memory address of the command immediately
        following the "call" command.

        Args:
            function_name (str): the name of the function to call.
            n_args (int): the number of arguments of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "call function_name n_args" is:
        # push return_address   // generates a label and pushes it to the stack
        # push LCL              // saves LCL of the caller
        # push ARG              // saves ARG of the caller
        # push THIS             // saves THIS of the caller
        # push THAT             // saves THAT of the caller
        # ARG = SP-5-n_args     // repositions ARG
        # LCL = SP              // repositions LCL
        # goto function_name    // transfers control to the callee
        # (return_address)      // injects the return address label into the code

        self.write(f"// call {function_name}")
        self.write("// Pushes return address")
        # creates a new label
        return_label = f'{function_name}.{self.generate_helper_label()}'
        self.write(f'@{return_label}')
        self.write("D=A")
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

        
        # Push LCL, ARG, THIS, THAT in that order
        for segment in ["LCL", "ARG", "THIS", "THAT"]:
            self.write(f"// Pushes {segment}")
            self.write(f"@{segment}")
            self.write("D=M")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
        
        # changing ARG value
        self.write("// Changes ARG value")
        self.write(f"@SP")
        self.write("D=M")
        self.write(f"@{n_args + 5}")
        self.write("D=D-A")
        self.write("@ARG")
        self.write("M=D")
        
        # changing LCL value
        self.write("// Changes LCL value")
        self.write("@SP")
        self.write("D=M")
        self.write("@LCL")
        self.write("M=D")
        
        #goto function
        self.write(f"// goes to execute the function {function_name}")
        self.write(f"@{function_name}")
        self.write("0;JMP")

        # (return_address)
        self.write(f'({return_label})')



    def write_return(self) -> None: # probably true
        """Writes assembly code that affects the return command."""
        # The pseudo-code of "return" is:
        # frame = LCL                   // frame is a temporary variable
        # return_address = *(frame-5)   // puts the return address in a temp var
        # *ARG = pop()                  // repositions the return value for the caller
        # SP = ARG + 1                  // repositions SP for the caller
        # THAT = *(frame-1)             // restores THAT for the caller
        # THIS = *(frame-2)             // restores THIS for the caller
        # ARG = *(frame-3)              // restores ARG for the caller
        # LCL = *(frame-4)              // restores LCL for the caller
        # goto return_address           // go to the return address
            
        self.write("// return")

        # frame = LCL
        self.write("// frame = LCL")
        self.write("@LCL")
        self.write("D=M")
        self.write("@R13")  # R13 will store FRAME
        self.write("M=D")
        
        # return_address = *(frame - 5)
        self.write("@R13")
        self.write("D=M")
        self.write("@5")
        self.write("A=D-A")  
        self.write("D=M")
        self.write("@R14")
        self.write("M=D")
        
        # *ARG = pop()
        self.write("// *ARG = pop()")
        self.write("@SP")
        self.write("M=M-1")
        self.write("A=M")
        self.write("D=M")
        self.write("@ARG")
        self.write("A=M")
        self.write("M=D")


        
        # SP = ARG + 1
        self.write("// SP = ARG + 1")
        self.write("@ARG")
        self.write("D=M+1")
        self.write("@SP")
        self.write("M=D")
        
        # LCL, ARG, THIS, THAT = *(FRAME - i)
        for i, segment in enumerate(["THAT", "THIS", "ARG", "LCL"]):
            self.write(f"// {segment} = *(FRAME - {str(i+1)})")
            self.write("@R13")
            self.write("D=M")
            self.write(f"@{i + 1}")
            self.write("A=D-A")
            self.write("D=M")
            self.write(f"@{segment}")
            self.write("M=D")
        
        # goto return_address
        self.write("// goto return_address")
        self.write("@R14")
        self.write("A=M")
        self.write("0;JMP")

        


    def init_segment_values(self) -> None:
        segment_init_value = {
            'SP': 256,
            'LCL': 300,
            'ARG': 400,
            'THIS': 3000,
            'THAT': 3010
        }
        
        self.write("// bootstraping")
        for segment in segment_init_value.keys():
            seg_value = segment_init_value[segment]
            self.write(f"@{seg_value}")
            self.write("D=A")
            self.write(f"@{segment}")
            self.write("M=D")

        self.write_call("Sys.init", 0)


    