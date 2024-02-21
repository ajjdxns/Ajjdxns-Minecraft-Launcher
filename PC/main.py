'''
Ajjdxns minecraft launcher
(C) 2024 Ajjdxns
'''

import sys
import os
from console_start import console

command = ""
argv = sys.argv

try:
    if argv[1] == '--version':
        with open(r"/text/wirte.txt",'r') as f:
            print(f.read())
            os._exit()
except:
    os._exit(0)

def main():
    '''
    主要的核心程序
    '''
    print("Ajjdxns minecraft launcher Copyright (C) 2024 Ajjdxns studio\n本程序没有任何保证，输入“license 15”了解更多。\n这是一个自由软件，欢迎再次分发。输入“license 3”了解详情。\n随程序应该有一份GPL3.0协议，如果没有找到，从这里找：https://www.gnu.org/licenses/。\n使用参数“--version”查看更多协议")
    while True:
        command = input("(AMLcommand)")
        if command == "quit":
            os._exit()

if __name__ == "__main__":
    main()