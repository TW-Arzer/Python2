import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--number", help="Un nombre entier", required=True, type=int)
    parser.add_argument("-e", "--exponent", help="Un exposant", type=int, default=1)

    args = parser.parse_args()

    print(args.number ** args.exponent)
