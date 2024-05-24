# -*- coding: utf-8 -*-
import sys

# 将控制台编码方式设置为 'utf-8'
#sys.stdout.reconfigure(encoding='utf-8')
a ='中'
b=b'\xe4\xb8\xad'
print(type(a.encode()),a.encode(),type(b))