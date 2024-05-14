import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    new_list = family[start:end:1]
    size_y = len(family)
    size_x = len(family[0])

    new_size_y = len(new_list)
    new_size_x = len(new_list[0])
    print("My shape is : (",size_y,",",size_x,")")
    #your code here
    print("My new shape is : (",new_size_y,",",new_size_x,")")

    return family[start:end:1]

# def main():
#     Lst = [50, 70, 30, 20, 90, 10, 50]
 
#     print(Lst[-6:-2:1])

# if __name__ == "__main__":
#     main()