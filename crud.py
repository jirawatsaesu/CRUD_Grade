import csv

def string_cleanup(string):
    ''' Remove circle bracket, comma and space from string'''
    string = string.strip('()').replace("'", '').replace(' ', '')
    return string

while True:
    command = input('>')
    if command.startswith('INSERT INTO'):
        # INSERT INTO Grade.csv VALUES ('1', '1', 'Data', '3', 'B+')
        command = command.split(' VALUES ')
        table = command[0].split(' ')[2]                # Grade.csv
        value = string_cleanup(command[1]).split(',')   # ['1', '1', 'Data', '3', 'B+']

        with open(table, 'a', newline='') as csvfile:
           writer = csv.writer(csvfile)
           writer.writerow(value)
        csvfile.close()
    elif command.startswith('UPDATE'):
        # Collect data from csv file
        with open('Grade.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
        csvfile.close()
        attribute = data[0]

        # UPDATE Grade.csv SET Grade='A' WHERE Subject='Data'
        command = command.split()
        table = command[1]                                      # Grade.csv
        where_col = command[5].split('=')[0]                    # Subject
        where_row = string_cleanup(command[5].split('=')[1])    # Data
        set_col = command[3].split('=')[0]                      # Grade
        set_row = string_cleanup(command[3].split('=')[1])      # A

        for i in range(len(data)):
            if where_row in data[i]:
                select_data = data[i]
                select_row = i

        index_change = attribute.index(set_col)
        select_data[index_change] = set_row
        data[select_row] = select_data

        with open('Grade.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
    else:
        break