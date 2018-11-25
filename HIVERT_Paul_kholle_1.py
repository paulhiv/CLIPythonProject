# Author: Paul Hivert
import os
import sys
import argparse
import csv

# varriables
parser = argparse.ArgumentParser()
file_csv ='list.csv'
array = []

# define functions

csv_writer = lambda csvfile: csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_reader = lambda csvfile: csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

def Get_rows():
    with open(file_csv, 'r') as csvfile:
        reader = csv_reader(csvfile)
        try:
            [(array.append(row[entry])) for row in reader for entry in range(len(row))]
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (file_csv, reader.line_num, e))

def Get_min():
    minimim = min(array)
    return minimim

def Get_max():
    maximum = max(array)
    return maximum

def Get_moy():
    return Get_sum() / len(array)

def Get_sum():
    rows = [int(row) for row in array]
    return sum(rows)


def DeleteRows():
    try:
        os.remove('list.csv')
        sys.stdout.write("list reset")
    except Exception as e:
        sys.stdout.write(str(e))

def Write_row(entry):
    with open(file_csv, 'a') as csvfile:  
        if entry.isdigit():
            try:
                csv_writer(csvfile).writerow(entry)
            except Exception as e:
                sys.stdout.write(str(e)+'\n')

def Sort_list():
    rows = [int(row) for row in array]
    return sorted(rows, key=int)

def Sort_list_desc():
    rows = [int(row) for row in array]
    return sorted(rows, key=int, reverse=True)

# Start of program
# check if lists.csv exists in the current directory and create one if not
try:
    with open(file_csv, 'r') as csvfile:
        sys.stdout.write('list.csv found\n')
except Exception as e:
    sys.stdout.write(str(e)+'\ncreating list\n')
    with open(file_csv, 'w+') as csvfile:
        pass


# initialize CLI positional arguments

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-l', help = 'list all integers', action= 'store_true')
parser.add_argument('-a', nargs = '*', help = 'add integers to list ex: HIVERT_PAUL_KHOLLE_1.py -a 1 2 3')
parser.add_argument('-c', action='store_true', help = 'reset the list')
parser.add_argument('-s', '--max', action='store_true', help='display the list in ascending order')
parser.add_argument('-s', '--min', action='store_true', help='display the list in ascending order')
parser.add_argument('-s', '--moy', action='store_true', help='display the average of the list')
parser.add_argument('-s', '--sum', action='store_true', help='display the sum of the list')
parser.add_argument('-t', action='store_true', help = 'sort list in ascending order')
parser.add_argument('-desc', action='store_true', help = 'sort in descending order')

args = parser.parse_args()

#argument handling
if args.l:
    Get_rows()
    sys.stdout.write(str(array))
    
elif args.a:
    list(map(Write_row, args.a))
    sys.stdout.write(str(args.a)+' were added to the list')

elif args.c:
    DeleteRows()

elif args.min:
    Get_rows()
    sys.stdout.write(Get_min())
    

elif args.max:
    Get_rows()
    sys.stdout.write(Get_max())
    pass

elif args.moy:
    Get_rows()
    sys.stdout.write(str(Get_moy()))

elif args.sum:
    Get_rows()
    sys.stdout.write(str(Get_sum()))

elif args.t:
    Get_rows()
    Sort_list()
    sys.stdout.write('sorted\n'+ str(Sort_list()))

elif args.desc:
    Get_rows()
    sys.stdout.write('sorted in reverse order\n'+str(Sort_list_desc()))
