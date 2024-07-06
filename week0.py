# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
import math
def dose(needs):
    total = sum(needs)
    if total >= 500:
        return "No medicine given"
    ##

    treatment = []
    for need in needs:
        if(need >250):
            return "No medicine given"
        round_up = math.ceil(need/10) * 10
        vitamins = round_up /10
        injections = round_up - need
        treatment.append((math.ceil(vitamins), injections))
    
    return treatment





    #YOUR SOLUTION ENDS HERE

