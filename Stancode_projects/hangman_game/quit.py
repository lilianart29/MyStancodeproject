
import random
"""
File: count_runs.py
———————————————————————————————————
This program simulates a certain number of die-roll results and calculates
how many consecutive number (defined as runs) appears.
"""
# This constant controls the number of rolls
NUM_ROLLS = 15


def main( ):
    old_a =''
    run = 0
    for i in range(NUM_ROLLS):
        a = random.randrange(1, 7)
        print('Rolls: '+str(a))
        if old_a == a:
            run += 1
        else:
            old_a = a

    print('Number of runs:'+str(run))



    #####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()