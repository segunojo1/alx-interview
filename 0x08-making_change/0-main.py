#!/usr/bin/python3
"""
Main file for testing makeChange function.
"""

makeChange = __import__('0-making_change').makeChange

if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 5
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
