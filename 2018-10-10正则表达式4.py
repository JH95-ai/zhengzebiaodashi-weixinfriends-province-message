# -*-coding:utf-8 -*-
#提取电话号码
import re
string ='18893165883'
#以1开头，第二个数字从3，4，5，6，7，8中任意选一个，之后的字符是0到9中的数字，但是限定为9次
regex_str='(1[345678][^1]{9})'
match_obj=re.match(regex_str,string)
if match_obj:
    print(match_obj.group(1))
