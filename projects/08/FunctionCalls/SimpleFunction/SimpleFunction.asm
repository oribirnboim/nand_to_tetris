(SimpleFunction.test)
// Inits 0 local variable to 0.
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// Inits 1 local variable to 0.
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 1
@1
D=A
@LCL
A=D+M
D=M
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
M=D+M //add
@SP //neg group
A=M-1
M=!M
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
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M //add
//push argument 1
@1
D=A
@ARG
A=D+M
D=M
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
