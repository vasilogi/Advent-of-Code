# import 3rd party packages
import pandas as pd

# read CSV as dataframe
df = pd.read_csv('input.csv',sep=' ',names=['direction','amount'])

# sum the forward, up, and down values separately
forward = df[ df['direction'] == 'forward' ].amount.sum()
up = df[ df['direction'] == 'up' ].amount.sum()
down = df[ df['direction'] == 'down' ].amount.sum()

# calculate the depth based on the up and down directions given from the problem statement
# down adds depth and up reduces it
depth = down - up

# What do you get if you multiply your final horizontal position by your final depth?
sol = depth*forward

print('Depth x Horizontal Position = ', sol)