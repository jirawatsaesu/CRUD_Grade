import csv
import math


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
    ''' Remove circle bracket, quote and space from string. '''
    string = string.strip('()').replace("'", '').replace(' ', '')
    return string


while True:
    command = input('>')
    if command.startswith('GPA'):
        # GPA Grade.csv 1 1
        command = command.split()
        table = command[1]          # Grade.csv
        year = command[2]           # 1
        semester = command[3]       # 1

        data = read_csvfile(table)
        select_data = [row for row in data if row[0] == year and row[1] == semester]
        credit = [int(row[-2]) for row in select_data]
        grade = []
        for row in select_data:
            if row[-1] == 'A':
                grade.append(4)
            elif row[-1] == 'B+':
                grade.append(3.5)
            elif row[-1] == 'B':
                grade.append(3)
            elif row[-1] == 'C+':
                grade.append(2.5)
            elif row[-1] == 'C':
                grade.append(2)
            elif row[-1] == 'D+':
                grade.append(1.5)
            elif row[-1] == 'D':
                grade.append(1)
            else:
                grade.append(0)
        point = [a * b for (a, b) in zip(grade, credit)]    # credit * grade

        gpa = math.floor(sum(point) / sum(credit) * 100) / 100
        print(gpa)
    elif command.startswith('INSERT INTO'):
        # INSERT INTO Grade.csv VALUES ('1', '1', 'Data', '3', 'B+')
        command = command.split(' VALUES ')
        table = command[0].split()[2]                       # Grade.csv
        value = [string_cleanup(command[1]).split(',')]     # [['1', '1', 'Data', '3', 'B+']]

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
