import sys


def main():
    print("Hello World! From Python: " + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        # script will fail for python 3.6 #
        raise Exception("Python version 3.6.x is unsupported!")


if __name__ == "__main__":
    main()
