"""ex02"""
def main():
    array = [1,2,3,4,55,66,77]
    print("Original array:", array)
    new_arr = []
    for i in array:
        if i >= 5:
            new_arr.append(i + 2)
    print("New array:", new_arr)
main()