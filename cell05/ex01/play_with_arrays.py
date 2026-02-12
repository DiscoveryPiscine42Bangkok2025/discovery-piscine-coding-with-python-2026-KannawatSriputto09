"""ex01"""
def main():
    """main"""
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    print("Original array:", array)
    newarray = []
    for i in array:
        newarray.append(i+2)
    print("New array:", newarray)
main()