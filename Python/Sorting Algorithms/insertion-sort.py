# Insertion Sort
def insertionSort(arr):
    arrLength = len(arr)

    # First element in the array is Assumed to be sorted
    for i in range(1, arrLength):
        currElement = arr[i]

        j = i-1  # Previous Element Index

        # Loop Until Current Element is Less than the previos Element
        while j >= 0 and currElement < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1    # Decrement to Compare it with the next previous Index

        arr[j + 1] = currElement

    return arr


# Insetion Sort Using Order
def insertionSortWithOrder(arr):
    arrLength = len(arr)

    sortingOrder = input(
        "Please Enter Sorting Order \n asc for Ascending \n desc for Descending \n ")
    order = sortingOrder.lower()

    if order != 'asc' and order != 'desc':
        return "Please Specify Correct Order"

    # First element in the array is Assumed to be sorted
    for i in range(1, arrLength):
        currElement = arr[i]

        j = i-1  # Previous Element Index

        if order == 'asc':
            # Loop Until Current Element is Less than the previous Element
            while j >= 0 and currElement < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1    # Decrement to Compare it with the next previous Index

        else:
            # Loop Until Current Element is Greator than the previous Element
            while j >= 0 and currElement > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1    # Decrement to Compare it with the next previous Index

        arr[j + 1] = currElement

    return arr


test_data = [7, 10, 3, 13, 21, 15]

# print(insertionSort(test_data))
print(insertionSortWithOrder(test_data))
