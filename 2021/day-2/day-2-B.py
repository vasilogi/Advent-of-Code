# import 3rd party packages
import pandas as pd

# read CSV as dataframe
df = pd.read_csv('input.csv',sep=' ',names=['direction','amount'])

# initialize depth, aim, and, horizontal
depth = 0
aim = 0
horizontal = 0
# loop over the dataframe rows
for index, row in df.iterrows():
    # get the raw into a dictionary, e.g. {'direction': 'forward', 'amount': 2}
    rowDict = row.to_dict()
    # implement the algorithm stated by the day-2 problem
    if 'forward' in rowDict.values():
        horizontal += rowDict['amount']
        depth += aim * rowDict['amount']
    elif 'up' in rowDict.values():
        aim -= rowDict['amount']
    elif 'down' in rowDict.values():
        aim += rowDict['amount']

sol = depth * horizontal
print('Depth x Horizontal Position = ', sol)