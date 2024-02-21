'''
Ajjdxns minecraft launcher
(C) 2024 Ajjdxns
'''

import sys
import os
from console_start import console

command = ""
argv = sys.argv

console.print("Ajjdxns minecraft launcher Copyright (C) 2024 Ajjdxns studio\n本程序没有任何保证，输入“license 15”了解更多。\n这是一个自由软件，欢迎再次分发。输入“license 3”了解详情。\n随程序应该有一份GPL3.0协议，如果没有找到，从这里找：https://www.gnu.org/licenses/。\n使用命令“version”查看更多协议")

def main():
    '''
    主要的核心程序
    '''
    while True:
        command = input(">>>")
        if command == "quit":
            os._exit(1)
        elif command == "version":
            console.print('Ajjdxns minecraft launcher\nCopyright (C) Ajjdxns studio(电子邮件：wyj121023@163.com,备用地址：ajjdxns@outlook.com)\nver. alpha 0.1\n基于GPL3.0\n我们希望这个\n程序对你有用，但是不保证它真的好用。随程序应该有一\n份GPL3.0协议，如果没有找到，从这里找：https://www.gnu.org/licenses/以下简称AML启动\n器。（可看可不看）\nAML启动器根据GPL3.0协议，允许您进行软件破解、源代码分发以及分发破解版软件。\n但是破解版软件并不属于AML启动器的一部分，向外分发时请不要使用与本产品相近或类似的名字。\n在您分发该项目副本时，请注明该文件的源代码地址和分发平台。\n此外，请您遵守附加条款：\n1.修改后的代码与Ajjdxns studio没有任何关系，我们也不对此负责。\n2.修改后的代码中请注明代码的原作者。\n3.修改后的代码请不要用Ajjdxns(代码作者)的名义宣传。\n4.请让您的软件使用者明白，这个软件是基于Ajjdxns studio的源代码修改的，Ajjdxns studio对其中的BUG概不负责。\n5.如果有涉及到钱的修改版，修改版作者将不能继续使用软件最新版进行修改，同时停止作者对修改版软件中未修改部分的支持。\n')

if __name__ == "__main__":
    main()