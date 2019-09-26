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
