def ComputeList(list):
    return sum(list)

def ProductList(list):
    if len(list) == 0:
            return 0
    total = 1
    for i in range(len(list)):
        total = total * list[i]
    return total

def ReverseList(list):
    rev = list
    rev.reverse()
    return rev

def main():
    x = input("Please enter a list of integers seperated by a space: ")
    z = x.split(" ")
    for i in range(len(z)):
        z[i] = int(z[i])
    print(z)
    print("The sum of the list is: " + str(ComputeList(z)))
    print("The product of the list is: " + str(ProductList(z)))

    #This change was made in branch part10

if __name__ == "__main__":
    main()