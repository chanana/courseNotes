#! /usr/bin/env python3
'''
calculates 'n choose k' for n > 0 and 0 <= k <= n
optional boolean arguement 'log' can be true for returning the
natural logarithm of 'n choose k'
'''
import math
import argparse
import sys

# if no arguments provided, exit
if not len(sys.argv) > 1:
    print('No arguments detected!\nPlease use \
            -n <number> or --help for more details')
    sys.exit()

# instantiate Class ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('-n',
                    #required=True,
                    type=int,
                    help='total number of items to choose from')
parser.add_argument('-k',
                    type=int,
                    help='number of items to choose',
                    default=0)
parser.add_argument("-l", "--log", 
                    action="store_true", 
                    help="returns the log binomial coefficient")
parser.add_argument("--test",
                    action="store_true",
                    help="tests the module and quits")
args = parser.parse_args()

def logfactorial(n, k=0):
    '''Calculates log(n!/k!)
    n, k should be integers
    k is optional
    
    >>> logfactorial(1)
    0.0

    >>> round(logfactorial(2),3)
    0.693

    >>> round(logfactorial(2, 1),3)
    0.693

    >>> round(logfactorial(3, 2),4)
    1.0986

    >>> logfactorial(5, 5)
    0.0

    >>> round(logfactorial(5, 4),1)
    1.6

    >>> logfactorial(5, 6)
    0.0
    '''
    # Assertions
    assert n >= 0, 'n cannot be negative'
    assert k >= 0, 'k cannot be negative'
    assert type(n)==int, 'n must be an integer'
    assert type(k)==int, 'k must be an integer'
    
    if k > n:
        return 0.

    # ln(n!/k!) = ln(n) + ln(n-1) + ... + ln(k+2) + ln(k+1)
    total = 0.
    for i in range(k+1, n+1):
        total += math.log(i)

    return total


def choose(n, k, log=False):
    '''Calculates log(choose(n, k)) for any integers
    n > 0 and 0 <= k <= n
    
    >>> choose(5, 3, True) == logfactorial(5, 3) - logfactorial(5 - 3)
    True

    >>> choose(5, 3)
    10

    >>> choose(5, 5)
    1

    >>> choose(5, 5, True)
    0.0
    '''
    # reuse code i.e. use the function defined above
    logChoose = logfactorial(n, k) - logfactorial(n - k)

    if log:
        return logChoose
    else:
        return round(math.exp(logChoose)) # returns whole number


if __name__=='__main__':
    if args.test:
        print("testing the module...")
        import doctest
        doctest.testmod()
        print("done with tests.")
    else:
        answer = choose(args.n, args.k, log=args.log)
        print(answer)
