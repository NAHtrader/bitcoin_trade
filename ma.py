import pandas as pd

yr=['2018','2019','2020']
month=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for y in yr:
    for m in month:
        tradedata = {}
        df = pd.read_excel("C:/Users/kjs01/AT/Bitcoin/"+y+"_"+m+".xlsx")
        num_index = len(df.index)
        for i in range(0,num_index):
            timedata = df.iloc[i, 0]
            op = df.iloc[i, 1]  # op 는 시작 가격
            tp = df.iloc[i, 2]  # tp 는 종가
            hp = df.iloc[i, 3]  # hp 는 고가
            lp = df.iloc[i, 4]  # lp 는 저가
            tradedata[timedata] = [op, tp, hp, lp, ma_6]

        tradedata = pd.DataFrame(tradedata)
        tradedata.rename(index={0: "Opening Price", 1: "Trade Price", 2: "High Price", 3: 'Low Price',4: 'ma_6'}, inplace=True)
        transposed_tradedata = tradedata.transpose()
        reversed_tradedata = transposed_tradedata.iloc[::-1]
        reversed_tradedata.to_excel(excel_writer='C:/Users/kjs01/AT/Bitcoin_ma/' + y + "_" + m + '.xlsx')  # 코인이름에 따라 폴더명 변경할 것!!
