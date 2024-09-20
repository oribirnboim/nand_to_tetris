// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// The program should swap between the max. and min. elements of an array.
// Assumptions:
// - The array's start address is stored in R14, and R15 contains its length
// - Each array value x is between -16384 < x < 16384
// - The address in R14 is at least >= 2048
// - R14 + R15 <= 16383
//
// Requirements:
// - Changing R14, R15 is not allowed.

// Put your code here.

// sets min and max variables --------
@-16383
D=A
@MIN
M=D

@INDMIN
M=0


@16383
D=A
@MAX
M=D

@INDMAX
M=0
//------------------------------------

// sets i variable which runs along the array
@R14
D=M

@I
M=D
D=A

@ARRi
M=D

(LOOP)
//checks arr[i]<=min ----------
@MIN
D=M

@ARRi
D=D-M

@SWAPMIN
D;JGE
(RETURN_SWAPMIN)

//checks arr[i]>=max ----------
@MAX
D=M

@ARRi
D=D-M

@SWAPMAX
D;JLE
(RETURN_SWAPMAX)

// changes i
@I
M=M+1
D=M

@ARRi
M=D

//loop stop condition
@I
D=M

@R15
D=D-M

@R14
D=D-M

@LOOP
D;JLE

// swaps min and max
@MAX
D=M

@INDMIN
A=M
M=D

@MIN
D=M

@INDMAX
A=M
M=D

(SWAPMIN)
@ARRi
D=M

@MIN
M=D

@I
D=M

@INDMIN
M=D

@RETURN_SWAPMIN
0;JMP


(SWAPMAX)
@ARRi
D=M

@MAX
M=D

@I
D=M

@INDMAX
M=D

@RETURN_SWAPMAX
0;JMP
