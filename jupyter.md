# Jupyter a notebook like excel. 
- Before starting, make sure to enter the v env using this command
& "$HOME\jupyter-env\Scripts\Activate.ps1"
- file extension **.ipynb**
- to start a note book server: jupyter notebook
- to open a specific notebook: jupyter notebook notebookname.ipynb
- An open notebook has exactly one interactive session connected to a kernel,
- three types of cells: raw cells (no evaluated), markdown cell (evaluated as rich text like mark down document), and code cell (where code can run)
- The most important keyboard shortcuts are Enter, which enters edit mode, and Esc, which enters command mode.
- Alt-Enter runs the current cell and inserts a new one below.
- Ctrl-Enter run the current cell and enters command mode.
- code run in a separated kernel, kernel can be interupted or shutdown
- In a Jupyter Notebook, variables carry over between lines and cells automatically because they share the same interactive Python kernel (session)
- for markdown, can have line code (kept in between a pair of $) or displayed in new line
- Expressions on their own line are surrounded by \begin{equation} and \end{equation}:
    \begin{equation}
    e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i
    \end{equation}
GitHub flavored markdown
The Notebook webapp supports Github flavored markdown meaning that you can use triple backticks for code blocks:

```python
print "Hello World"
```

```javascript
console.log("Hello World")
```
Gives:

print "Hello World"
console.log("Hello World")
And a table like this:

| This | is   |
|------|------|
|   a  | table|
A nice HTML Table:

# Steps to inspect the notebook
To inspect the output or state of each step in a Jupyter Notebook, you can use several methods depending on whether you want to alter cell execution, use a visual debugger, or inspect interactive variables.

1. Enable Global Interactivity (Print All Lines)

By default, Jupyter only outputs the result of the very last line in a cell. To force Jupyter to automatically output the result of every single line/step in a cell without typing print() everywhere, execute this command at the top of your notebook: [1] (https://www.youtube.com/watch?v=894Py3V0wZM), [2] (https://www.youtube.com/watch?v=bqw5-8f-cEI)
python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
Use code with caution.

2. Use the Built-in Visual Debugger

If you are using JupyterLab (version 3+), there is a built-in visual debugger that allows you to set breakpoints and step through code line by line. [1] (https://jupyterlab.readthedocs.io/en/latest/user/debugger.html)
1. Activate the Debugger: Click the bug icon 🪲 in the upper-right corner of the notebook to turn debugging on. [1] (https://jupyterlab.readthedocs.io/en/stable/user/debugger.html), [2] (https://jupyterlab.readthedocs.io/en/latest/user/debugger.html)
2. Set Breakpoints: Click in the margin (gutter) next to the line numbers of your code cell to drop a red dot breakpoint. [1] (https://jupyterlab.readthedocs.io/en/latest/user/debugger.html)
3. Run the Cell: Execute the cell (Shift + Enter). The execution will pause at your breakpoint. [1] (https://www.codecademy.com/article/getting-started-with-jupyter), [2] (https://jupyterlab.readthedocs.io/en/latest/user/debugger.html)
4. Inspect State: Use the Variables panel in the right-hand debugger sidebar to view the exact data, shapes, and values at that specific step. You can step over, step into, or continue using the control buttons. [1] (https://medium.com/@heshanottawa/variable-inspector-in-jupyter-notebook-or-jupyterlab-mac-os-5639f12bbfb), [2] (https://jupyterlab.readthedocs.io/en/latest/user/debugger.html)

3. Use Notebook Magics (%debug)

If your code throws an error or you want a quick interactive terminal at a specific step without a GUI:
• Post-Mortem Debugging: If a cell crashes, create a new cell immediately below it, type %debug, and run it. This opens the interactive Python Debugger (pdb) at the exact point of failure. [1] (https://www.youtube.com/watch?v=rSPyvPw0p9k&t=5), [2] (https://www.codecademy.com/article/getting-started-with-jupyter)
• Step Commands: Type p <variable_name> to print a value, n to step to the next line, or q to exit. [1] (https://www.cambridge.org/core/resources/pythonforscientists/jupyterdb/), [2] (https://www.youtube.com/watch?v=rSPyvPw0p9k&t=5)

4. Code Structuring: One Operation Per Cell

The most robust approach for data exploration is structural. Instead of writing a massive block of operations in one cell, break your code down so that each cell performs only one main operation and ends by outputting the variable. [1] (https://www.linkedin.com/pulse/five-step-process-data-exploration-jupyternotebook-ted-petrou)
For example:
• Cell 1: df = pd.read_csv('data.csv') followed by df.head()
• Cell 2: df_filtered = df[df['age'] > 30] followed by df_filtered.head() [1] (https://www.linkedin.com/pulse/five-step-process-data-exploration-jupyternotebook-ted-petrou)
This allows you to visually track changes across the entire notebook workflow without needing extensions or debuggers. [1] (https://www.eosc.cz/en/news-and-events/news/jupyter-notebooks-vol-1), [2] (https://www.linkedin.com/pulse/five-step-process-data-exploration-jupyternotebook-ted-petrou)
If you are looking for a specific type of inspection, let me know:
• Are you looking to track Pandas DataFrames step-by-step?
• Do you want to see inline variable values as you type?
• Are you using standard Jupyter Notebook, JupyterLab, or VS Code?
I can provide the exact extension or shortcut tailored to your specific setup!
