//push
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@32767
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
//push
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP //gt group
M=M-1
A=M
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@StackTestOverflow_helper0
D;JLT
@R13
D=M
@StackTestOverflow_helper1
D;JGE
@SP
A=M-1
M=0
@StackTestOverflow_helper2
0;JMP
(StackTestOverflow_helper0)
@R13
D=M
@StackTestOverflow_helper1
D;JLT

@SP
A=M-1
M=-1
@StackTestOverflow_helper2
0;JMP
(StackTestOverflow_helper1)
@R13
D=M
@R14
D=M-D
@SP
A=M-1
M=-1
@StackTestOverflow_helper2
D;JLT
@SP
A=M-1
M=!M
(StackTestOverflow_helper2)
@3
//push
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@32767
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
@SP //gt group
M=M-1
A=M
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@StackTestOverflow_helper3
D;JLT
@R13
D=M
@StackTestOverflow_helper4
D;JGE
@SP
A=M-1
M=0
@StackTestOverflow_helper5
0;JMP
(StackTestOverflow_helper3)
@R13
D=M
@StackTestOverflow_helper4
D;JLT

@SP
A=M-1
M=-1
@StackTestOverflow_helper5
0;JMP
(StackTestOverflow_helper4)
@R13
D=M
@R14
D=M-D
@SP
A=M-1
M=-1
@StackTestOverflow_helper5
D;JLT
@SP
A=M-1
M=!M
(StackTestOverflow_helper5)
@3
//push
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@32767
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
//push
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP //gt group
M=M-1
A=M
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@StackTestOverflow_helper6
D;JLT
@R13
D=M
@StackTestOverflow_helper7
D;JGE
@SP
A=M-1
M=-1
@StackTestOverflow_helper8
0;JMP
(StackTestOverflow_helper6)
@R13
D=M
@StackTestOverflow_helper7
D;JLT

@SP
A=M-1
M=0
@StackTestOverflow_helper8
0;JMP
(StackTestOverflow_helper7)
@R13
D=M
@R14
D=M-D
@SP
A=M-1
M=-1
@StackTestOverflow_helper8
D;JGT
@SP
A=M-1
M=!M
(StackTestOverflow_helper8)
@3
//push
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@32767
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
@SP //gt group
M=M-1
A=M
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@StackTestOverflow_helper9
D;JLT
@R13
D=M
@StackTestOverflow_helper10
D;JGE
@SP
A=M-1
M=-1
@StackTestOverflow_helper11
0;JMP
(StackTestOverflow_helper9)
@R13
D=M
@StackTestOverflow_helper10
D;JLT

@SP
A=M-1
M=0
@StackTestOverflow_helper11
0;JMP
(StackTestOverflow_helper10)
@R13
D=M
@R14
D=M-D
@SP
A=M-1
M=-1
@StackTestOverflow_helper11
D;JGT
@SP
A=M-1
M=!M
(StackTestOverflow_helper11)
@3
