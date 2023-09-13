def ComputeList(list):
    return sum(list)

def ProductList(list):
    if len(list) == 0:
            return 0
    total = 1
    for i in range(len(list)):
        total = total * list[i]
    return total

def main():
    x = input("Please enter a list of integers seperated by a space ")
    y = x.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i])
    print(y)
    print("The sum of the list is: " + str(ComputeList(y)))
    print("The product of the list is: " + str(ProductList(y)))

if __name__ == "__main__":
    main()