"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
from Parser import Parser
from CodeWriter import CodeWriter


def translate_file(
        input_file: typing.TextIO, input_filename: str, output_file: typing.TextIO) -> None:
    """Translates a single file.

    Args:
        input_file (typing.TextIO): the file to translate.
        output_file (typing.TextIO): writes all output to this file.
    """
    # Your code goes here!
    # It might be good to start with something like:
    # parser = Parser(input_file)
    # code_writer = CodeWriter(output_file)
    parser = Parser(input_file)
    code_writer = CodeWriter(output_file, input_filename)
    while parser.has_more_commands():
        parser.advance()
        cmd_type = parser.command_type()
        
        if cmd_type == 'C_ARITHMETIC':
            command = parser.arg1()
            code_writer.write_arithmetic(command)
        
        if cmd_type in {'C_PUSH', 'C_POP'}:
            segment = parser.arg1()
            index = parser.arg2()
            code_writer.write_push_pop(cmd_type, segment, index)
        
        if cmd_type == 'C_LABEL':
            label = parser.arg1()
            code_writer.write_label(label)
        
        if cmd_type == 'C_GOTO':
            label = parser.arg1()
            code_writer.write_goto(label)
        
        if cmd_type == 'C_IF':
            label = parser.arg1()
            code_writer.write_if(label)
        
        if cmd_type == 'C_FUNCTION':
            function_name = parser.arg1()
            n_vars = parser.arg2()
            code_writer.write_function(function_name, n_vars)
        
        if cmd_type == 'C_CALL':
            function_name = parser.arg1()
            n_args = parser.arg2()
            code_writer.write_call(function_name, n_args)
        
        if cmd_type == 'C_RETURN':
            code_writer.write_return()
            
def init_values(input_file: typing.TextIO, input_filename: str, output_file: typing.TextIO) -> None:
    code_writer = CodeWriter(output_file, input_filename)
    code_writer.init_segment_values()

if "__main__" == __name__:
    # Parses the input path and calls translate_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: VMtranslator <input path>")
    
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        # Collect all .vm files in the directory
        files_to_translate = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)
            if filename.lower().endswith(".vm")
        ]
        # Ensure Sys.vm is the first file to translate, if it exists
        sys_file_path = os.path.join(argument_path, "Sys.vm")
        if sys_file_path in files_to_translate:
            files_to_translate.remove(sys_file_path)
            files_to_translate.insert(0, sys_file_path)
        
        # Set output file name based on the directory name
        output_path = os.path.join(argument_path, os.path.basename(argument_path))
    else:
        # Single file translation
        files_to_translate = [argument_path]
        output_path, extension = os.path.splitext(argument_path)
    
    output_path += ".asm"
    file_0 = files_to_translate[0]
    filename0, extension0 = os.path.splitext(file_0)

    # Translate files and write to the output file
    with open(output_path, 'w') as output_file:
        init_values(file_0,filename0,output_file)
        for input_path in files_to_translate:
            filename, extension = os.path.splitext(input_path)
            if extension.lower() != ".vm":
                continue
            with open(input_path, 'r') as input_file:
                translate_file(input_file, filename, output_file)
