# import packages
import pandas as pd
import os

# user-defined functions
def positive_edge(a,b):
    # this function returns true if there is positive edge
    # and false otherwise
    #
    # a,b: numerical values
    if a > b:
        return True
    else:
        return False

def count_edges(l):
    # this function returns the number of positive edges
    # of a list
    # 
    # l: list
    counter = 0
    # loop over the list
    for i in range(1,len(l)):
        # count for positive edge
        if positive_edge(l[i],l[i-1]):
            counter += 1
    return counter

# read data
# get current working directory
CWD = os.getcwd()
# define the filepath of input
input_file = 'input.csv'
input_file = os.path.join(CWD,input_file)
# read csv as data-frame
df = pd.read_csv(input_file, engine='c', header=None, names=['depth'])
# get depth to a list
depth = df['depth'].to_list()

# part A

print('Part A: there are ' + str(count_edges(depth)) + ' measurements that are larger than the previous measurement')

# part B

# sliding window
window_size = 3
N = len(depth) - 1 # the last index of the depth array

# get the first 3 elements in an array
triplet = depth[0:window_size]
# calculate the sum of the first triplet and add it into an array
triplet_sums = [sum(triplet)]

# loop over the depth measures
for i in range(1,len(depth)):
    # "Stop when there aren't enough measurements left to create a new three-measurement sum"
    if ((N - i) >= 2):
        # stack the triplets vertically
        triplet = depth[i:i+window_size]
        triplet_sums.append(sum(triplet))

print('Part B: there are ' + str(count_edges(triplet_sums)) + ' measurements that are larger than the previous measurement')