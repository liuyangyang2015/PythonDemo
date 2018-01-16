# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:
#         print("B")
#
#     except C:
#         print("C")
#
#     except D:
#         print("D")

import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# for arg in sys.argv[1:]:
for i in range(6):
    try:
        arg="test1.py"
        f = open(arg, 'r')
    except OSError as ex:
        print('cannot open', ex.__str__())
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()