# -*-coding:utf-8 -*-
import re
string ='dcpeng1234'
regex_str='(dcpeng1|dcpeng1234)'
match_obj=re.match(regex_str,string)
if match_obj:
    print(match_obj.group(1))