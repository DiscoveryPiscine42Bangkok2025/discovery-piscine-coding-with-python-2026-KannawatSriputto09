import sys
"""ex13"""
def main():
    """main"""
    if len(sys.argv) > 1:
        for text in sys.argv:
            if not text.endswith("ism"):
                print(text + "ism")
    else:
        print("none")
main()