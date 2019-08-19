#修改headers部分即可
#本机ip211.161.196.173

import requests
from requests import RequestException
from lxml import etree
from time import sleep
import pymysql
from fake_useragent import UserAgent

conn = pymysql.connect('localhost','root','123456','work')
cur = conn.cursor()
class Boss():
    def __init__(self):
        self.headers = {
            'Host': 'www.zhipin.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': UserAgent().random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'https://www.zhipin.com/web/common/security-check.html?seed=f5%2B8qP6Kiq5wWk3Z01hUU5m2nXTTYacCaoy84d%2BhGlY%3D&name=bf41467a&ts=1565743375942&callbackUrl=%2Fjob_detail%2F%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%26city%3D101190200%26industry%3D%26position%3D',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'sid=sem; __g=sem; __l=%22r=http%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000Ks1acltSXAQu2RTE6AvCDMGXbxHDkL9zcCsK50tJYD4f4S_3ZGLZpK_dSzNUpKSrP3uY5_S3MLtPm10G33FGP0XwMgrhpdQa0XNupNzBB1f-s3AHsm-npfGHsyzbqkvQK84HbsU1CDPYDfjjDHQurt5sst-yg3oa6AVtkgzfAWajROQs7QMxEUGeRjpFOtc2k_ZJP5eChDK0.7D_NR2Ar5Od663rj6t8AGSPticnDpuCcYlxZMLWknwGYqxu68uTkxIW94UvTyj59tqvZut_r11sSXejE33I-XZ1LmIMzseOU9tOZjESyZdS8zEk_lIqMgZwuBmOPtrxj4qhZdvmI-hZ1tT5oeT5oqTSZ1LmIOZj_osSxW9vUtr13T5M_sSLl3IMz1459l3cMYA5gSWS533x5kseOgjlqhZ1vmI-XZx_13x5kseS1jle_5M_ser1jEosSxW9vUtr1udeRlrKYd1ZoOwOZtT5M33IOo9qX1j4enrzEjEvmx5kseS1jle_5M_ser1jEosSxW9vUtr1m_HZW____zI-xQb_4phgT85R_nYQZHb_LUd0.U1Yk0ZDqmhq1Tqpkko60TA-W5HD0IjdBULP1doZA8QgMkPis46KGUHYznjf0u1d-Tv7Bpyfs0ZNG5yF9pywdUAY0TA-b5Hc0mv-b5Hn4r0KVIjYknjDLg1DsnH-xnH0YP-t1PW0k0AVG5H00TMfqnWRk0ANGujY0mhbqnHRdg1Ddr7tznjf0UynqnH6zrHRYnWnYnNtknj0kg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5yFGuadWUfKGuAnqiDFK0ZwdT1YkPjRzPjDkPj0sPjcvnHn1n10zP0Kzug7Y5HDdPWRLPjc3P103n1b0Tv-b5yDvrjbLrj01njKbnjm3PAR0mLPV5Ru7rH61wjKKfWmzfbDznjf0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tzPjnsrHndg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wc100mLFW5Hmznjnz%26word%3Dboss%25E7%259B%25B4%25E8%2581%2598%26ck%3D1287.6.111.361.556.358.354.224%26shh%3Dwww.baidu.com%26sht%3D78000241_20_hao_pg%26bc%3D110101%26us%3D1.173866.2.0.3.1524.0.0&l=%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%E5%8D%8E%E5%93%81%E5%8D%9A%E7%9D%BF8170690%26plan%3DPC-%E4%B8%80%E7%BA%BF-%E5%93%81%E7%89%8C%E8%AF%8D-2C%26unit%3DBOSS%E7%9B%B4%E8%81%98-%E7%94%B5%E8%84%91%E7%89%88%26keyword%3DBOSS%E7%9B%B4%E8%81%98%E7%94%B5%E8%84%91%E7%89%88%22&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF8170690%26plan%3DPC-%25E4%25B8%2580%25E7%25BA%25BF-%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-2C%26unit%3DBOSS%25E7%259B%25B4%25E8%2581%2598-%25E7%2594%25B5%25E8%2584%2591%25E7%2589%2588%26keyword%3DBOSS%25E7%259B%25B4%25E8%2581%2598%25E7%2594%25B5%25E8%2584%2591%25E7%2589%2588; __a=71904334.1565743051..1565743051.1.1.1.1; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1565743053; t=oPAxDqpEwhIHcFas; wt=oPAxDqpEwhIHcFas; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1565743353; __zp_stoken__=ebdfolkdr%2BhiL2K9vW0x3L6dG%2BaGs4qZ6PKPFNBmw3XQx3v1yIbP8%2BMZqJpCQes%2FLB0RwvBq5eJMu9AnHC1dq3NuTQ%3D%3D'
        }
        self.proxy = 'http://59.52.187.118:25537'
        self.proxies = {
            'http':self.proxy,
            'https':self.proxy
        }
    def get_index(self,url):
        try:
            r = requests.get(url,headers=self.headers)
            sleep(2)
            #r = requests.get(url,headers=self.headers,proxies=self.proxies)
            if r.status_code==200:
                print('请求成功')
                #print(r.text) #时而拿得到时而拿不到是因为请求头
                return r.text
            else:
                return None
        except RequestException:
            print("请求错误")
            quit()

    def parse_index(self,r_text):
        html = etree.HTML(r_text)
        content = html.xpath("//li/div[@class='job-primary']")#拿到每条信息的节点
        for c in content:
            try:
                job_title = ''.join(c.xpath(".//div[@class='job-title']/text()"))
            except:
                job_title =''
            try:
                salary = ''.join(c.xpath(".//h3/a/span/text()"))
            except:
                salary =''
            try:
                location = c.xpath("./div[@class='info-primary']/p/text()")[0]
            except:
                location =''
            try:
                experience = c.xpath("./div[@class='info-primary']/p/text()")[1]
            except:
                experience =''
            try:
                education = c.xpath("./div[@class='info-primary']/p/text()")[2]
            except:
                education =''
            try:
                company_name = ''.join(c.xpath(".//div[@class='info-company']/div/h3/a/text()"))
            except:
                company_name =''
            try:
                industry = c.xpath(".//div[@class='company-text']/p//text()")[0]
            except:
                industry =''
            try:
                situation = c.xpath(".//div[@class='company-text']/p//text()")[1]
            except:
                situation =''
            try:
                scale = ''.join(c.xpath("./div[@class='info-company']//p/text()[last()]"))
            except:
                scale =''
            sql = "INSERT INTO boss_11 values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(job_title,salary,location,experience,education,company_name,industry,situation,scale)
            cur.execute(sql)
            conn.commit()

if __name__ == '__main__':
    boss = Boss()
    city_list = [101010100,101020100,101280100,101280600,101210100,101030100,101110100,101190400,101200100,101230200,101250100,101270100,101180100,101040100]
    for city_num in city_list:
        for num in range(1,11): # 每个城市10页
            url = 'https://www.zhipin.com/c{}/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page={}'.format(
                city_num, num)
            try:
                r_text = boss.get_index(url)
                boss.parse_index(r_text)
                print("{}城市的第{}页已存储完毕".format(city_num,num))
            except:
                print("该城市没有这一页")
                break
            sleep(2)
        sleep(3)
        print('这个城市已经存储完毕')
    print('14个城市已全部爬取并存储完毕')
