from ast import Index
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
from operator import index
from tkinter import E


while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
        ##ここに書く
        if number == 1:
            number = int('hoge')
        elif number == 2:
            number = "hoge"
            number[8]
        elif number == 3:
            print("例外を発生させませんでした")
            continue
    except ValueError as e:
        print("Value Error")
        print(e.args)
    except IndexError as e:
        print("Index Error")
        print(e.args)
        
    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    ##ここに書く
    else:
        print("修了させます")
        break
print('↓')
print('無限ループを終了します')