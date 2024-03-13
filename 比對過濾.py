import pandas as pd

a={"color":["green","green","green","blue","blue","red","red","red"],"shape":["rectangle","square","rectangle","rectangle","square","square","square","rectangle"],"price":[10,15,5,5,10,15,15,5]}
a1=pd.DataFrame(a)
print(a1)
print("------")

a4=input("你要買幾個箱子?")

tmp=[]
for b in range(int(a4)):
 a2=input(f"{b+1}號箱子請輸入顏色")
 a3=input(f"{b+1}號箱子請輸入形狀")
 selected=a1.loc[(a1["color"]==a2) & (a1["shape"]==a3)]
#  print(selected)
 tmp.append(selected)

print(pd.concat(tmp))

