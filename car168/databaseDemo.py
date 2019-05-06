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
def query_series_url_by_status(cc2):
    sql_str = ("SELECT url"
                + " FROM series"
                + " WHERE status='%s'" % (cc2))
    con = connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    assert len(rows) != 0, 'Fatal error: series url does not exists!'
    return rows

# 查询
def query_series_person_url_by_status(cc2):
    sql_str = ("SELECT url"
                + " FROM series_person"
                + " WHERE status='%s'" % (cc2))
    con = connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    assert len(rows) != 0, 'Fatal error: series url does not exists!'
    return rows

# 查询
def query_company_url_by_status(cc2):
    sql_str = ("SELECT distinct url"
                + " FROM seller_backup"
                + " WHERE status='%s'" % (cc2))
    con = connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()

    assert len(rows) != 0, 'Fatal error: series url does not exists!'
    return rows


#插入多条数据
def insert_data_brand(aa):
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


#插入多条数据
def insert_data_series(aa):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:
        cur.executemany("INSERT INTO series (name, url, status)" + " VALUES (%s, %s, %s)", aa)
        assert cur.rowcount == len(aa), 'my error message'
        con.commit()
    except Exception as e:
        con.rollback()
    finally:
        cur.close()
        con.close()


#插入多条数据
def insert_data_seller(aa):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:
        cur.executemany("INSERT INTO seller (name, url, status)" + " VALUES (%s, %s, %s)", aa)
        assert cur.rowcount == len(aa), 'my error message'
        con.commit()
    except Exception as e:
        con.rollback()
    finally:
        cur.close()
        con.close()

#插入多条数据
def insert_data_person(aa):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:
        cur.executemany("INSERT INTO person (name, url, status)" + " VALUES (%s, %s, %s)", aa)
        assert cur.rowcount == len(aa), 'my error message'
        con.commit()
    except Exception as e:
        con.rollback()
    finally:
        cur.close()
        con.close()

def delete_data_seller(url):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:
        delete_sql = "delete from seller_backup where url = '%s'" % url
        print(delete_sql)
        cur.execute(delete_sql)
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        cur.close()
        con.close()


#更新状态
def update_company_status_by_url(address, contact, url, status):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:

        sql_str_update = ("UPDATE seller_backup"
                    + " SET status='%s', " % status
                    + " contact='%s', " % contact
                    + " address='%s' " % address
                    + " WHERE url='%s'" % url)
        print(sql_str_update)
        cur.execute(sql_str_update)
        # assert cur.rowcount == 1, 'The number of affected rows not equal to 1'
        con.commit()
    except Exception as e:
        con.rollback()
        raise
    finally:
        cur.close()
        con.close()


#更新状态
def update_series_status_by_url(url, status):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:

        sql_str_update = ("UPDATE series"
                    + " SET status='%s'" % status
                    + " WHERE url='%s'" % url)
        cur.execute(sql_str_update)
        print(sql_str_update)
        # assert cur.rowcount == 1, 'The number of affected rows not equal to 1'
        con.commit()
    except Exception as e:
        con.rollback()
        raise
    finally:
        cur.close()
        con.close()


#更新状态
def update_series_person_status_by_url(url, status):
    con = connect_wxremit_db()
    cur = con.cursor()
    try:

        sql_str_update = ("UPDATE series_person"
                    + " SET status='%s'" % status
                    + " WHERE url='%s'" % url)
        cur.execute(sql_str_update)
        print(sql_str_update)
        # assert cur.rowcount == 1, 'The number of affected rows not equal to 1'
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

# update_status_by_url('http://www.chehang168.com/index.php?c=index&m=brand&pbid=bd4Tl', 'finished')

if __name__ == '__main__':
    # update_series_status_by_url("http://www.chehang168.com/index.php?c=index&m=series&psid=14081ZU&type=1", "DONE")
    # update_company_status_by_url("0", "0", "http://www.chehang168.com/u/ewxpt_027ppBdpZ", "DONE")

    # a = query_company_url_by_status("TODO")
    # for url in a:
    #     print(url[0])

    a = query_series_person_url_by_status("TODO")
    print(len(a))



    # delete_data_seller('http://www.chehang168.com/u/dtlij_9b0zWKO8y')