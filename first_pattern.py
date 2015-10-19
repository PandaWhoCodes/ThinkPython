"""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

"""


def pattern():
    for x in range(0, 11):
        if (x == 0 or x == 5 or x == 10):
            print("+ - - - - + - - - - +")
        else:
            print("|         |         |")


pattern()
