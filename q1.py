#!/usr/bin/env python3

import argparse
import sys

if __name__ == "__main__":
    # process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--column", type=int, help="column number to monitor", required=True)
    parser.add_argument("--max_count", type=int, help="maximum number of times limit can be exceeded", required=True)
    parser.add_argument("--max_value", type=int, help="maximum value column can reach", required=True)
    args = parser.parse_args()
    
    #print("col: {}".format(args.column))
    #print("count: {}".format(args.max_count))
    #print("val: {}".format(args.max_value))
    
    # remove non data lines from input stream
    line = input()
    line = input()
    
    times_limit_exceeded = 0
    
    # process every subsequent line
    while times_limit_exceeded <= args.max_count:
        line = input()
        #print(line)
        
        # split line into columns
        cols = [int(x) for x in line.split()]
        print(cols)
        
        current_value = None
        try:
            current_value = cols[args.column]
        except IndexError:
            print("Column out of range")
            sys.exit()
            
        if current_value > args.max_value:
            times_limit_exceeded += 1
    
    print("Column {0} exceeded {1} more than {2} times".format(args.column, args.max_value, args.max_count))
        
