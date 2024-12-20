(Sys.init)
//push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
// call Sys.main
// Pushes return address
@Sys.main.Sys_helper0
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
// goes to execute the function Sys.main
@Sys.main
0;JMP
(Sys.main.Sys_helper0)
//pop temp 1
@SP
M=M-1
A=M
D=M
@6
M=D
// label LOOP
(Sys.LOOP)
//goto Sys.LOOP
@Sys.LOOP
0;JMP
(Sys.main)
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
// Inits 2 local variable to 0.
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// Inits 3 local variable to 0.
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// Inits 4 local variable to 0.
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 1
@1
D=A
@LCL
M=D+M
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
@1
D=A
@LCL
M=M-D
//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 2
@2
D=A
@LCL
M=D+M
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
@2
D=A
@LCL
M=M-D
//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 3
@3
D=A
@LCL
M=D+M
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
@3
D=A
@LCL
M=M-D
//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Sys.add12
// Pushes return address
@Sys.add12.Sys_helper1
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
// goes to execute the function Sys.add12
@Sys.add12
0;JMP
(Sys.add12.Sys_helper1)
//pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D
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
//push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 4
@4
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
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M //add
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M //add
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
(Sys.add12)
//push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
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
//push constant 12
@12
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
