#!/usr/bin/python

#coding=utf-8

import pymysql

connection=pymysql.connect(

host="172.16.1.18",

port=3306,

user="root",

password="123456",

db="banma_dev",

charset="utf8")

try:

    with connection.cursor() as cursor:

        sql='select*from tongye_wechat_home'

        cout=cursor.execute(sql)

        print("数量:"+str(cout))

        for row in cursor.fetchall():

            print("编号："+str(row[0])+" 12"+str(row[1])+"    性别："+str(row[2]))

        connection.commit()

finally:

        connection.close()