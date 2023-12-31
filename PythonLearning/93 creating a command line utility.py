# Python is command line utility.
# If we create our command line utility, we can easily read from anothor software.
# we can create out command line utility using python:

import argparse  # helps in making command line utility.
import sys  # whatever with argparse, sys helps to write it in console.


def Calc(args):
    if args.o == 'add':
        return args.x + args.y

    if args.o == 'null':
        return args.x * args.y

    if args.o == 'sub':
        return args.x - args.y

    if args.o == 'div':
        return args.x / args.y

    return "Something went wrong!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # ArgumentParser() is a class.

    parser.add_argument('--x', type=float, default=1.0,
                        help="Please contact Aditya")  # to add argument.

    parser = argparse.ArgumentParser()  # ArgumentParser() is a class.

    parser.add_argument('--y', type=float, default=3.0,
                        help="Please contact Aditya")  # to add argument.

    parser = argparse.ArgumentParser()  # ArgumentParser() is a class.

    parser.add_argument('--o', type=str, default="add",  # --o means what operation you want.
                        help="Please contact Aditya")  # to add argument.

    args = parser.parse_args()

    sys.stdout.write(str(Calc(args)))  # sys.stdout.write: print on console whatever return will come.
