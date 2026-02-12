"""ex03"""
def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    print(array)
    new_arr = []
    for i in array:
        if i >= 5:
            new_arr.append(i + 2)
    print(set(new_arr))
main()