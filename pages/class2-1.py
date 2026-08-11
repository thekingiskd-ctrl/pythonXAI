# 比較運算子，只能同樣型作比較
print(1==1)   #True
print(1!=1)   #False
print(1>1)    #False
print(1<1)    #False
print(1>=1)   #True
print(1<=1)   #True

#邏輯運算子
# and 運算，兩個條件都成立才會成立
print(True and True)   #True
print(False and True)  #False
print(True and False)  #False
print(False and False) #False

# or 運算，兩個條件只要有一個成立就會成立
print(True or True)    #True
print(True or False)   #True
print(False or False)  #False

# not 運算，將條件反過來
print(not True)        #False
print(not False)       #True

# 密碼驗證
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎chloe")
else:
    print("密碼錯誤")
# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的復雜度，也節省了時間
# 但是如果是使用多個if來判斷，則每個if都會被執行，所以效率較低


#BMI計算
height = float(input("請輸入身高(公尺)："))
weight = float(input("請輸入體重(公斤)："))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("體重正常")
else:
    print("體重過重")

