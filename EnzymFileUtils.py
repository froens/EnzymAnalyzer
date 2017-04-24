import csv

def loaddata(file_name, max_rows = -1):
    """
    Pre-processing
    Reading file into a list
    """

    # Open file handle from data.csv
    file = open(file_name)

    # Read first line of the file
    # The first line contains information about the types in each column
    typeStr = file.readline()
    types = typeStr.rstrip().split(';')

    # Read second line of the file
    # The second line contains the header information for each column
    headerStr = file.readline()
    headerNames = headerStr.rstrip().split(';')

    # List for collecting row data, once they've been processed
    collectionList = list()

    # Iterate through each row in the file
    row_num = 0
    for row in file:
        if 0 <= max_rows <= row_num:
            break

        # Split the row into columns
        columns = row.rstrip().split(";")

        # Initialize new dictionary to contain column values
        dictionary = dict()

        # For 0 to length of columns (number of columns)
        # For each column, create new entry in the dictionary with the name of the header
        # Insert converted value
        for column_i, valueStr in enumerate(columns):

            # Convert data type to the one described in the corresponding column in the first row
            if types[column_i] == "str":
                dictionary[headerNames[column_i]] = valueStr
            if types[column_i] == "float":
                valueStr = valueStr.replace(",", ".")
                dictionary[headerNames[column_i]] = float(valueStr)

        # Add collection to the list
        collectionList.append(dictionary)
        row_num = row_num + 1

    # Close file handle, so other programs are able to use it
    file.close()

    return collectionList


def load_targets(file_name):
    with open(file_name) as csvfile:

        reader = csv.DictReader(csvfile, delimiter=';', lineterminator='\n',)
        lst = []
        for r in reader:
            lst.append(r)

        return {k: float(v.replace(',', '.')) for k, v in lst[0].items()}


def write_to_csv(data):
    fieldnames = sorted([key for key in data[0]])
    with open('transpose.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        writer.writerows(data)






