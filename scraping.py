from bs4 import BeautifulSoup
import requests

url = 'https://www.stat.go.jp/data/shakai/2011/rank/rank3.html'
response = requests.get(url)
response.encoding = 'shift_jis'
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all('tr')

all_prefectures_data = []
for row in rows:
    # 各tdタグからテキストを取得
    tds = row.find_all('td')
    if len(tds) == 4: 
        rank_data = {
            'rank': tds[0].text.strip(),
            'prefecture': tds[1].text.strip(),
            'hours': tds[2].text.strip(),
            'minutes': tds[3].text.strip()
        }
        all_prefectures_data.append(rank_data)

# 結果を出力します。
for data in all_prefectures_data:
    print(data)

import sqlite3

# データベース接続のセットアップ
conn = sqlite3.connect('prefectures_data.db')  # データベースファイルを指定
cursor = conn.cursor()

# テーブルの作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prefecture_statistics (
        rank INTEGER,
        prefecture TEXT,
        hours INTEGER,
        minutes INTEGER
    )
''')

# データの挿入
for data in all_prefectures_data:
    cursor.execute('''
        INSERT INTO prefecture_statistics (rank, prefecture, hours, minutes)
        VALUES (?, ?, ?, ?)
    ''', (data['rank'], data['prefecture'], data['hours'], data['minutes']))

# 変更をコミットし、接続を閉じる
conn.commit()
conn.close()