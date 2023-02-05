def binary_search(arr):
    lowerbound = 0
    upperbound = (len(arr) - 1)
    validInput = False
    found = False

    # Repeatedly Prompt for Input if Not Provided Valid Input
    while not validInput:
        searchValue = input("Please Enter Value to be Searched \n")
        # Check if Search Value Entered is Digit
        if searchValue.isdigit():
            validInput = True
            # Convert str int Value to integer
            searchValue = int(searchValue)

    # Loop until either Value is Found or Upper Bound is less than Lower Bound, that means the value does Not Exists
    while found == False and upperbound >= lowerbound:
        # Find Middle Index to compare it to the Input Value Given
        middleValue = int((lowerbound + upperbound) / 2)
        print("Middle Value is ", middleValue)

        if arr[middleValue] > searchValue:
            # If Given Value is Greator than provided Search value, 
            # that mean that the value exist between the lower bound and middle value
            # Adjust the Upper Bound to the middle value (-1 because middle value is already compared)
            upperbound = middleValue - 1
        elif arr[middleValue] < searchValue:
            # If Given Value is Less than provided Search value, 
            # that mean that the value exist between the middle value and Upper bound
            # Adjust the Lower Bound to the middle value (+1 because middle value is already compared)
            lowerbound = middleValue + 1
        else:
            found = True
            print(f"Found {searchValue}, Position: {middleValue}")

        if not found:
            print(
                f"Lower Bound is {lowerbound} \nUpper Bound is {upperbound} \n")

    # If Input Value is Not found
    if not found:
        print(f"Your Searched Value {searchValue} does Not Exist")


testData = [2, 19, 24, 32, 51, 64, 76]
binary_search(testData)
