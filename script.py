import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--api-key", help="tenant API key", required=True)
parser.add_argument(
    "--stage",
    help="tenant stage (latest/test/beta/prod/parvati)",
    choices=["latest", "test", "beta", "prod", "parvati"],
    required=True,
)
parser.add_argument(
    "--dry-run", help="execute script in dry run mode", action="store_true"
)
parser.add_argument(
    "--blocks", help="delete blocks in the specific tenant", action="store_true"
)
parser.add_argument(
    "--exclude-blocks",
    nargs="+",
    help="list of blocks which should be excluded from deletion",
    default=[],
)
parser.add_argument(
    "--deployments",
    help="delete deployments in the specific tenant",
    action="store_true",
)
parser.add_argument(
    "--exclude-deployments",
    nargs="+",
    help="list of deployments which should be excluded from deletion",
    default=[],
)


args = parser.parse_args()

print(args)
