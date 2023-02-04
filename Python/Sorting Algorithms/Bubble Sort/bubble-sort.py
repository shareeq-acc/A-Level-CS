# Bubble Sort Using a count-controlled and pre-conditional Loop

# Test Data
arr = [23, 18, 49, 5, 55, 53, 81, 19]


def bubbleSort(arr):
    swapped = True
    maxSize = len(arr)

    # Loop If Swapped is True -> After Every Iterations Swapped is Set to True if Elements are Swapped
    while (swapped):
        swapped = False
        for i in range(maxSize - 1):

            # Swap if Current Element is Greator than previous one
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        # Decrement Max Size since the Last i Elements are Sorted
        # e.g After 3 Iterations Last 3 Are Already Sorted
        maxSize = maxSize - 1

    return arr  # Return the Sorted Array


# Bubble Sort with Specified Order
def bubbleSortWithOrder(arr):
    swapped = True
    maxSize = len(arr)

    sortingOrder = input(
        "Please Enter Sorting Order \n asc for Ascending \n desc for Descending \n ")
    order = sortingOrder.lower()

    if order != 'asc' and order != 'desc':
        return "Please Specify Correct Order"

    # Loop If Swapped is True -> After Every Iterations Swapped is Set to True if Elements are Swapped
    while (swapped):
        swapped = False
        for i in range(maxSize - 1):

            if order == 'asc':
            # Swap if Current Element is Greator than previous one
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True

            else:
            # Swap if Current Element is Less than previous one
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True

        # Decrement Max Size since the Last i Elements are Sorted
        # e.g After 3 Iterations Last 3 Are Already Sorted
        maxSize = maxSize - 1

    return arr  # Return the Sorted Array


print("Sorting Using a count-controlled and pre-conditional Loop.... \n", bubbleSort(arr))
print("Sorting Array in Given Order.... \n", bubbleSortWithOrder(arr))
