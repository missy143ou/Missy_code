class ATM:
    def __init__(self):
        self.account=[{"name":"admin","password":"123"}]
        self.money=[{"name":"admin","money":0}] 
        # 這兩個可以合併
    def adduser(self,name,code):
        self.account.append({"name":name,"password":code})
        self.money.append({"name":name,"money":0})
    def addmoney(self,name,number):
        for a in self.money: 
            if a["name"] == name:
                a["money"]+=number
    def takemoney(self,name,number):
        for a in self.money:
            if a["name"] == name:
                a["money"]-=number

test=ATM() 

while True:
    answer=input("歡迎來到阿許銀行, 請問是要登入還是註冊新帳號? 登入請輸入1, 註冊請輸入2:")
    if answer=="2":
    
        while True:
            name=input("註冊新帳號, 請輸入你的名稱:")
            password=input("註冊新帳號, 請輸入你的密碼:")
            test.adduser(name,password)
            print(test.account)
            answer2=input("註冊完畢請按1, 繼續則按任意鍵")
            if answer2=="1":
                break

    if answer=="1":
        check_name=input("請輸入帳號:")
        check_password=input("請輸入密碼:")

        if {"name":check_name, "password":check_password} in test.account:
            print("good")
            answer2=input("存錢請按1, 提款請按2, 顯示餘額請按3: ")
            if answer2=="1":
                number2=input("你要存多少錢?")
                test.addmoney(check_name,float(number2))
            if answer2=="2":
                for a in test.money:
                    if a["name"] == check_name:
                        print("您的餘額是:", a["money"])
                        if a["money"]==0:
                            print("餘額不足")
                            break
                        number3=input("您要領多少錢?")
                        test.takemoney(check_name,float(number3))
                        print("您的餘額是:", a["money"])
            if answer2=="3":
                for a in test.money:
                    if a["name"] == check_name:
                        print("您的餘額是:", a["money"])
        else:
            print("輸入資訊有誤")
            

    
                
    

    





