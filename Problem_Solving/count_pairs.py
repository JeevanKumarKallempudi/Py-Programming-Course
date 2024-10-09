"""
Count Pairs
Given a dictionary dic, count the pairs where the sum of keys and their respective values are equal.

Sample Case
Input: {5:5, 8:9, 8:7, 1:2, 10:0, 7:8}
Output: 2
Explanation:
There are 2 pairs, where the sum of keys and their values are equal :
1. 5:5  and 10:0 , as 5+5 = 10+0 = 10
2. 8:7 and 7:8, as 8+7=7+8 = 15
"""

import sys

# Parse the input lists from command-line arguments
keys = [int(k) for k in sys.argv[1].split()]
values = [int(v) for v in sys.argv[2].split()]

# Create the dictionary
dic = {}
for k, v in zip(keys, values):
    dic[k] = v
    
# Function to count pairs with equal sum of key and value
def count_pairs_with_equal_sum(dic):
    # Create a dictionary to store sums of key-value pairs
    sum_dict = {}
    
    # Loop through the dictionary and calculate the sum of each key-value pair
    for key, value in dic.items():
        pair_sum = key + value
        if pair_sum in sum_dict:
            sum_dict[pair_sum] += 1
        else:
            sum_dict[pair_sum] = 1
    
    # Count pairs where there are at least two sums with the same value
    pair_count = 0
    for count in sum_dict.values():
        if count >= 2:
            pair_count += count // 2  # Each pair contributes 1 to the count
    
    return pair_count

# Get the result
result = count_pairs_with_equal_sum(dic)

# Print the result
print(result)
