# Numby learning
- powerful arrays in Python. also comes with good amount of functions to manipute the arrays
- **n**array is the core of this library. Once it is created, it has fixed size, so when you change the size, it will be deleted and a new array will be created
- why it is fast? 
- numpy: new array with np.array()
- shape: (a:b) where a is number of col and b is number of row. if only one dimesion then a, or be is omitted
- dimension: 2d array 1d 3d etc.
- size: number of elements
- reshape(a,b): take a array, turn them in to 1d then reshape them into a rows, b columns
- ndim for number of dimesions
- np.zeros(), np.ones(), np.empty(), np.arange(n) create a array from 0 to n-1, np.linspace(a,b, num) a: start, b: end,  num: interval must be using the keyword argument
- np.sort(), np.concaternate(array1, array2, axis), axis can be 0 which put array in a 2 d array instead of merging them into 1d
- can conditionally select element from array with arr[condition]
- ex: con = (arr <=5)
- print(arr[con])
- arr[:2]
-  tuple(dim // 2 for dim in arr.shape) center coordinates of a 2 d array with rows == col the dim // 2 is floor division, round to floor

## Basic array operations
- between arr1, and arr2, can +, -, /, *. Will match each element from the one array to another
- in an array, can also operate(sum) by axis 0 for top to bottom (x axis or axis of rows) 1 for left to right (y axis, axis of cols)
- axis 0: operate down the row from top to bottom
- axis 1: operate from left to right, about the col
## Broadcasting
- applied operate of every element on the array with another value
- arr * 10 will multiply every element of arr by 10
- can also perfom with another array as long as they are compatible (when the dimensions of both arrays are equal or when one of them is 1)
- numpy random number operator
- rng = np.random.default_rng()
- can have a lower bound (inclusive) and higher bound (exclusive) in the rng.integers(low = a, high = b, size=(,))
- When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimension and works its way left. Two dimensions are compatible when **they are equal, or one of them is 1.**. To determine whether two arrays can be broadcast together, compare their shapes from right to lef
- example of arrays with mismatched
- A      (1d array):  3
B      (1d array):  4 # trailing dimensions do not match

A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
- When one shape has fewer dimensions, NumPy treats it as if it had extra dimensions of size 1 on the left.

For example:
A: (5, 3, 5)
B:    (3, 5)

B is treated as: (1, 3, 5)

-When working with NumPy arrays:
1. Write down their shapes.
2. Add dimensions of size 1 to the left of the shorter shape until the shapes have the same number of dimensions.
3. Compare from right to left.
4. Each pair must be equal or contain a 1.
5. The result uses the larger size from each compatible pair.

In NumPy, the @ operator performs matrix multiplication. It is different from *, which performs element-by-element multiplication.
1. Basic example
import numpy as npA = np.array([[1, 2],              [3, 4]])B = np.array([[5, 6],              [7, 8]])print(A @ B)



Output:
[[19 22]
 [43 50]]


2. How does it calculate the result?
Matrix multiplication takes a row from A and a column from B, multiplies corresponding elements, and adds them together.



A
2
1
3
4
0
2



×
B
5
2
1
4
3
7



=
AB
20292622









\(\left(AB\right)_{11}=(2\cdot 5)+(1\cdot 1)+(3\cdot 3)=20\)

Row
12




Column
12










Give feedback

For our example, the result is calculated like this:
First row, first column
\[
1\times5+2\times7=19
\]

First row, second column
\[
1\times6+2\times8=22
\]

Second row, first column
\[
3\times5+4\times7=43
\]

Second row, second column
\[
3\times6+4\times8=50
\]


Putting those four results together gives the matrix:
\[
\begin{bmatrix}
19 & 22\\
43 & 50
\end{bmatrix}
\]

3. Difference between @ and *
Using the same arrays:
print(A @ B)  # Matrix multiplicationprint(A * B)  # Element-wise multiplication



The results are different:
A @ B:
[[19 22]
 [43 50]]

A * B:
[[ 5 12]
 [21 32]]


For A * B, NumPy simply multiplies each element at the same position: \(1\times5\), \(2\times6\), and so on.
4. Matrix dimensions must match
For matrix multiplication, the number of columns in the first matrix must equal the number of rows in the second matrix.

For example:
A = np.ones((2, 3))  # 2 rows, 3 columnsB = np.ones((3, 4))  # 3 rows, 4 columnsC = A @ Bprint(C.shape)  # (2, 4)



2 × 3
Matrix A

×
3 × 4
Matrix B


The inner dimensions must match: 3 = 3.

2 × 4
Result shape: (2, 4)


The general rule is:
\[
(m\times n)@(n\times p)=(m\times p)
\]

If the inner dimensions don't match, NumPy raises a ValueError.

Remember: @ means matrix multiplication; * means element-wise multiplication.