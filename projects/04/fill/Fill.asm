// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// This program illustrates low-level handling of the screen and keyboard
// devices, as follows.
//
// The program runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// 
// Assumptions:
// Your program may blacken and clear the screen's pixels in any spatial/visual
// Order, as long as pressing a key continuously for long enough results in a
// fully blackened screen, and not pressing any key for long enough results in a
// fully cleared screen.
//
// Test Scripts:
// For completeness of testing, test the Fill program both interactively and
// automatically.
// 
// The supplied FillAutomatic.tst script, along with the supplied compare file
// FillAutomatic.cmp, are designed to test the Fill program automatically, as 
// described by the test script documentation.
//
// The supplied Fill.tst script, which comes with no compare file, is designed
// to do two things:
// - Load the Fill.hack program
// - Remind you to select 'no animation', and then test the program
//   interactively by pressing and releasing some keyboard keys

// keyboard register 24576

//----- CONSTANTS ------
@512
D=A
@NUM_ROWS
M=D
@32
D=A
@NUM_COLUMNS
M=D
@16384
D=A
@ST_SCREEN_IND
M=D
@24576
D=A
@KEYBOARD_IND
M=D
//----------------------


(MAINLOOP)
//sets useful variables - ROW_NUM,COL_NUM ---
@ROW_NUM
M=0
@COL_NUM
M=0
//-------------------------------------------


// ---- if key is pressed go to BLACK ----
@KEYBOARD_IND
A=M
D=M

@BLACK
D;JNE

@WHITE
D;JEQ
//------------------------------------------





(BLACK)
// gets exact register to change ------------
@ROW_NUM
D=M
@COL_NUM
D=D+M
@ST_SCREEN_IND
D=D+M
//------------------------------------------

// changes pixel to black
A=D
M=-1


//raises COL_NUM,ROW_NUM -------------------
@COL_NUM
//M=M+1
D=M

@NUM_COLUMNS
D=D-M 

//a condition to raise the ROW_NUM
@INC_ROW_B
D;JEQ
//-------------------------------------------


(INC_ROW_B)
@ROW_NUM
M=M+1

//a condition to finish the loop
D=M
@NUM_ROWS
D=D-M
@MAINLOOP
D;JEQ
@BLACK
0,JMP


(WHITE)
// gets exact register to change ------------
@ROW_NUM
D=M
@COL_NUM
D=D+M
@ST_SCREEN_IND
D=D+M
//------------------------------------------

// changes pixel to black
A=D
M=-1


//raises COL_NUM,ROW_NUM -------------------
@COL_NUM
//M=M+1
D=M

@NUM_COLUMNS
D=D-M 

//a condition to raise the ROW_NUM
@INC_ROW_W
D;JEQ
//-------------------------------------------


(INC_ROW_W)
@ROW_NUM
M=M+1

//a condition to finish the loop
D=M
@NUM_ROWS
D=D-M
@MAINLOOP
D;JEQ
@WHITE
0,JMP






