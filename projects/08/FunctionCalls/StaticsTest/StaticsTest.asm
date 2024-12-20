// bootstraping
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
// call Sys.init
// Pushes return address
@Sys.init.Sys_helper0
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
@5
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Sys.init
@Sys.init
0;JMP
(Sys.init.Sys_helper0)
(Sys.init)
//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class1.set
// Pushes return address
@Class1.set.Sys_helper0
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
@7
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Class1.set
@Class1.set
0;JMP
(Class1.set.Sys_helper0)
//pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D
//push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class2.set
// Pushes return address
@Class2.set.Sys_helper1
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
@7
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Class2.set
@Class2.set
0;JMP
(Class2.set.Sys_helper1)
//pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D
// call Class1.get
// Pushes return address
@Class1.get.Sys_helper2
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
@5
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Class1.get
@Class1.get
0;JMP
(Class1.get.Sys_helper2)
// call Class2.get
// Pushes return address
@Class2.get.Sys_helper3
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
@5
D=D-A
@ARG
M=D
// Changes LCL value
@SP
D=M
@LCL
M=D
// goes to execute the function Class2.get
@Class2.get
0;JMP
(Class2.get.Sys_helper3)
// label WHILE
(Sys.WHILE)
//goto Sys.WHILE
@Sys.WHILE
0;JMP
(Class1.set)
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
//pop static 0
@SP
M=M-1
A=M
D=M
@Class1.0
M=D
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
//pop static 1
@SP
M=M-1
A=M
D=M
@Class1.1
M=D
//push constant 0
@0
D=A
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
(Class1.get)
//push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1
@Class1.1
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
(Class2.set)
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
//pop static 0
@SP
M=M-1
A=M
D=M
@Class2.0
M=D
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
//pop static 1
@SP
M=M-1
A=M
D=M
@Class2.1
M=D
//push constant 0
@0
D=A
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
(Class2.get)
//push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1
@Class2.1
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
