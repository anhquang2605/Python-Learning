# Starting Matplotlib
- .show(): show the plot, some application like jupyter note book skip this call, plot are automatically shown
![alt text](image.png)
- scatter():
- plot():
- bar():
- size of figure: To change the figure size in Matplotlib, specify the figsize parameter as a tuple of (width, height) in inches. The default size is 6.4 by 4.8 inche

# ploting the df
- we can call the .plot(kind=plottype) method directly on to the df object. we need to specify the name of the plot type as a string
- histogram, to know the distribution of range of value
- bins is number of intervals in between, the more bins the more details the distributions
- four kind of distribution: 
    1. Normal distribution: mass at the center
    2. left skewer: the distribution lean to ward the left
    3. right skewer
    4. uniformity: distributed evenly across
- scatter: explore relation ship between two number: does salary increase with year of experiece?
- df.plot(kind='scatter', x='col1', y='col2')
- correlation: allow measure strength and direction of the linear relationship between two values. scatter plot can do this visually
- Correlation efficiency
![alt text](image-1.png)
