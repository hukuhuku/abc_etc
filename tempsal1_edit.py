import datetime as dt
import pandas as pd

#Todo
#環境データは一時間ごとに取られているが,PAM,成長率は月ごと
#データを編集して月ごとのcsvファイルにする

df = pd.read_csv("TempSal1.csv")
len_data = len(df['Date'])

###データにdatetime型の日付,時刻情報列を追加する
d = []
for i in range(len_data):
    a = df['Date'][i] + " " + df['Time'][i]
    tdate = dt.datetime.strptime(a,'%Y/%m/%d %H:%M:%S')
    d.append(tdate)

#Datetime列の追加
df['DateTime'] = d

#Date列,Time列の削除
del df["Date"]
del df["Time"]

###とりあえず期間に環境情報データの平均をとる

term = [dt.datetime(2012,9,14,0,0,1),dt.datetime(2012,10,16,0,0,1),dt.datetime(2012,11,19,0,0,1),
dt.datetime(2012,12,19,0,0,1),dt.datetime(2013,1,17,0,0,1),dt.datetime(2013,2,18,0,0,1),dt.datetime(2013,3,19,0,0,1),dt.datetime(2013,4,19,0,0,1),
dt.datetime(2013,5,20,0,0,1),dt.datetime(2013,6,17,0,0,1),dt.datetime(2013,7,19,0,0,1),dt.datetime(2013,9,1,0,0,1)]


df_2 = [[0 for i in range(3)]for i in range(len(term))]#Temp,Sal,Condをそれぞれの期間ごとに集計する
count = [0 for i in range(len(term))]#平均化のためにデータ数を記録する


for i in range(len_data):
    for index,kikan in enumerate(term):
        if df['DateTime'][i] <= kikan:
            df_2[index][0] += df['Temp'][i]
            df_2[index][1] += df['Sal'][i]
            df_2[index][2] += df['Cond'][i]
            count[index] += 1


#平均をとる
for i in range(len(term)):
    for j in range(3):
        df_2[i][j] /= count[i]

#ラベル作成
label = ['T09TH']
for i in range(10,13):
    label.append('T'+str(i)+'TH')
for i in range(1,9):
    label.append('T0'+str(i)+'TH')

#Pythonのリスト型からpandasパッケージのDataFrame型へ
df_2 = pd.DataFrame(df_2)
df_2.columns = ['Temp','Sal','Cond']
df_2.index = label

df_2.to_csv("TempSal2.csv")