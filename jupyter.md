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