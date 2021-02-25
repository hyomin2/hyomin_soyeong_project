import os
import time

os.system('cd {}'.format(os.getcwd()))
output = os.popen('pip install pymysql').read()
print(output)

os.system('cd {}'.format(os.getcwd()))
output = os.popen('conda install -c scrapinghub scrapy').read()
print(output)

while True:
    os.system('cd {}'.format(os.getcwd()))
    output = os.popen('scrapy crawl mybots').read()
    print(output)

    print("Timer Start 30sec -----------")
    time.sleep(30)
    print("Timer over ------------------")
