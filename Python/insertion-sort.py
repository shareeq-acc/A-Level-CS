def insertionSort(sortArray):
    arrayLength = len(sortArray)  # Array Length
    sortIndex = 0     # Index of the Value that Needs to be Sorted
    for index in range(1, arrayLength):
        valueToSort = sortArray[index]
        sortIndex = index
        while valueToSort < sortArray[sortIndex - 1] and sortIndex > 0:
            sortArray[sortIndex] = sortArray[sortIndex - 1]
            sortArray[sortIndex - 1] = valueToSort
            sortIndex -= 1
    return sortArray


print(insertionSort([7, 10, 3, 13, 2, 0]))
