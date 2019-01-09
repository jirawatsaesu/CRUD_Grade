import csv

def convert_to_list(string):
    ''' Convert string with circle bracket, comma and space to list'''
    string = string.strip('()').replace("'", '').replace(' ', '')
    string = string.split(',')
    return string

while True:
    command = input('>')
    if command.startswith('INSERT INTO'):
        # INSERT INTO Grade.csv VALUES ('1', '1', 'Data', '3', 'B+')
        command = command.split(' VALUES ')
        table = command[0].split(' ')[2]
        value = convert_to_list(command[1])

        with open(table, 'a', newline='') as csvfile:
           writer = csv.writer(csvfile)
           writer.writerow(value)
    else:
        break