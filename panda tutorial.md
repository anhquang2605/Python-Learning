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

### counting values
_ df.value_counts(): list value and their ocurrence


### sort values
DataFrame.sort_values(by, *, axis=0, ascending=True, inplace=<no_default>, kind='quicksort', na_position='last', ignore_index=False, key=None)
* by str or list of str
Name or list of names to sort by.

if axis is 0 or ‘index’ then by may contain index levels and/or column labels.

if axis is 1 or ‘columns’ then by may contain column levels and/or index labels.

* axis“{0 or ‘index’, 1 or ‘columns’}”, default 0
Axis to be sorted.

* ascending bool or list of bool, default True
Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the by.

### remove duplicate rows
- df.drop_duplicates(): will return new data frame with on the first occurence of the row

### add new col
- insert(index position, "col_name", [colvalues,...])
- df['new_col'] = [newvalues,...]
- adding new cols with new values based on the condtion of the old colummn
- np.where(condition, "value if true", "value if false")
- or prefill the cols with one values, then use loc with condition to replace the value to meet the condition
df['pay_rate_type'] = 'Other'
df.loc[df['salary'] > 140000, 'pay_rate_type'] = 'High'

### Clean and organize data
- isna(): detect missing values
- dropna(): remove missing values
- fillna(): filling missing values
- groupby():
- agg():
- merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=<no_default>, indicator=False, validate=None):Merge DataFrame or named Series objects with a database-style join.

how{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’, ‘left_anti’, ‘right_anti},
default ‘inner’ Type of merge to be performed.

left: use only keys from left frame, similar to a SQL left outer join; preserve key order.

right: use only keys from right frame, similar to a SQL right outer join; preserve key order.

outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.

inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.

cross: creates the cartesian product from both frames, preserves the order of the left keys.

left_anti: use only keys from left frame that are not in right frame, similar to SQL left anti join; preserve key order.

right_anti: use only keys from right frame that are not in left frame, similar to SQL right anti join; preserve key order.

onHashable or a sequence of the previous
Column or index level names to join on. These must be found in both DataFrames. If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.

left_onHashable or a sequence of the previous, or array-like
Column or index level names to join on in the left DataFrame. Can also be an array or list of arrays of the length of the left DataFrame. These arrays are treated as if they are columns.

right_onHashable or a sequence of the previous, or array-like
Column or index level names to join on in the right DataFrame. Can also be an array or list of arrays of the length of the right DataFrame. These arrays are treated as if they are columns.
