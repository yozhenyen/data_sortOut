import pandas as pd

df_data = pd.read_csv('data.csv')
df_time = pd.read_csv('time.csv')
df_all11 = pd.read_csv('all3.csv')
data = []
time = []

for f in range(0, 12):
    for x in df_data['num']:
        for i in range(0, 28):
            data.append(x)
            # print(data)
    for y in df_time['0']:
        time.append(y)

df_all11['num'] = data
df_all11.to_csv('all3.csv', index=False)
# for y in df_time['0']:
    # print(y)