# -*- coding: utf-8 -*-

import sys
import requests as req
from bs4 import BeautifulSoup as bs
import json

def get_foros(url):
    try:
        r = req.get(url)
        
        soup = bs(r.text, 'html.parser')
        scripts = soup.find_all('script')
        script = scripts[28]

        txt_ini = 'JSON.parse(\''
        index_ini = str(script).index(txt_ini)
        
        txt_fin = '\');'
        index_fin =  str(script).index(txt_fin)
        
        return json.loads(str(script)[index_ini + len(txt_ini) : index_fin])
    except Exception as e:
        print('Error: %s' % e)

def main():
    try:
        print('-*-*-*-*-*- Get Foros TJSP -*-*-*-*-*-\n')
        
        url = 'https://esaj.tjsp.jus.br/cpopg/open.do'
        output_file_name = 'output.json'
        
        if len(sys.argv) >= 3:
            output_file_name = sys.argv[2]
        if len(sys.argv) >= 2:
            url = sys.argv[1]

        print('--> Output file: %s\n' % output_file_name)
        output_file = open(output_file_name, 'w', encoding='utf8')
        
        foros = get_foros(url)
        count_lines = 0
        first = True
        
        for f in foros:
            if first:
                first = False
            else:
                output_file.write('\n')
            print(f['text'])
            json.dump(f, output_file)
            count_lines += 1

        print('\n--> JSON file saved successfully!')
        print('--> %s lines written' % count_lines)
            
        output_file.close()
    except Exception as e:
        print('Error: %s' % e)

if __name__== '__main__':
    main()
