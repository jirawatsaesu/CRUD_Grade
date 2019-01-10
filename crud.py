import csv


def read_csvfile(filename):
    ''' Read data from csv file and put it to list. '''
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    csvfile.close()
    return data


def write_csvfile(filename, mode, data):
    ''' Write data from list to csvfile. '''
    with open(filename, mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
    csvfile.close()


def string_cleanup(string):
    ''' Remove circle bracket, comma and space from string. '''
    string = string.strip('()').replace("'", '').replace(' ', '')
    return string


while True:
    command = input('>')
    if command.startswith('INSERT INTO'):
        # INSERT INTO Grade.csv VALUES ('1', '1', 'Data', '3', 'B+')
        command = command.split(' VALUES ')
        table = command[0].split(' ')[2]                        # Grade.csv
        value = [string_cleanup(command[1]).split(',')]         # [['1', '1', 'Data', '3', 'B+']]

        write_csvfile(table, 'a', value)
    elif command.startswith('UPDATE'):
        # UPDATE Grade.csv SET Grade='A' WHERE Subject='Data'
        command = command.split()
        table = command[1]                                      # Grade.csv
        where_attr = command[5].split('=')[0]                   # Subject
        where_value = string_cleanup(command[5].split('=')[1])  # Data
        set_attr = command[3].split('=')[0]                     # Grade
        set_value = string_cleanup(command[3].split('=')[1])    # A

        # Read data
        data = read_csvfile(table)
        attributes = data[0]
        attr_to_change = attributes.index(set_attr)
        attr_to_find = attributes.index(where_attr)

        # Find attribute
        for row in range(len(data)):
            if where_value == data[row][attr_to_find]:
                data[row][attr_to_change] = set_value
                break

        write_csvfile(table, 'w', data)
    else:
        break