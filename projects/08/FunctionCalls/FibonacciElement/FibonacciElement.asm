(Sys.init)
//push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci
// Pushes return address
@Main.fibonacci.Sys_helper0
D=A
@SP
A=M
M=D
@SP
M=M+1
// Pushes LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Changes ARG value
@SP
D=M
@6
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci.Sys_helper0)
// label WHILE
(Sys.WHILE)
//goto Sys.WHILE
@Sys.WHILE
0;JMP
(Main.fibonacci)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP //eq group
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
M=-1
@Main_helper0
D;JLT
@SP
A=M-1
M=!M
(Main_helper0)
// if-goto Main.IF_TRUE
@SP
M=M-1
A=M
D=M
@Main.IF_TRUE
D;JNE
//goto Main.IF_FALSE
@Main.IF_FALSE
0;JMP
// label IF_TRUE
(Main.IF_TRUE)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// return
// frame = LCL
@LCL
D=M
@R13
M=D
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(FRAME - 1)
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(FRAME - 2)
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(FRAME - 3)
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(FRAME - 4)
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto return_address
@R14
A=M
0;JMP
// label IF_FALSE
(Main.IF_FALSE)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D //sub
// call Main.fibonacci
// Pushes return address
@Main.fibonacci.Main_helper1
D=A
@SP
A=M
M=D
@SP
M=M+1
// Pushes LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Changes ARG value
@SP
D=M
@6
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci.Main_helper1)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D //sub
// call Main.fibonacci
// Pushes return address
@Main.fibonacci.Main_helper2
D=A
@SP
A=M
M=D
@SP
M=M+1
// Pushes LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Pushes THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Changes ARG value
@SP
D=M
@6
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci.Main_helper2)
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M //add
// return
// frame = LCL
@LCL
D=M
@R13
M=D
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(FRAME - 1)
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(FRAME - 2)
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(FRAME - 3)
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(FRAME - 4)
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto return_address
@R14
A=M
0;JMP
