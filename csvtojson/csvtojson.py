# -*- coding: utf-8 -*-

import sys
import csv
import json

def main():
    try:
        print('-*-*-*-*-*- CSV to JSON -*-*-*-*-*-\n')
        
        input_file_name = 'input.csv'
        output_file_name = 'output.json'
        
        if len(sys.argv) >= 2:
            input_file_name = sys.argv[1]
        if len(sys.argv) >= 3:
            output_file_name = sys.argv[2]

        print('--> Input file: %s' % input_file_name)
        input_file = open(input_file_name, 'r', encoding='utf8')
        print('--> Output file: %s' % output_file_name)
        output_file = open(output_file_name, 'w', encoding='utf8')
        
        reader = csv.DictReader(input_file, delimiter=';')
        
        count_lines = 0
        first = True
        
        for row in reader:
            if first:
                first = False
            else:
                output_file.write('\n')
            json.dump(row, output_file)
            count_lines += 1

        print('\n--> JSON file saved successfully!')
        print('--> %s lines written' % count_lines)

        input_file.close()
        output_file.close()
    except Exception as e:
        print('Error: %s' % e)

if __name__== '__main__':
    main()
