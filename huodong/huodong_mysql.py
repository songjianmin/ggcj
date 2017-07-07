#!usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

class use_mysql():

    def __init__(self,hostname="183.131.6.183",portno=4987,username="test_ggcj",
                 pwd="test_ggcj_2013",db="ggcj_gift_statistics"):

        self.conn = pymysql.connect(host=hostname,port=portno,user=username,passwd=pwd)
        self.cur = self.conn.cursor()
        self.cur.execute("USE "+db)

        # print ("数据库连接异常，请检查")

        # print (cur.fetchone()[0])


    def select_sql(self,sql="SELECT amount FROM t_all_new_statistics order by amount DESC "):

        allrang_list = []

        count = self.cur.execute(sql)
        for line in self.cur.fetchall():
            allrang_list.append(line[0])

        # print ("数据库查询失败")
        # print (count)\
        allrang_list = self.cur.fetchall()
        for each in allrang_list:
            print (each)
        # return allrang_list

    def close_sql(self):
        self.conn.close()


if __name__ == "__main__":
    test_mysql = use_mysql()
    test_mysql.select_sql()
