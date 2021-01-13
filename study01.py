import pandas as pd

df = pd.read_csv('kimetsu.csv')
source = list(df['キャラクターネーム'])

search = input('キャラクターリストから検索するキャラクター名を入力してください：')

if search in source:
    print(f'「{search}」はキャラクターリストにありました')
else:
    source.append(search)
    print(f'「{search}」はキャラクターリストに無かったので、追加しました')
    # print(source)

df = pd.DataFrame({'キャラクターネーム': source})
df.to_csv('kimetsu.csv', index=False)