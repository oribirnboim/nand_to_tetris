//push
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@17
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
@StackTest_helper0
D;JEQ
@SP
A=M-1
M=!M
(StackTest_helper0)
//push
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@16
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
@StackTest_helper1
D;JEQ
@SP
A=M-1
M=!M
(StackTest_helper1)
//push
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@17
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
@StackTest_helper2
D;JEQ
@SP
A=M-1
M=!M
(StackTest_helper2)
//push
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@891
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
@StackTest_helper3
D;JLT
@SP
A=M-1
M=!M
(StackTest_helper3)
//push
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@892
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
@StackTest_helper4
D;JLT
@SP
A=M-1
M=!M
(StackTest_helper4)
//push
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@891
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
@StackTest_helper5
D;JLT
@SP
A=M-1
M=!M
(StackTest_helper5)
//push
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@32766
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
@StackTest_helper6
D;JGT
@SP
A=M-1
M=!M
(StackTest_helper6)
//push
@32766
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
@SP //eq group
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
M=-1
@StackTest_helper7
D;JGT
@SP
A=M-1
M=!M
(StackTest_helper7)
//push
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@32766
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
@StackTest_helper8
D;JGT
@SP
A=M-1
M=!M
(StackTest_helper8)
//push
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push
@53
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
//push
@112
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
@SP //neg group
A=M-1
M=-M
@SP //add group
M=M-1
A=M
D=M
@SP
A=M-1
M=D&M //and
//push
@82
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
M=D|M //or
@SP //neg group
A=M-1
M=!M
