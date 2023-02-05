import os

def inputFilename():
    # Input Filename
    fileName = input("Please Enter File Name \n")
    # Absolute Directory
    filePath = (f"{os.getcwd()}\Filing\Files\{fileName}.txt")
    return filePath


def readFile():
    try:
        filePath = inputFilename()
        # Open file in Read Mode
        f = open(filePath, "r")
        # Print File Content
        print(f.read())
        f.close()
    except:
        print("Error Occured")


def appendFile():
    try:
        filePath = inputFilename()
        # Open File in Append Mode
        file = open(filePath, "a")
        # Enter number pf Records to be Added
        records = int(input("Please Enter Number of Records to be Entered \n"))

        for i in range(i, records):
            data = input("Enter Record", i + 1, "\n")
            # Write Data to File
            file.write(data)
            # Add a new Line
            file.write('\n')
        file.close()
    except:
        print("Error Occured")
    return


def editFile():
    try:
        filePath = inputFilename()
        # File Line that needs to be updated
        fileLine = int(input("Enter File Line to be Edited \n"))
        # New Data that will replace the previous line data
        data = input("Enter The Updated Data \n")
        # Open File and Read All the Lines, File data will be Stored in a List(Array)
        # Each Line is an Element in the List(Array) e.g [line1Data, line2Data]
        f = open(filePath, "r")
        fileData = f.readlines()
        # Replace Element in the list that correspond to the Line and add a New Line Character
        fileData[fileLine - 1] = data + '\n'
        f.close()
        # Remove the Exisiting File
        os.remove(filePath)
        # Create New File with same Name
        newFile = open(filePath, "w")
        # Write the new Data as Lines in the File
        newFile.writelines(fileData)
        newFile.close()

    except:
        print("Error Occured")

    return


def deleteFile():
    try:
        filePath = inputFilename()
        os.remove(filePath)

    except:
        print("Error Occured")


def basicFiling():
    selectedOption = ''

    while selectedOption != '5':
        selectedOption = input(
            "Welcome.. Please Enter: \n 1 for Reading a File \n 2 For Writing in a File \n 3 For Editing an Existing File \n 4 For Deleting an Existing File \n 5 For Exit \n")

        if selectedOption == '1':
            readFile()

        elif selectedOption == '2':
            appendFile()

        elif selectedOption == '3':
            editFile()

        elif selectedOption == '4':
            deleteFile()

        elif selectedOption == '5':
            break

        else:
            print("Wrong Input")


basicFiling()
