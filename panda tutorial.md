# PANDAS
## what kind of data?
- **Data frame** is the main data type
- similar to spread sheet or SQL table
- 2 d data structure (with column and rows)
- **Series**: a column in data frame
- to select a column, use the [] with the column title in it
- can do sth with the df or the column by using the dot notation on it
- ex: df.describe() //basic static desciption of the data frame, df.max() get max, df.['col1'].min() get min of the column
- import data frame from a csv file: filedata = pd.read_csv("file path")
- to see first N rows of the file: filedata.head(N)
- to see last N rows: filedata.tail(N)
- to see datatypes of each series based on pandas: filedata.dtypes
- can read and write excel sheets, but need excel reader
- df.info() technical information like the data type, number of rows, columns
- To select multiple columns, use a list of column names within the selection brackets []
- .shape: return number of rows and column of the selected section of df in a form of tuple (r,l)
- can select specific rows like numby filtering for array
- df[df['age'] >= 35]
- isin([a,b,c....,n]) check if rows is in the specified values in the list
- notna(). return rows with value that is known (not na)
- can also filter by using conditional operator 
- df[df['col1'] sth | df['col1'] sth]
- select a specific rows with specific columns
- df.loc[df[row] condition, df[col] condition]: this is used if interested in the rows or col titles
- df.iloc[a:b, c:d]: this is used if intersred in the index position of rows or cols: interested in from row a+1 to b and cols c+1 to d
- when selecting with loc or iloc, new values can be filled in based on the selection
- when write to csv, use index=False option to remove the index from the table
### New col from exisisting col
- df['new_col'] = df['old_col'] opertators (+,-,*,/,>,<,==) Values. Will perform the operation element wise with each value. Can use apply() for more sophisticated use

### rename cols 
- df_renamed = df.rename( columns = {"old_col1": "new_col1", "old_col2" : "new_col2"})
- can be used for cols and rows titles
- can also use functions instead of string to rename
ex: air_quality_renamed = air_quality_renamed.rename(columns=str.lower) // rename from upper case to lower case