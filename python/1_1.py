# int型のリストdataを作成し、値を1,3,5,7で初期化
date = [1,3,5,7]

for i in date:
    print(i**2)
#問1－2
for j in range(1,8,2):
    print(j**2)
    
#問2－1
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if "横浜" in place:
        print(place + "のチケットが当選しました！")
    elif "札幌" in place or "大阪" in place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")
        
#問2－2
wait_place += get_place
ans = "{0[0]}と{0[1]}と{0[2]}のチケットが当選しました！"
print(ans.format(wait_place))