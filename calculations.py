#Uses the information to calculate ROI/Passive income
def calculations(information,dividendValues):
    current_shares = information['current_shares']['value']
    stock_price = information['stock_price']['value']
    total_value = current_shares*stock_price
    months = 0
    extra = 0
    #formula = (1+PR)n - 1. where PR is a 5yr growth rate, and n converts it to a monthly growth rate.
    monthly_gain = ((1+(information['percent_gain']['value']/100))**(1.0/60)-1)
    #turns dividend/yield into the reflected payout amount(value/frequency).
    dividend = (information['dividend']['dividendValueValue']/dividendValues["{}".format(information['dividend']['dividendFrequencyValue'])])/100
    #the modifier allows for the total_value to remain unchacned, while changing the equation from passive to roi
    if information['goal']['goalTypeValue'] == "passive":
        modifier = dividend
    else:
        modifier = 1
    while total_value*modifier <= information['goal']['goalValue']:
        months += 1
        current_shares += int(information['monthly_addition']['value']/stock_price)
        stock_price = stock_price + (stock_price*monthly_gain)
        extra += information['monthly_addition']['value']%stock_price
        if months%dividendValues["{}".format(information['dividend']['dividendFrequencyValue'])] == 0:
            extra += total_value*dividend
        if extra/stock_price >= 1:
            current_shares += int(extra/stock_price)
            extra = extra%stock_price
        total_value = current_shares * stock_price
    print ("Months:{}\tShares:{}\tStock Price:{}\tTotal Value:{}\tDividend:{}".format(months,current_shares,stock_price,total_value,total_value*(dividend)))
