# %% Open the CodeSpace in your local VS Code
# What is your terminal display "path"?
# /workspaces/daytwostuff

# %% Create a virtual environment
# Should you include the environment in your repo or not? 
# No, you should not include the virtual environment in your repo. 

# Now, What is your terminal display "path"? Is it different?
# /workspaces/daytwostuff
# The terminal path is not different.

# %% Viewing data
import pandas as pd 
df = pd.read_csv('tip.csv')
df.head()

# %% Extension Management 
# What do you notice about the extension menu?
# It shows me all the extensions I have installed locally and in the Codespace.

# Review the capabilities, what are three useful elements of Data Wrangler?
# The Data Wrangler extension automatically calculates the basic statistics (mean, median, standard deviation, etc.). It also showcases if there are any missing values in the dataset and visualizes the numerical variables. 

# %% Package Managing 
# Plotly version: 6.5.1
# Why do we use a requirements.txt file?
# It shows us all the package versions that were used when running this project, and allows others to do so as well on their own machines when cloning/forking the project. 
# %%
