import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np

def main():
    descStr="""
    이 프로그램은 아이튠즈의 재생목록 파일을 분석한다
    """
    parser=argparse.ArgumentParser(description=descStr)
    group=parser.add_mutually_exclusive_group()

    group.add_argument('--common', nargs='*', dest='plFiles', required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup', dest='plFileD', required=False)

    args=parser.parse_args()
    if args.plFiles:
        #common tracks을 발견했을 때,
        findCommonTracks(args.plFiles)
    elif args.plFile:
        #plot stats
        plotStats(args.plFile)
    elif args.plFileD:
        #중복된 트랙을 발견했을 때,
        findDuplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for")

if __name__ == '__main__':
    main()
