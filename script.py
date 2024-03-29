import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="name", required=True)
parser.add_argument("--age", help="age", required=True)
parser.add_argument("--city", help="city")

args = parser.parse_args()

if args.age == '15':
    choice = input("enter choice- ")

name, city = args
print(name + " " + city + " " + choice)
