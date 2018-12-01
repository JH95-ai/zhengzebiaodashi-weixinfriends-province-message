# -*-coding:utf-8 -*-
import re
string ='ccpeng1234'
regex_str='^d.*'
match_obj=re.match(regex_str,string)
if match_obj:
    print('Yes')
else:
    print('No')
