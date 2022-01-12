#test01.py

import random
answer = random.randint(1, 10)

while True:  # 無限ループ
    try:
        number = int(input('10までの数値を入力してください: '))
        # 問①：ValueError例外を処理するコードを記述してください。
    except ValueError:
        continue
    
    if answer< number:
        print('もっと小さな数値です')
        # 問②：画像のように表示するように、コードを記述してください。
    elif answer > number:
        print("もっと大きな数字です")
    elif type(number) is str:
        print("整数ではない")
    else:
        break  # 変数answerの値と変数numberの値が等しければ終了
print(type(number))
print('正解！')