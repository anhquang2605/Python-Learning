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

## Broadcasting
- applied operate of every element on the array with another value
- arr * 10 will multiply every element of arr by 10
- can also perfom with another array as long as they are compatible (when the dimensions of both arrays are equal or when one of them is 1)
- numpy random number operator
- rng = np.random.default_rng()
- When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimension and works its way left. Two dimensions are compatible when **they are equal, or one of them is 1.**
- example of arrays with mismatched
- A      (1d array):  3
B      (1d array):  4 # trailing dimensions do not match

A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched