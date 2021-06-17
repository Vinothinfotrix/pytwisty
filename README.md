# Overview

This is an extremely fast and efficient Python 3 implementation of a solver for 1x2x2, 1x2x3, and 2x2x2 Rubik's cube puzzles.
It works on a technique developed by me called "Minimal Thinking" that, as the name suggests, minimises the thought process behind solving any problem by recognising the type of problem and using a predetermined result to jump straight to the solution.
At each step of solving a puzzle, the solver recognises the current arrangement and orientation of the individual pieces of the puzzle, and rearranges and reorients the pieces into the final state of the puzzle that the corresponding algorithm would have resulted in, had it been manually executed.

## Installation

Run the following to install:

```python
pip install pytwisty
```

https://pypi.org/project/pytwisty/

## solve122

1x2x2 solver. Requires two parameters, namely a 6 character long string representing the colour alignment of the solved cube, and an 8 character long string based on the first letters of the colors of each sticker on the scrambled puzzle.
The order for noting the colour alignment must be front face, left face, right face, top face, bottom face and back face. While noting the colour alignment or the scramble string, the user can hold the cube in any way but with a 2*2 face facing him.
In order to obtain the scramble string, the user must start with the the stickers on the upper face with the one on the left coming first followed by the one on the right.
Next he must go layer by layer from top to bottom and enter 2 stickers for each of the 2 layers.
For each layer, the first and the second stickers must be ones on the front face towards the left and right side.
Last are the ones on the bottom face, with the one on the left coming first followed by the one on the right.
Stickers on the remaining 3 faces must be ignored.
For example, let the colour alighnment of the puzzle be OGBYWR. Here W corresponds to white, O corresponds to orange, G corresponds to green, R corresponds to red, B corresponds to blue, and Y corresponds to yellow. This means that if this puzzled is already solved, the string entered would be YYOOOOWW.
The output will be a series of steps that will lead to a solved state of the puzzle. Each step would be of the form R or U each of which represent a 180 degree turn of the right face and the upper layer respectively.

```python
>>> import pytwisty
>>> colors='OGBYWR'
>>> scramble='WYORORWY'
>>> pytwisty.solve122(colors,scramble)
['U', 'R']
```

## solve123

1x2x3 solver. Requires two parameters, namely a 6 character long string representing the colour alignment of the solved puzzle, and a 16 character long string based on the first letters of the colors of each sticker on the scrambled puzzle.
The order for noting the colour alignment must be front face, left face, right face, top face, bottom face and back face. While noting the colour alignment or the scramble string, the user can hold the cube in any way but with a 2*3 side facing him in such a way that the front face has 3 rows and 2 columns.
In order to obtain the scramble string, the user must start with the the stickers on the top face with the one on the left coming first followed by the one on the right.
Next he must go layer by layer from top to bottom and enter 4 stickers for each of the 3 layers.
For each layer, the first sticker will be the one of the left face, the second and the third stickers must be ones on the left and right side of the front face respectively, and the fourth will be the one on the right face.
Last are the ones on the bottom face, with the one on the left coming first followed by the one on the right.
Stickers on the back face must be ignored.
For example, let the colour alighnment of the puzzle be OGBYWR. Here W corresponds to white, O corresponds to orange, G corresponds to green, R corresponds to red, B corresponds to blue, and Y corresponds to yellow. This means that if this puzzled is already solved, the string entered would be YYGOOBGOOBGOOBWW.
The output will be a series of steps that will lead to a solved state of the puzzle. Each step would be of the form U, D, R, L or M each of which represent a 180 degree turn of the upper layer, bottom layer, right face, left face and the middle layer respectively.

```python
>>> import pytwisty
>>> colors='OGBYWR'
>>> scramble='WYBOOBGORBGRRGYW'
>>> pytwisty.solve123(colors,scramble)
['U', 'D', 'R', 'U']
```

## solve222

2x2x2 Rubik's Cube solver. Requires a single parameter, namely, a 24 character long string representing the scrambled state of the cube based on the first letters of the colors of each sticker.
In order to obtain the scramble string, the user may hold the cube in any way.
The first four stickers will be the ones on the front side, staring with the one on the top left and going around clockwise.
Next are the ones on the left side, starting with the one on top in the back and going around clockwise.
Next are the ones on the right side, starting with the one in the front on the top and going around clockwise.
Next are the ones on the top side of the cube, starting with the one in the back left and going around clockwise.
Next are the ones on the bottom side, starting with the one in the front left and going around clockwise.
Last are the ones on the back side, starting with the one on the top right (keep in mind that you are still holding the cube the same way as before) and going around clockwise (based on the perspective you would have if you were facing the back side rather than the front side).
The output will be a list of steps in the form of the official WCA notation that will lead to a solved state of the cube.

```python
>>> import pytwisty
>>> scramble='BWRRWWYGOYYWGBGOBBGRORYO'
>>> pytwisty.solve222(scramble)
["L'", "B'", 'L', 'F2', 'B', "L'", "B'", 'L', "F'", 'B', "L'", "B'", 'L', "F'", 'y2', 'F2', "L'", 'F', 'R', "F'", 'L', 'F', "R'", "F'"]
```
