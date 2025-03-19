#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Follow-the-gap is a geometric obstacle avoidance algorithm that"
        " will move toward goal point considering the largest gap."
    )
    parser.add_argument("-i", "--input", default=Path("input.yaml"), type=Path)
    parser.add_argument("-o", "--output", default=Path("output.yaml"), type=Path)
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    sys.exit(main())
