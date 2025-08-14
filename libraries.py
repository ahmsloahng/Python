import itertools

'''Nested for loop for unknown times'''
def nest_loop(range_list):
    '''Input : rangelist - a list containing how much to iterate each time.
    length of range_list will give how many times nested for loop will run'''
    iterables = [range(r) for r in range_list]
    for com in itertools.product(*iterables):
        print (com)

