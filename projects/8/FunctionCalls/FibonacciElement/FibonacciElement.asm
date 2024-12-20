@256
D=A
@SP
M=D
@300
D=A
@LCL
M=D
@400
D=A
@ARG
M=D
@3000
D=A
@THIS
M=D
@3010
D=A
@THAT
M=D
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
// label END
(Sys.END)
//goto Sys.END
@Sys.END
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
// if-goto Main.N_LT_2
@SP
M=M-1
A=M
D=M
@Main.N_LT_2
D;JNE
//goto Main.N_GE_2
@Main.N_GE_2
0;JMP
// label N_LT_2
(Main.N_LT_2)
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
// label N_GE_2
(Main.N_GE_2)
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
