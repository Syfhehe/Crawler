import pymysql


# 连接数据库
def connect_wxremit_db():
    return pymysql.connect(host='cdb-6ziqfv67.gz.tencentcdb.com',
                           port=10119,
                           user='root',
                           password='admin123456',
                           database='car168',
                           charset='utf8')


# 查询
def query_url_by_status(cc2):
    sql_str = ("SELECT url"
                + " FROM brand"
                + " WHERE status='%s'" % (cc2))
    con = connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    assert len(rows) != 0, 'Fatal error: country_code does not exists!'
    return rows[0][0]

#插入多条数据
def insert_data(aa):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:
        cur.executemany("INSERT INTO brand (name, url, status)" + " VALUES (%s, %s, %s)", aa)
        assert cur.rowcount == len(aa), 'my error message'
        con.commit()
    except Exception as e:
        con.rollback()
    finally:
        cur.close()
        con.close()


#更新状态
def update_status_by_url(url, status):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:
        sql_str = ("SELECT status"
                   + " FROM brand"
                   + " WHERE url='%s'" % url
                   + " FOR UPDATE")

        cur.execute(sql_str)
        assert cur.rowcount == 1, 'Fatal error: The wx-refund record be deleted!'

        sql_str_update = ("UPDATE brand"
                    + " SET status='%s'" % status
                    + " WHERE url='%s'" % url)
        cur.execute(sql_str_update)
        print(sql_str_update)
        assert cur.rowcount == 1, 'The number of affected rows not equal to 1'
        con.commit()
    except Exception as e:
        con.rollback()
        raise
    finally:
        cur.close()
        con.close()


# connection = connect_wxremit_db()
#
# result = query_url_by_status('not start')
# print(result)

# brands = [('benz', 'http://www.chehang168.com/index.php?c=index&m=brand&pbid=bd4Tl', 'not start'), ('audi', 'http://www.chehang168.com/index.php?c=index&m=brand&pbid=65eWU','not start')]
# insert_data(brands)

update_status_by_url('http://www.chehang168.com/index.php?c=index&m=brand&pbid=bd4Tl', 'finished');