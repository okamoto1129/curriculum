from ast import Index
from multiprocessing.sharedctypes import Value
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
            number = "hoge"
    except ValueError as e:
        print(e)
        print(e.args)
    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    ##ここに書く
    else:
        break
print('↓')
print('無限ループを終了します')