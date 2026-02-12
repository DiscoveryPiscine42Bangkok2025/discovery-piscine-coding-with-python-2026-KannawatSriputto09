import sys
"""ex10"""
def main():
    """main"""
    if len(sys.argv) != 2:
        print("none")
    else:
        user_input = input("What was the parameter? ")

        if user_input == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")
main()