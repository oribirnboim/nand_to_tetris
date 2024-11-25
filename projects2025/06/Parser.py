"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class Parser:
    """Encapsulates access to the input code. Reads an assembly program
    by reading each command line-by-line, parses the current command,
    and provides convenient access to the commands components (fields
    and symbols). In addition, removes all white space and comments.
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Opens the input file and gets ready to parse it.

        Args:
            input_file (typing.TextIO): input file.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:
        # input_lines = input_file.read().splitlines()
        input_lines = input_file.read().splitlines()
        self.commands = []
        for line in input_lines:
            comment_index = line.find("//")
            if comment_index >= 0: line = line[0:comment_index]
            line = line.strip()
            if line != "": self.commands.append(line)
        self.current_line = 0


    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        # Your code goes here!
        return self.current_line < len(self.commands) - 1


    def restart(self) -> None:
        self.current_line = 0


    def advance(self) -> None:
        """Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        """
        # Your code goes here!
        self.current_line += 1


    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current command:
            "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
            "C_COMMAND" for dest=comp;jump
            "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
        # Your code goes here!
        # print(self.current_line)
        command = self.commands[self.current_line]
        if command[0] == '(': return "L_COMMAND"
        if command[0] == '@': return "A_COMMAND"
        return "C_COMMAND"
    

    def symbol(self) -> str:
        """
        Returns:
            str: the symbol or decimal Xxx of the current command @Xxx or
            (Xxx). Should be called only when command_type() is "A_COMMAND" or 
            "L_COMMAND".
        """
        # Your code goes here!
        command = self.commands[self.current_line]
        if self.command_type() == "A_COMMAND": return command[1:].strip()
        return command[1:-1].strip()
    

    def dest(self) -> str:
        """
        Returns:
            str: the dest mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        # Your code goes here!
        command = self.commands[self.current_line]
        eq_index = command.find('=')
        if eq_index >= 0:
            return command[:eq_index].strip()
        return ""
    

    def comp(self) -> str:
        """
        Returns:
            str: the comp mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        # Your code goes here!
        command = self.commands[self.current_line]
        eq_index = command.find('=')
        jump_index = command.find(';')
        if eq_index >= 0:
            if jump_index < 0: return command[eq_index+1:].strip()
            return command[eq_index+1:jump_index].strip()
        if jump_index >= 0:
            return command[:jump_index].strip()
        return command.strip()
    

    def jump(self) -> str:
        """
        Returns:
            str: the jump mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        # Your code goes here!
        command = self.commands[self.current_line]
        jump_index = command.find(';')
        if jump_index < 0: return ''
        return command[jump_index+1:].strip()