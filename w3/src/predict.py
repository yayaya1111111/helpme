import argparse

parser = argparse.ArgumentParser(description="a program designed to predict future prices")


parser.add_argument('filename', help="Filename of data on the previous prices of a commodity")
arguments = parser.parse_args()
print(arguments)