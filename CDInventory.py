#------------------------------------------# 
# Title: CDInventory.py
# Desc: CD Inventory
# Change Log: (Who, When, What)
# DRodriguez, 2022-02-28, Created File
#------------------------------------------#

# -- DATA -- #

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PROCESSING -- #

# Get user Input
print('Write or Read file data.')
while True:
    print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')
    print('[d] display data\n[v] view existing data\n[x] to delete\n[exit] to quit')
    strChoice = input('a, w, r, d, v, x, or exit: ').lower()  # convert choice to lower case at time of input
    print('\n\n')

    if strChoice == 'exit':
        break
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to list in memory
       strCD_Title = input('Please enter CD Title: ')
       strCD_Artist = input('Please enter Artist Name: ')
       dicRow = {'CD Title': strCD_Title, 'Artist': strCD_Artist}
       lstTbl.append(dicRow)  
    elif strChoice == 'w':
        if len(lstTbl) != 0:
            # List to File
            objF = open(strFileName, 'a')
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objF.write(strRow)
            objF.close()
            lstTbl.clear()
            print('Saved to file.\n')
        else:
            print('No data available.\n')
    elif strChoice == 'r':
        # File to print
        lstTbl.clear()
        objF = open(strFileName, 'r')
        for row in objF:
            lstRow = row.strip().split(',')
            dicRow = {'CD Title': lstRow[0], 'Artist': lstRow[1]}
            lstTbl.append(dicRow)
        objF.close()
        print('Artist, Title')
        for row in lstTbl:
            print(row)
    elif strChoice == 'd':
        # Display data
        print('Artist, Title')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'v':
        # Load existing data
        objF = open(strFileName, 'r')
        print(objF.read())
        input('Press enter to continue.')
    elif strChoice == 'x':
        # Delete an entry
        objF = open(strFileName, 'r')
        temp = []
        for row in objF:
            temp.append(row)
        objF.close()
        if len(temp) != 0:
            objF = open(strFileName, 'w')
            temp = temp[:-1]
            for row in temp:
                objF.write(row)
        else:
            print('No data to delete.\n')
        objF.close()
    else:
        print('Please choose either a, w, r, d, v, or exit!')
