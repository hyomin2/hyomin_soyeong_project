# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import time
from datetime import datetime, timezone

class MyScrapyPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.create_table()

    # 데이터베이스에 저장하고자하는 코드를 이곳에 입력하면 된다.
    def process_item(self, item, spider):
        # print("- - - - - - - - - - - - - - - - - - - -")
        self.storeDB(item)

        # print("Timer Start 10sec -----------")
        # time.sleep(600)
        # print("Timer over ------------------")

        return item


    def storeDB(self, item):
        # 각 아이템을 테이블에 저장
        now = datetime.now()
        f = '%Y-%m-%d %H:%M:%S'
        now2 = now.strftime(f)
        sql = "insert into stock_review(now_time, amount, price, max_price, min_price, s_code) values (%s, %s, %s, %s, %s, %s);"
        val = (now2, item.get('amount'), item.get('price'), item.get('max_price'), item.get('min_price'), item.get('s_code'))
        self.cur.execute(sql, val)
        self.conn.commit()
        print("DB insert Success !!!!!!")


    # 데이터베이스를 사용하기 위한 연동 작업을 이곳에서 하자
    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', port=3307, password='', db='python_data', charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected !!!")

    def create_table(self):
        sql_1 = "DROP TABLE IF EXISTS stock_review"
        self.cur.execute(sql_1)

        sql_2 = """
        CREATE TABLE IF NOT EXISTS stock_review(
            id INT AUTO_INCREMENT PRIMARY KEY,
            now_time VARCHAR(100),
            amount VARCHAR(100),
            price VARCHAR(100),
            max_price VARCHAR(100),
            min_price VARCHAR(100),
            s_code VARCHAR(100)
            )
        """
        self.cur.execute(sql_2)


