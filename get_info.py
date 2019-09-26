#used for confirming Values entered are usable in the scripts
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
def get_info(information,dividendValues):
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
