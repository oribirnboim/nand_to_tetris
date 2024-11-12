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


(START)
@R14 //copy addresses to other variables
D=M
@addr
M=D
@R15
D=M
@array_counter
M=D

@R14 // init min and max variables
A=M
D=M
@min
M=D
@max
M=D

@R14 // init min and max addresses
D=M
@min_addr
M=D
@max_addr
M=D

(LOOP) //go over the array, find min, max, and their addresses
@addr
A=M
D=M
@min
D=D-M
@NOT_LESS
D;JGE // if value is less than min:
@addr
D=M
@min_addr // save address
M=D
@addr
A=M
D=M
@min // save value
M=D
(NOT_LESS)

@addr
A=M
D=M
@max
D=D-M
@NOT_MORE
D;JLT // if value is more than max:
@addr
D=M
@max_addr // save address
M=D
@addr
A=M
D=M
@max // save value
M=D
(NOT_MORE)

@array_counter //loop utilities:
M=M-1 //reduce counter
@addr
M=M+1 //increase address
@array_counter
D=M
@LOOP
D;JGT //repeat loop if needed


@min //do the swap
D=M
@max_addr
A=M
M=D
@max
D=M
@min_addr
A=M
M=D


(END)
@END
0;JMP