import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='10baton', db='meibo_db', charset='utf8')
curs = conn.cursor()

#curs.execute("CREATE TABLE meibotest(id INT, lastname TEXT, firstname TEXT, lstyomi TEXT, fstyomi TEXT, start DATE, birth DATE, age INT);" )
# ↑↑↑すでにTABLE作成済み
#curs.execute("INSERT INTO meibotest VALUES (ユーザID, '名字', '名前', '名字読み', '名前読み', '入社日', '誕生日', 年齢);")
# ↑↑↑すでにINSERT作成済み
# conn.commit()

sql = ("select * from meibotest;")
curs.execute(sql)
result = curs.fetchall()

for id, lastname, firstname, lstyomi, fstyomi, start, birth, age in result:
    print(id, lastname, firstname, lstyomi, fstyomi, start, birth, age)
