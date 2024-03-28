import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="name", required=True)
parser.add_argument("--age", help="age", required=True)
parser.add_argument("--city", help="city")

choice = input("enter choice- ")

args = parser.parse_args()
name, city = args
print(name + " " + city + " " + choice)
