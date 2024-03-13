#chatGPT設計平均數計算機

def calculate_average():
    numbers = []  # 創建一個空的數字列表
    
    while True:
        user_input = input("輸入一個數字 (或輸入 'done' 來計算平均值): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            number = float(user_input)  # 將用戶輸入轉換為浮點數
            numbers.append(number)
        except ValueError:
            print("請輸入有效的數字或 'done' 來計算平均值。")

    if numbers:
        average = sum(numbers) / len(numbers)
        return average
    else:
        return None  # 如果列表為空，返回None或其他適當的值

result = calculate_average()

if result is not None:
    print(f"平均值為: {result:.3f}")
else:
    print("沒有數字可以計算平均值。")