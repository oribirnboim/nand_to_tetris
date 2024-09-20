// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// Multiplies R0 and R1 and stores the result in R2.
//
// Assumptions:
// - R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.
// - You can assume that you will only receive arguments that satisfy:
//   R0 >= 0, R1 >= 0, and R0*R1 < 32768.
// - Your program does not need to test these conditions.
//
// Requirements:
// - Your program should not change the values stored in R0 and R1.
// - You can implement any multiplication algorithm you want.

// Put your code here.

@0
D=A

@R2
M=D // R2=0

@i
M=D // i = 0

@R1
D=M

@R1NEG
D;JLT

@R1ZERO
D;JEQ

@R1POS
D;JGT

(R1POS) /////////////////
@R0
D=M // D=RAM[1]

@R2
M=M+D // M=M+RAM[1]

@i
M=M+1 // i++
D=M // D=i

@R1
D=D-M

@R1POS
D;JLT //jump if i<r1

@END
0,JEQ

(R1ZERO) //////////////////
@END
0;JEQ

(R1NEG) //////////////////
@R0
D=M // D=RAM[1]

@R2
M=M+D // M=M+RAM[1]

@i
M=M-1 // i++
D=M // D=i

@R1
D=D+M

@R1POS
D;JGT //jump if i>r1

@R2
M=-M // flips sign

@END
0,JEQ



(END)
@END
0;JEQ