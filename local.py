import pandas as pd
import sqlite3

csv_file_path = '/Users/shionozakiayae/DSP1/DSPro2_final/localdata.csv'

data = pd.read_csv(csv_file_path)

# SQLiteデータベースへの接続
conn = sqlite3.connect('local.db')

# データをデータベースに保存
data.to_sql('local', conn, if_exists='replace', index=False)

# 接続を閉じる
conn.close()


# データベースファイルに接続
conn = sqlite3.connect('local.db')
cursor = conn.cursor()

# テーブル 'local' から全てのデータを選択するクエリを実行
cursor.execute('SELECT * FROM local')

# 結果を取得
rows = cursor.fetchall()

# 各行を表示
for row in rows:
    print(row)

# 接続を閉じる
conn.close()
