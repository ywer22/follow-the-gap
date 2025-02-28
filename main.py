#!/usr/bin/env python3
import argparse


def main():
    print("IGVC")
    parser = argparse.ArgumentParser(description = "processing input and output file")
    parser.add_argument('-i','--input' )
    parser.add_argument('-o','--output' )
    args = parser.parse_args()
    print(args)



if __name__ == "__main__":
    main()