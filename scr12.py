import os
import time
while True:
    os.system('cd {}'.format(os.getcwd()))
    output = os.popen('scrapy crawl mybots').read()
    print(output)

    print("Timer Start 30sec -----------")
    time.sleep(30)
    print("Timer over ------------------")