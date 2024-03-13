import random
import pandas as pd

df1 = pd.DataFrame({"薪資":[100, 100, 100, 100],
                    "差旅":[100, 100, 100, 100],
                    "公關":[100, 100, 100, 100],
                    "加班":[100, 100, 100, 100]},
                    index =["Q1", "Q2", "Q3", "Q4"])
 
print(df1)

while True:
    df2 = pd.DataFrame({"薪資":[random.randrange(50), random.randrange(50), random.randrange(50), random.randrange(50)],
                    "差旅":[random.randrange(50), random.randrange(50), random.randrange(50), random.randrange(50)],
                    "公關":[random.randrange(50), random.randrange(50), random.randrange(50), random.randrange(50)],
                    "加班":[random.randrange(50), random.randrange(50), random.randrange(50), random.randrange(50)]},
                    index =["Q1", "Q2", "Q3", "Q4"])
    df1=df1.subtract(df2)
    print(df1)
    if df1.iloc[3,0]<50:
        break

print("--------------")
print(df1)