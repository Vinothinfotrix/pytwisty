# Overview

“pytwisty” package on PyPI (https://pypi.org/project/pytwisty/) is an extremely fast and efficient Python 3 implementation of a solver for a number of twisty puzzles including the 1x2x2, 1x2x3, and 2x2x2 Rubik's cubes. It works on a technique I developed called "Minimal Thinking" that, as the name suggests, minimizes the thought process behind solving a problem by effectively recognizing the type of the problem and using a predetermined result to jump straight to the solution. At each step of solving a puzzle, the solver recognizes the current arrangement and orientation of the individual pieces of the puzzle, and rearranges and reorients the pieces into the final state of the puzzle that the corresponding algorithm would have resulted in, had it been manually executed. This solver is faster than every other Rubik’s cube solver to date and is just one of the innumerable applications of the “Minimal Thinking” technique.

## Introduction

Modern speedcubers, or individuals who compete in speedcubing solve the Rubik’s cube quickly not by sheer intuition, but with memorized sequences of moves, called algorithms, which they deploy to solve the cube section by section. Knowing which algorithm to use when boils down to pattern recognition: Each algorithm corresponds to a different arrangement of coloured squares on the cube. When a speedcuber spots an arrangement they recognize, they perform the corresponding algorithm, bringing the cube one step closer to solved. Using these algorithms, the most fleet-fingered cubers in the world average between 50 and 60 moves per solve, which they can execute almost without thinking.

An important point to note is that the 3x3x3 Rubik’s cube is essentially a 2x2x2 Rubik’s cube without the edge and center pieces. Hence anybody who knows how to solve the 3x3x3 cube can also solve the 2x2x2 cube using the exact same algorithms, ignoring those algorithms which are related to permuting and orienting the edge pieces. In particular, solving the 2x2x2 Rubik’s cube is just like solving the corners pieces of the 3x3x3 cube and solving a 3x3x3 cube is exactly the same as solving a 2x2x2 cube but with an added complexity of solving the edge pieces. Similarly, solving the 4x4x4 cube is exactly the same as solving the 3x3x3 cube but with an added complexity of completing the centers and pairing up the edges at the beginning of the solve. In fact, especially after the 4x4x4 Rubik’s cube, this difference between the subsequent puzzles of the NxNxN category of twisty puzzles (puzzles like the Rubik's Cube which are manipulated by rotating a section of pieces) becomes more and more subtle. To a cuber, there is almost no difference between solving a 5x5x5, a 6x6x6 or a 7x7x7 Rubik’s cube because solving each one of them involves the general steps of completing the centers, pairing up the edges and then proceeding the complete the puzzle just like a 3x3x3 cube. This general pattern of an added complexity with increasing order of the puzzle can, in fact, be seen not only in the NxNxN puzzle category but in every category of twisty puzzles. For example, a 1x2x3 puzzle can be solved by first correctly positioning its corner pieces as if it were a 1x2x2 puzzle. After this, only a single algorithm is required to correctly orient the pieces in its middle layer, which is absent in a 1x2x2 puzzle.

## Common Rubik’s Cube Solvers and their Solving Methods

Rubik’s cube solving computer programs are pretty common and have been created by many using many different methods. The general approach of almost every one of these, however, is to use complex graph search algorithms to find an optimum solution that can solve the scrambled cube. Three of the most common and fastest Rubik’s cube solving methods are:

1) **Two-way Breadth-first Search method:** Rather than building up a single BFS tree from the scrambled state and searching until the solved state is found, two BFS trees are built - one from the scrambled state and one from the solved state.

2) **Korf’s Algorithm:** This algorithm is iterative-deepening-A* (IDA*), with a lower bound heuristic function based on large memory-based lookup tables, or “pattern databases”. These tables store the exact number of moves required to solve various subsets of the individual movable cubies.

3) **Kociemba's algorithm:** Kociemba’s algorithm identifies a subset of 20 billion positions. Phase one finds a move sequence that takes an arbitrary cube position to some position in the subset, and phase two finds a move sequence that takes this new position to the fully solved state.

## Statistical Analysis of Different Solvers

Since we have already established the similarity between Rubik’s cubes of subsequent orders of the form NxNxN, let us consider the case of a 2x2x2 Rubik’s cube for the sake of simplicity and a better understanding of concepts. The 3x3x3 and 2x2x2 cube solvers for each of the above-mentioned solvers are almost identical. In order to compare the speed and efficiency of all these solving methods, I ran the 2x2x2 version of each of the three algorithms on CPython on my PC and compared their mean solve times.  To all three I gave the same set of 10 random scrambles and the results are summarized below:

