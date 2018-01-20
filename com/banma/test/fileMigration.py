#!/usr/bin/env python
# coding=utf-8

# 文件迁移   test prod   win10 centos6 172.16.1.17
import MySQLdb

def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    db = MySQLdb.connect("172.16.1.18","root","123456","banma_dev")
    print('连接上了!')
    return db

def createtable(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果存在表Sutdent先删除
    cursor.execute("DROP TABLE IF EXISTS Student")
    sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""

    # 创建Sutdent表
    cursor.execute(sql)

def insertdb(db,datas):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO tongye_file_owner(file_id,owner_id) VALUES (%s, %s)"

    try:
        # 执行sql语句
        for data in datas:
            # print(data)
            print(sql,(str(data[0]),data[1]))
            cursor.execute(sql,(str(data[0]),data[1]))
            # 提交到数据库执行
            db.commit()
    except:
        # Rollback in case there is any error
        print('插入数据失败!')
        db.rollback()

def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句

    sql0 = 'select QR_code , dealer_id  from tongye_dealer_shop where QR_code is not NULL and QR_code !=""'
    sql1 = 'select business_licence , dealer_id  from tongye_dealer where business_licence is not NULL and business_licence !=""'
    sql2 = 'select business_permit , dealer_id  from tongye_dealer where business_permit is not NULL and business_permit !=""'
    sql3 = 'select business_protocol , dealer_id  from tongye_dealer where business_protocol is not NULL and business_protocol !=""'
    sql4 = 'select t.attachment_local , o.dealer_id   from tongye_order_confirmation  t JOIN `order` o on t.order_id = o.id where t.attachment_local is not NULL and t.attachment_local !=""'

    sql5 = 'select oss_qr , dealer_id  from tongye_dealer_shop where oss_qr is not NULL and oss_qr !=""'
    sql6 = 'select oss_licence , dealer_id  from tongye_dealer where oss_licence is not NULL and oss_licence !=""'
    sql7 = 'select oss_permit , dealer_id  from tongye_dealer where oss_permit is not NULL and oss_permit !=""'
    sql8 = 'select oss_protocol , dealer_id  from tongye_dealer where oss_protocol is not NULL and oss_protocol !=""'
    sql9 = 'select t.attachment, o.dealer_id   from tongye_order_confirmation  t JOIN `order` o on t.order_id = o.id where t.attachment is not NULL and t.attachment !=""'

    sql = [sql0, sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9]

    try:
        results = []
        # 文件迁移   test  range(10) local oss  prod range(5) local
        for i in range(10):
            # 执行SQL语句
            print(sql[i])
            cursor.execute(sql[i])
            # 获取所有记录列表
            results += cursor.fetchall()
        # for row in results:
        #     fileId = row[0]
        #     dealerId = row[1]
            # 打印结果
            # print( "fileId: %s, dealerId: %s" % \
            #     (fileId,dealerId))
        print(len(results))
        return results
    except:
        print("Error: unable to fecth data")

def deletedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
    except:
        print('删除数据失败!')
        # 发生错误时回滚
        db.rollback()

def updatedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print('更新数据失败!')
        # 发生错误时回滚
        db.rollback()

def closedb(db):
    db.close()

def main():
    db = connectdb()    # 连接MySQL数据库

    # createtable(db)     # 创建表
    # insertdb(db)        # 插入数据
    # print('\n插入数据后:')
    # querydb(db)
    # deletedb(db)        # 删除数据
    # print('\n删除数据后:')
    # querydb(db)
    # updatedb(db)        # 更新数据
    # print('\n更新数据后:')
    results=querydb(db)
    # for i,result in enumerate(results):
    #     print(str(i),':',result[0],result[1])
    insertdb(db,results)

    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    main()