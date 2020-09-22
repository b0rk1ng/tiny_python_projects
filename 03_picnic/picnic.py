#!/usr/bin/env python3
"""
Author : smash <smash@localhost>
Date   : 2020-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('foods',
                        metavar='str',
                        nargs='+',
                        help='item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    foods = args.foods

    if args.sorted:
        foods.sort()

    if len(foods) == 1:
        print(f"You are bringing {foods[0]}.")

    elif len(foods) == 2:
        print(f"You are bringing {foods[0]} and {foods[1]}.")

    else:
        print(f"You are bringing {', '.join(foods[:-1])}, and {foods[-1]}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
