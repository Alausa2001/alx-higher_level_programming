#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) > 4:
        print(f"Usage: ./100-my_calculator.py {sys.argv[1]} {sys.argv[2]}\
 {sys.argv[3]}")
        exit(1)
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}

    if sys.argv[2] in op_dict.keys():
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = op_dict[sys.argv[2]]
        result = op(a, b)
        print(f"{a} {sys.argv[2]} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
