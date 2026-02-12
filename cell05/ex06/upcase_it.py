import sys
"""ex06"""
def main():
    """main"""
    if len(sys.argv) > 1:
        print(sys.argv[1].upper())
    else:
        print("none")
main()