#!/usr/bin/env python3      # サーバのどこにPythonのどこにインタプリタがあるかを意味する。

import cgi
import html
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='PW', db='meibo_db', charset='utf8')
curs = conn.cursor()

print('Content-type: text/html')
print('')

def print_html(data=''):
    print('''\
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>
                TopPage
            </title>
        </head>
        <body>
            <h1>meibo TopPage</h1>
            <form action="toppage.py" method="post">
                ユーザID<input type="text" name="userid">
                名字<input type="text" name="name">
                <input type="hidden" name="mode" value="search">
                <input type="submit" value="検索">
            </form>
            <ul>
                {0}
            </ul>
        </body>
    </html>
    '''.format(data))


form = cgi.FieldStorage()
mode = form.getvalue('mode')

point = "'"
form_check = 0

if mode == 'search':
    if 'userid' in form:                  # mekaに値が入力され、
        if 'name' in form:              # 1.itemにも入力されていたら
            form_check = 1
        elif not 'name' in form:        # 2.itemには入力されていなかったら
            form_check = 2

    elif 'name' in form:                # itemに値が入力され、
        if 'userid' in form:              # 1.mekaにも入力されていたら
            form_check = 1
        elif not 'userid' in form:        # 2.mekaには入力されていなかったら
            form_check = 3

    if form_check == 0:     # 両方とも何も入力されていなかったら、form_checkは0なので以降の処理を行う。
        sql = ("SELECT * FROM meibotest")

    elif form_check == 1:
        userid = form.getvalue('userid')
        userid = html.escape(userid)

        name= form.getvalue('name')
        name= html.escape(name)

        slctU = 'id=' + point + userid + point
        slctN = 'lastname=' + point + name + point
        sql = ("SELECT * FROM meibotest WHERE " + slctU + ' AND ' + slctN)

    elif form_check == 2:
        userid = form.getvalue('userid')
        userid = html.escape(userid)

        slctU = 'id=' + point + userid + point
        sql = ("SELECT * FROM meibotest WHERE " + slctU)

    elif form_check == 3:
        name = form.getvalue('name')
        name = html.escape(name)
        slctN = 'lastname=' + point + name + point
        sql = ("SELECT * FROM meibotest WHERE " + slctN)

    curs.execute(sql)

result = curs.fetchall()

data = ''

for id, lastname, firstname, lstyomi, fstyomi, start, birth, age in result:
    data += '''
    <li>{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}
    </li>
    '''.format(id, lastname, firstname, lstyomi, fstyomi, start, birth, age)
print_html(data)
