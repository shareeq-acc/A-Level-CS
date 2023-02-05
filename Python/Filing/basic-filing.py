import os


def inputFilename():
    fileName = input("Please Enter File Name \n")
    filePath = (f"{os.getcwd()}\Filing\Files\{fileName}.txt")
    return filePath


def readFile():
    try:
        filePath = inputFilename()
        f = open(filePath, "r")
        print(f.read())
        f.close()
    except:
        print("Error Occured")


def appendFile():
    try:
        filePath = inputFilename()
        file = open(filePath, "a")
        records = int(input("Please Enter Number of Records to be Entered \n"))
        for i in range(i, records):
            data = input("Enter Record", i + 1, "\n")
            file.write(data)
            file.write('\n')
        file.close()
    except:
        print("Error Occured")
    return


def deleteFile():
    try:
        filePath = inputFilename()
        os.remove(filePath)

    except:
        print("Error Occured")


def editFile():
    try:
        filePath = inputFilename()
        fileLine = int(input("Enter File Line to be Edited \n"))
        data = input("Enter The Updated Data \n")
        f = open(filePath, "r")
        fileData = f.readlines()
        fileData[fileLine - 1] = data + '\n'
        f.close()
        os.remove(filePath)
        newFile = open(filePath, "w")
        newFile.writelines(fileData)
        newFile.close()

    except:
        print("Error Occured")

    return


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
