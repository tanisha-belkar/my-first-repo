import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--api-key", help="name", required=True)
parser.add_argument("--stage", help="age", required=True)
parser.add_argument("--dry-run", help="city")

parser.add_argument("--blocks", help="city")
parser.add_argument("--exclude-blocks", help="city")

parser.add_argument("--deployments", help="city")
parser.add_argument("--exclude-deployments", help="city")

args = parser.parse_args()
choice = 'n'
if args.age != '15':
    choice = input("enter choice- ")
print(args)
