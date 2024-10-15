// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.


(START) //main loop
@SCREEN //init counter to SCREEN
D=A;
@R0 
M=D;

@KBD //select a color value based on the value in KBD
D=M;
@PRESSED
D;JNE

(NOTPRESSED)
@R0 //restart if finished
D=M;
@KBD
D=D-A;
@START
D;JGE

@R0
D=M;
A=D;
M=0;

@R0 //increment and loop
M=M+1;
@NOTPRESSED
0;JMP

(PRESSED)
@R0 //restart if finished
D=M;
@KBD
D=D-A;
@START
D;JGE

@R0
D=M;
A=D;
M=-1;

@R0 //increment and loop
M=M+1;
@PRESSED
0;JMP