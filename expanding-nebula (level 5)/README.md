## How this works:

1. The input matrix gets converted into a tuple of tuples to allow for hashing operations
2. The program creates a dictionary, where each key is a combination possible for the current (iteration) row, and the corresponding value is the amount of valid occurances.
3. The program iterates over each row to find each possible row given any of the previous rows, and stores the amount of valid occurances in the dictionary (most row combinations will have 0 valid occurances, depending on how the given matrix looks like)

### Time complexity
This program has a  time complexity of O(count_row<sup>2</sup> * 2<sup>count_column</sup>) (worst case), O(count_row * 2<sup>count_column</sup>) (best case), as the rows and columns are swapped. It is possible to vastly reduce the complexity (to O(count_column<sup>2</sup> * count_row<sup>2</sup>)) by not looking at all possible combinations per row, but instead per cell / 2 cells, depending on how many adjacent cells are precalculated.

If there is interest in this possible faster solution, let me know. I already know how to program it, but this solution sufficed for the constraints given in the task and was much simpler. The faster solution would allow you to calculate preimages for much bigger sizes of grids (for instance 50⨯50 would not be possible with the current solution).
