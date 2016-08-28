import argparse

ap = argparse.ArgumentParser()
ap.add_argument("echo", help = "repeats the string")
ap.add_argument("-v", "--verbose", help = "increase verbosity", action = "store_true")
args = ap.parse_args()
if args.verbose:
    print("verbosity turned on")

