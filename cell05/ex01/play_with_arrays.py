"""ex01"""
def main():
    """main"""
    array = [1,2,3,4,55,66,77]
    print("Original array:", array)
    newarray = []
    for i in array:
        newarray.append(i+2)
    print("New array:", newarray)
main()