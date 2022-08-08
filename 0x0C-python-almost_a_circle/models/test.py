#!/usr/bin/python3
#!/usr/bin/python3
""" 3-main """
from rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(2, 2, 2, 2, 3)
    print(r1)
    r1.update(89, 10)
    print(r1)
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)
    r1.update(45)
    print(r1)
    r1.update(width=1, x=2)
    print(r1)
    print()
    r1.update(y=1, width=2, x=3, id=89)
    print(r1)
    print()
    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
