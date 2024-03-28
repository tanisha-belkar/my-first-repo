import sys

args = sys.argv

if not args[1]:
    print("No name!!")
    sys.exit()
print("Hello {}".format(args[1]))