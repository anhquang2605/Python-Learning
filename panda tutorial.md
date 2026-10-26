# PANDAS
## what kind of data?
- **Data frame** is the main data type
- similar to spread sheet or SQL table
- 2 d data structure (with column and rows)
- **Series**: a column in data frame
- to select a column, use the [] with the column title in it
- can do sth with the df or the column by using the dot notation on it
- ex: df.describe() //basic static desciption of the data frame, df.max() get max, df.['col1'].min() get min of the column
- import data frame from a csv file: pd.read_csv("file path")