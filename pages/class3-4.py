import random as rm

ans = rm.randint(1, 100)   # 隨機產生1到100的整數
min_num = 1
max_num = 100
while True:  # 無窮迴圈
    # 可以把想要測試的程式碼放在try裡面，如果程式碼有錯誤，就執行 except 裡面的程式碼
    # try跟except是一對的，最少要有一個try跟一個except，也可以有多個except
    try:
        num = int(input(f"請輸入{min}到{max}的整數"))
    except:   # 如果輸入的不是數字整數
        print("請輸入1到100的整數數字，不要亂輸入!")
        continue  # 跳過這次回圈，直接進入下一次迴圈
    if num < 0 or num > 100:  # 如果輸入超出範圍
        print("請輸入1到100的整數數字")
    elif num > ans:  # 如果輸入的數字大於答案
        print("太大了")
        if num < max_num:   # 檢查 num是否小於 max_num
            max_num = num   # 如果 num 小於 max_num 就更新範圍
    elif num < ans:  # 如果輸入的數字小於答案
        print("太小了")
        if num > min_num:   # 檢查 num是否大於 min_num
            min_num = num   # 如果 num 大於 min_num 就更新範圍
        else:  # 如果 num 等於 ans
            print("答對了")
            break  # 跳出迴圈