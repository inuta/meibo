import MySQLdb
import datetime

conn = MySQLdb.connect(host='localhost', user='root', passwd='10baton', db='meibo_db', charset='utf8')
curs = conn.cursor()



userid = input('ユーザIDは? ')
myoji = input('名字は? ')
namae = input('名前は? ')
myomi = input('名字の読み方は?　(カタカナで) ')
nyomi = input('名前の読み方は?　(カタカナで) ')
nyusha = input('入社日はいつ? (yyyy/mm/dd) ')
tanjobi = input('誕生日はいつ? (yyyy/mm/dd) ')
nennrei = input('年齢はいくつ?' )

tenn = "'"

sql = '''
    INSERT INTO meibotest(
    id, lastname, firstname, lstyomi, fstyomi, start, birth, age
    ) VALUES (
    {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}
    );
    '''.format(userid, tenn + myoji + tenn,
                tenn + namae + tenn,
                tenn + myomi + tenn,
                tenn + nyomi + tenn,
                tenn + nyusha + tenn,
                tenn + tanjobi + tenn, nennrei)

print(sql)



curs.execute(sql)

conn.commit()

sql = ("select * from meibotest;")
curs.execute(sql)
result = curs.fetchall()

for id, lastname, firstname, lstyomi, fstyomi, start, birth, age in result:
    print(id, lastname, firstname, lstyomi, fstyomi, start, birth, age)
