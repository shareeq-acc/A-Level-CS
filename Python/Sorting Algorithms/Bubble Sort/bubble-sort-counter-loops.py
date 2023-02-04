# Bubble Sort using 2 Counter Loops

# Test Data
arr = [23, 18, 49, 5, 55, 53, 81, 19]

def bubbleSort(arr):
    arrLength = len(arr)
    swapped = False

    # Loop through Elements
    for i in range(arrLength - 1):

        # Decreasing the Loop Range Value for Optimization
        for j in range(0, arrLength-i-1):

            # Swap if Current Element is Greator than previous one
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

    return arr


print("Sorting Using 2 Counter Loops.... \n", bubbleSort(arr))
