stock_price = ""
while not isinstance(stock_price, float):
    try:
        stock_price = input("Input price of individual Stock(Float): ")
    except SyntaxError:
        stock_price = None
    try:
        stock_price = float(stock_price)
        print(stock_price)
    except:
        print("Not a Float")

percent_gain = ""
while not isinstance(percent_gain, float):
    try:
        percent_gain = input("What is the % gain over the last 5yrs(Float)?: ")
    except SyntaxError:
        percent_gain = None
    try:
        percent_gain = float(percent_gain)
        print(percent_gain)
    except:
        print("Not a Float")

dividend = ""
while not isinstance(dividend, float):
    try:
        dividend = input("What is the dividend yield?: ")
    except SyntaxError:
        dividend = None
    try:
        dividend = float(dividend)
        print(dividend)
    except:
        print("Not a Float")

current_shares = ""
while not isinstance(current_shares, int):
    try:
        current_shares = input("How many shares do you currently have?: ")
    except SyntaxError:
        current_shares = None
    try:
        current_shares = int(current_shares)
        print(current_shares)
    except:
        print("Not an Integer")

monthly_addition = ""
while not isinstance(monthly_addition, float):
    try:
        monthly_addition = input("How much money can you spend on new shares every month? : ")
    except SyntaxError:
        monthly_addition = None
    try:
        monthly_addition = float(monthly_addition)
        print(monthly_addition)
    except:
        print("Not a Float")

goal = ""
while not isinstance(goal, int):
    try:
        goal = input("What is goal amount(in $)? : ")
    except SyntaxError:
        goal = None
    try:
        goal = int(goal)
        print(goal)
    except:
        print("Not an Integer")
months = 0
extra = 0
monthly_gain = ((1+(percent_gain/100))**(1.0/60)-1)
print(monthly_gain)
total_value = current_shares * stock_price

while total_value*(dividend/12/100) <= goal:
    months += 1
    current_shares += int(monthly_addition/stock_price)
    stock_price = stock_price + (stock_price*monthly_gain)
    extra += monthly_addition%stock_price
    extra += total_value*(dividend/12/100)
    print(extra)
    if extra/stock_price >= 1:
        current_shares += int(extra/stock_price)
        extra = extra%stock_price
        print(extra)
    total_value = int(current_shares) * stock_price
    print ("months :{} Value: {} shares: {} stock_price:{} dividend:{}".format(str(months),str(total_value),current_shares,stock_price,total_value*(dividend/12/100)))
