#!/usr/bin/env python3
"""
Author: Matthew Ashman <matthewiashman@gmail.com>
Purpose: say hello
"""

import argparse


def get_args():
    """Get the arguments to commands"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Greet someone or everyone"""
    print("Hello, {}!".format(get_args().name))


if __name__ == '__main__':
    main()