1) **Two-way Breadth-first Search method:**

Source Code: “rubiks_cube_bfs” solver by Mayank Rawat on GitHub (https://github.com/mayank18049/rubiks_cube_bfs)

Mean solve time: 0.5452627182006836 seconds per solve.

2) **Korf’s Algorithm:**

Source Code: “PocketCube” solver by Ivan Grudinin on GitHub (https://github.com/kuligram/PocketCube)

Mean solve time: 0.9749078100377863 seconds per solve

The program also took an additional 38.04953694343567 seconds on average to generate the pattern database heuristic before the very first solve.

3) **Kociemba's algorithm:**

Source Code: “Rubiks2x2x2-OptimalSolver” by Herbert Kociemba on GitHub (https://github.com/hkociemba/Rubiks2x2x2-OptimalSolver)

Mean solve time: 0.021625208854675292 seconds per solve 


This makes Kociemba’s Algorithm the fastest among the three. Kociemba’s Algorithm was in fact also used to calculate the solution in the robot that holds the current Guinness World Record for the fastest solve by a robot.

However, in comparison to the mean solve times of all the above-mentioned solvers, my 2x2x2 Rubik’s cube solver produced the following result: 

Mean solve time:  6.182333333413226e-05 seconds per solve

This solve time of the order -5 makes this solver 350 times faster than Kociemba’s algorithm! 

### Working Mechanism of My Solver

The conventional computerized Rubik’s cube solvers that look for an optimal solution from subsets of billions of positions of the cube using complex search techniques, although fast and close to optimal, are excessively memory-consuming as they generally require terabytes of pre-calculated lookup tables. Kociemba’s algorithm, for example, involves a subset of 20 billion positions every solve.

There have been numerous attempts to develop a solver using other efficient methods and techniques like Artificial Intelligence. The most notable of these is DeepCubeA, developed by a team of scientists at the University of California, Irvine, which uses a neural network and advanced machine learning techniques to solve the puzzle. However, with its three times slower speed and a longer average solution length, it is inferior to Kociemba’s algorithm in almost every aspect.

There is another category of Rubik’s cube solvers consisting of those that employ the so-called human approach to solve the puzzle. Unlike computers, humans cannot use large lookup tables or solve a scrambled cube quickly by sheer intuition. According to mathematicians, solving a Rubik’s cube is considered NP-complete, indicating that it is indeed extremely difficult to solve one mathematically. The human method thus involves the use of sets of memorized sequences of moves, called algorithms, which are deployed, in order, to solve the cube section by section. Each algorithm corresponds to a different arrangement of individual pieces on the cube. These algorithms are designed to transform only a small part of the cube without interfering with other parts that have already been solved so that they can be applied repeatedly to different parts of the cube until the whole is solved.

While this method generally produces solutions of about three times the length compared to those generated by a traditional dumb algorithm, people have largely been unsuccessful in creating a solver based on this approach that is anywhere close to Kociemba’s algorithm in speed. An example for the same is “rubik-cube” package by Paul Glass on PyPI (https://pypi.org/project/rubik-cube/) which uses the Beginner’s method and takes about 3 times the time taken by Kociemba's algorithm per solve on CPython.

However, my solver too uses the “human approach” to solve the puzzle. Specifically, it runs a combination of a slightly altered version of the layer-by-layer (LBL) method and the CFOP method (also known as the Fridrich method) of the 3x3x3 cube, which is heavily used and relied upon by most of the top speedcubers.

### Reason Behind the Unexpectedly High Speed and Efficiency of My Solver

One possible reason might be the way I stored and maintained the scrambled state cube throughout the program. Taking the example of the 2x2x2 Rubik’s cube, most solvers maintain an array of the colors on all the 24 colored stickers on the cube at all times. In contrast, I have maintained an array of only 8 elements. Without going much into the details, each of these 8 elements maintains the appropriate position and orientation of the corresponding pieces/cubies in the cube at all times during the solve. The logic behind this is that the 2x2x2 Rubik’s cube essentially consists of only 8 individual cubies which move about a common center. Each of those 8 pieces comprises 3 stickers that always remain together, no matter what. As a result, I effectively broke down the main problem of solving the entire collection of stickers into two subproblems namely, permuting the locations of the pieces and orienting them. This made my program comparatively easier to implement. However, this is not the main reason behind the extremely high speed and efficiency of my solver. The main reason is the use of the “Minimal Thinking” technique developed by me.

**Minimal Thinking technique:**
In simplest terms, this is a technique that minimizes the thought process behind solving a problem by effectively recognizing the type of the problem and using a predetermined result to jump straight to the solution.

The inspiration for this technique came from one of the most crucial principles of speedcubing, the fact that “each algorithm corresponds to a different arrangement of colored squares on the cube and that when a speedcuber spots an arrangement they recognize, they perform the corresponding algorithm, bringing the cube one step closer to solved.” And I successfully used this to create my solver. At each step of solving the puzzle, the solver recognizes the current arrangement and orientation of the individual pieces of the puzzle, and rearranges and reorients the pieces into the final state that the corresponding algorithm would have resulted in, had it been manually executed. This is just like how speedcubers, at each level of solving the Rubik’s cube, look at the arrangement of the cube and execute the corresponding algorithm, all without thinking. To better understand this concept, consider this simple math problem:

Calculate the numerical value of 9999^2 – 1^2.

Whenever someone sees this mathematical expression, the very first thing that will come to his mind is the identity a^2 – b^2 = (a + b) * (a – b). And without thinking further, he will immediately rewrite the expression as (9999 + 1) * (9999 – 1) which will give him 10000 * 9998 = 99980000 as the final answer.

However, someone unaware of this identity would either calculate and subtract the squares of 9999 and 1, or proceeded as follows:

9999^2 – 1^2

= 9999^2 – 1^2 + 9999 * 1 – 9999 * 1

= 9999 * (9999 + 1) – 1 * (9999 + 1)

= (9999 + 1) * (9999 – 1)

= 99980000

However, both of these methods are extremely time-consuming.

While solving a Rubik’s cube, each of the algorithms plays precisely the role the identity a^2 – b^2 = (a + b) * (a – b) plays in this math problem. What my solver does is that it first looks at the current arrangement of this cube at every stage and using a few conditional statements, it determines which algorithm is to be used (This is equivalent to us looking at the mathematical problem given in the example, recognizing that it is of the form a^2 – b^2 and thus concluding that the identity a^2 – b^2 = (a + b) * (a – b) is to be used). Now just like how we, without thinking anything, directly rearrange the given expression to the form (9999 + 1) * (9999 – 1), the solver also simply rearranges the cube pieces into the final arrangement that would have resulted had it actually followed each of the steps of the algorithm. It does not really execute that algorithm itself but simply adds the steps of that algorithm to the final solution.

In fact, the main reason why I employed the CFOP method in my solver is because of CFOP’s heavy reliance on algorithms, pattern recognition, and muscle memory, as opposed to more intuitive methods such as the Roux or Petrus methods. Therefore, it is also heavily used and relied upon by many speedcubers, including Max Park and Feliks Zemdegs.

## Applications

The Rubik’s cube solver is just one of the innumerable potential applications of the Minimal Thinking technique, which can be used to ease the computational part of a problem for a computer program by training it to use results that have already been established previously by human or artificial intelligence, and enabling it to jump directly to the solution without actually solving the entire problem. The result is a boost in the performance of the program both in terms of memory and speed.

However, an important point to note is that although Kociemba’s Algorithm is significantly slower than my solver, the fact that it almost always produces a solution that is much closer to the optimum solution than that produced by mine cannot be ignored. While the Fridrich method (the human method my solver is based on) produces solutions with a mean length of 50–60 moves, Kociemba’s algorithm produces one with a maximum of 29 moves and a minimum of 19. Therefore, the two solvers actually represent two different approaches to solving the same problem: whether we require a solution that is nearly the best and are willing to invest enough time and resources towards obtaining that solution, or are happy with a solution that may not be the shortest but is generated fairly quickly and at the cost of fewest possible resources, the choice is ours. With modern mechanical motors in Rubik's Cube solving robots that can execute each move in as less as 10 milliseconds, executing a handful of extra moves is an almost negligible task. In most real-life problems, an optimal solution may not always prove to be the best solution, especially when it is generated at the cost of an extremely slow and excessively memory-consuming program. Moreover, bringing down this move time of the motors to 5 milliseconds is a more achievable task in near future than developing faster and better search algorithms and reprogramming the other existing solvers to execute them.

Another significant takeaway from this particular solver is the fact that such a solver for a puzzle of a particular order can be built by adding on to the solvers of lower orders of the same category of puzzles, without having to start from scratch. This is precisely how I had built my solver for the 1x2x3 Rubik’s puzzle from my 1x2x2 puzzle solver by adding a few extra lines of code that correctly orient the middle layer pieces which are absent from a 1x2x2 puzzle.

### Featured:

https://prakharkuwait.medium.com/unintelligent-rubiks-cube-solvers-the-final-leap-bd5133f78505

https://www.geeksforgeeks.org/pytwisty-rubiks-cube-solver-python-project/

# Installation and Usage

Run the following to install the package:

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
