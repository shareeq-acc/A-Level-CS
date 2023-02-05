def linearSearch(arr, type= 'str'):
    maxIndex = len(arr) - 1
    searchValue = input("Please Enter Value to be Searched \n")
    i = 0
    found = False

    # Convert Search Value to Integer if type is 'int' 
    if type == "int":
        searchValue = int(searchValue)

    # Loop until Value Not Found or All Elments are checked
    while found == False and i <= maxIndex:
        if arr[i] == searchValue:
            found = True
        i = i+1

    if found:
        print(f"Your Input Value {searchValue} is Found at Index Postion {i-1}")
    else:
        print(f"Your Input Value {searchValue} does Not Exists")


# testData = ['alpha', 'beta', 'gamma']
testData = [21, 5, 41, 18, 54, 13]
linearSearch(testData, 'int')
