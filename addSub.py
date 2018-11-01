#! /usr/bin/env python3

import sys

def main():
    if len(sys.argv) == 1:
        print('no arguments supplied. Exiting...')
        sys.exit()
    
    action = sys.argv[1]
    numbers = [int(i) for i in sys.argv[2:]]
    
    assert action in ['add', 'sub'], 'must have either "add" or "sub"'

    if len(numbers) == 0:
        print('no numbers detected!')
        sys.exit()
    else:
        process(action, numbers)


def process(action, numbers):
    if action == 'add':
        print(sum(numbers))
    elif action == 'sub':
        if len(numbers) < 2:
            print(numbers[0])
        else:
            print(numbers[0] - numbers[1])


if __name__ == '__main__':
    main()
