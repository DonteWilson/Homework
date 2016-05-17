ADGP120
========================================================================================

Steps on how to Run program.

1.Visit www.github.com
2.Go to the search menu and search for DonteWilson
3.Visit Repositories and Click on Homework
4. Then go to 2nd Semester and find a folder labeled ADGP120.
5. This folder holds all data dealing with ADGP120. Files being used are the runit, Tester.py, and Image.py
=========================================================================================
Description of Project
This project is meant to demonstrate the A star algorithm. A* is used for pathfinding and graphing traversal.
In this project I set a start and goal point. The program will find and all nodes parent to its location and draw a line
to show the connection.

Each of these steps are broken down into functions inside my project.

Steps to A*
1.Add Start Node To Open
2.Get Lowest F
3.Set New Current Node
4. Get Adjacents 
5. Remove the current node from the open list and add it to the the closed list.
6. If in open, compare the g scores. If not in open list, then add to open list
7. If g score is less set the parent
8. If the parent is goal go back to finding the lowest F score
9. If goal is open retrace the path.


=========================================================================================
How does it work? 

The program has a grid that is 10 by 10 and it displays links to the parent nodes. The pink lines represent the surrounding nodes. The green represents the open nodes.

If you reopen the program it gives you another start to goal path demonstration. It generates a random start and end position
that will display the path on the screen to the user. The start goal is light blue and the goal is dark brownish color. There
is a grey line that runs from the start node to the goal node.