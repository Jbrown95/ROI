#a dict that is used to convert information['dividend']['dividendFrequencyValue'] into number values
dividendValues = {
    "annually":1,
    "bi-annually":2,
    "quarterly":4,
    "monthly":12,
    "None":1

}
#dict for information used in calculations().
information = {
    'stock_price':{
    'text':"Input price of individual Stock. : ",
    'value':None
    },
    'percent_gain':{
    'text':"What is the % gain over the last 5yrs? : ",
    'value':None
    },
    'dividend':{
    'dividendYesNoText':"Does this stock pay dividends(yes/no)? : ",
    'dividendYesNoValue':None,
    'dividendFrequencyText':"How often does it pay?(annually/bi-annually/quarterly/monthly) : ",
    'dividendFrequencyValue':"None",
    'dividendValueText':"what is Dividend/Yield? : ",
    'dividendValueValue':0,
    },
    'current_shares':{
    'text':"How many shares do you currently have? : ",
    'value':None
    },
    'monthly_addition':{
    'text':"How much money will you spend on this stock every month? : ",
    'value':None
    },
    'goal':{
    'goalTypeText':"Is the goal ROI or Passive income? : ",
    'goalTypeValue':None,
    'goalPassiveText':"What is monthly passive goal? : ",
    'goalROIText':"What is ROI goal? : ",
    'goalValue':None,
    },

}
#Checks the value of inputs to confirm they are what we want.
def checkValue(desiredValue,value):
    if "/" in desiredValue:
        print(desiredValue)
        while True:
            inputValue = input("{}".format(value))
            options = desiredValue.split("/")
            for option in options:
                if inputValue == option:
                    return inputValue
                    break
            print("{} please".format(desiredValue))
            continue
    elif desiredValue == "Float":
        while True:
            try:
                inputValue = float(input("{}".format(value)))
                return inputValue
                break
            except ValueError:
                print("Enter a number please.")

    elif desiredValue == "Integer":
        while True:
            try:
                inputValue = int(input("{}".format(value)))
                return inputValue
                break
            except ValueError:
                print("Enter a number please.")



#gets info from user for information dict
def get_info():
    information['stock_price']['value'] = checkValue("Float",information['stock_price']['text'])
    information['percent_gain']['value'] = checkValue("Float",information['percent_gain']['text'])
    information['dividend']['dividendYesNoValue'] = checkValue("yes/no",information['dividend']['dividendYesNoText'])
    if information['dividend']['dividendYesNoValue'] == "yes":
        information['dividend']['dividendFrequencyValue'] = checkValue("annually/bi-annually/quarterly/monthly",information['dividend']['dividendFrequencyText'])
        information['dividend']['dividendValueValue'] = checkValue("Float",information['dividend']['dividendValueText'])
    information['current_shares']['value'] = checkValue("Float",information['current_shares']['text'])
    information['monthly_addition']['value'] = checkValue("Float",information['monthly_addition']['text'])
    if information['dividend']['dividendFrequencyValue'] != "monthly":
        print("Your stock does not pay monthly, find a different investment for passive. We will continue with an ROI goal.")
        information['goal']['goalTypeValue'] = "roi"
    else:
        information['goal']['goalTypeValue'] = checkValue("passive/roi",information['goal']['goalTypeText'])
    if information['goal']['goalTypeValue'] == "passive":
        information['goal']['goalValue'] = checkValue("Float",information['goal']['goalPassiveText'])
    else:
        information['goal']['goalValue'] = checkValue("Float",information['goal']['goalROIText'])

#Uses the information to calculate ROI/Passive income
def calculations():
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
        print ("months:{}\tValue\:{}\tshares:{}\tstock_price:{}\tdividend:{}".format(months,current_shares,stock_price,total_value,total_value*(dividend)))

if __name__ == "__main__":
    get_info()
    calculations()
