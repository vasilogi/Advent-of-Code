import numpy as np

# import expenses file into a numpy array
expenses = np.fromfile('expense_report.csv', dtype=np.intc, sep='\n')

# self-explanatory
exitFlag = False
for i in range(0, len(expenses)):
    for j in range(i+1, len(expenses)):
        if (expenses[i] + expenses[j] == 2020):
            print('Entry #1 :', expenses[i], 'Entry #2 :', expenses[j])
            print('product :', expenses[i]*expenses[j])
            exitFlag = True
            break
    if exitFlag:
        break
