import pandas as pd

df = pd.read_excel("C:/Users/kjs01/AT/Bitcoin/2018_01.xlsx")
# start=500000
num_index = len(df.index)
total_profit=[]
charge=[]
lose=0
win=0
buy_commission=0
sell_commission = 0
for i in range(9, num_index-1):
    date = df.iloc[i, 0]legendary-octo-brocco
    op_a = df.iloc[i, 1]  # op 는 시작 가격
    tp_a = df.iloc[i, 2]  # tp 는 종가
    hp_a = df.iloc[i, 3]  # hp 는 고가
    lp_a = df.iloc[i, 4]  # lp 는 저가
    ms_10=0
    for k in range(0,10):
        ms_10+=df.iloc[(i-k),2]
    ma_10=((ms_10)/10)

    if hp_a>ma_10 and op_a<ma_10:


        # buy_num=(start/ma_10)
        # sell=(df.iloc[i+1,2]*buy_num)
        # profit=(sell-start)
        profit=((df.iloc[(i+1), 2])-ma_10)

        buy_commission=250
        sell_commission=250

        charge.append(buy_commission)
        charge.append(sell_commission)
        total_profit.append(profit)
        if profit < 0:
            lose += 1
        else:
            win += 1

total_plus=sum(total_profit)
total_charge=sum(charge)
win_ratio = (win/(win+lose)*100)

print(total_plus)
print(total_charge)
print(win_ratio)
print(len(total_profit))
