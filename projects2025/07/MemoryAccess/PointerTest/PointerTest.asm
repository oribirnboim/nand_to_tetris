//push
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop
@SP
M=M-1
A=M
D=M
@3
M=D
//push
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop
@SP
M=M-1
A=M
D=M
@4
M=D
//push
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop
@2
D=A
@THIS
M=D+M
@SP
M=M-1
A=M
D=M
@THIS
A=M
M=D
@2
D=A
@THIS
M=M-D
//push
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop
@6
D=A
@THAT
M=D+M
@SP
M=M-1
A=M
D=M
@THAT
A=M
M=D
@6
D=A
@THAT
M=M-D
//push
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push
@THAT
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
//push
@2
D=A
@THIS
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
//push
@6
D=A
@THAT
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
