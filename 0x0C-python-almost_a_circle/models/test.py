#!/usr/bin/python3
""" 15-main """
from rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle()
    r2 = Rectangle()
    Rectangle.save_to_file([r1, r2])
    with open("Rectangle.json", "r") as file:
        print(file.read())

