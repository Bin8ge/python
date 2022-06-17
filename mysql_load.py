# 导入pymysql方法
import fire
import pymysql
import time

# 连接数据库
config = {'host': 'liangbinbin.top',
          'port': 3306,
          'user': 'root',
          'passwd': '521lijin',
          'charset': 'utf8mb4',
          'local_infile': 1
          }
conn = pymysql.connect(**config)
cur = conn.cursor()

# load_csv函数，参数分别为csv文件路径，表名称，数据库名称
def load_csv():
    # 打开csv文件
    # file = open('F:\qq数据\qq.txt', 'r', encoding='utf-8')
    # # # 读取csv文件第一行字段名，创建表
    # reader = file.readline()
    # b = reader.split('----')
    # print(b)
    # for a in b:
    #     print(a)
    #     exit()
    # colum = ''
    # for a in b:
    #     colum = colum + a + ' varchar(255),'
    # colum = colum[:-1]
    # 编写sql，create_sql负责创建表，data_sql负责导入数据
    # create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8 engine=MyISAM'
    begin = time.time()



    data_sql = "LOAD DATA LOCAL INFILE 'F:/qq数据/qq_1.txt' INTO TABLE qq FIELDS TERMINATED BY '----' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES"

    # 使用数据库
    cur.execute('use %s' % 'qq')
    # 设置编码格式
    # cur.execute('SET NAMES utf8;')
    # cur.execute('SET character_set_connection=utf8;')
    # 执行create_sql，创建表
    # cur.execute(create_sql)
    # 执行data_sql，导入数据
    cur.execute(data_sql)
    # print(cur.fetchall())
    conn.commit()
    # 关闭连接
    conn.close()
    cur.close()

    end = time.time()
    print('time is %d seconds ' % (end - begin))

if __name__ == '__main__':
    fire.Fire()
