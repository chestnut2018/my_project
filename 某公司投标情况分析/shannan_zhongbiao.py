import requests
from lxml import etree
import time
import re
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
    每个链接都是个post请求，
    __doPostBack方法的格式为： __doPostBack(eventTarget,eventArgument)
　　        eventTarget:是要触发的服务器控件的客户端ID
　　　　　  eventArgument:参数
    这个两个值在后台可以通过下边方法得到：
    Request["__EVENTTARGET"] ：获取得到引发页面PostBack的控件ID
    Request["__EVENTARGUMENT"]： 获取参数。
'''
class Zhongbiao():
    def __init__(self):
        # 请求头，代理放在初始化里
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }
        # self.proxy = 'http://113.64.197.15:31469'
        # self.proxies = {
        #     'http': self.proxy,
        #     'https': self.proxy
        # }
    def get_index(self, url):
        data = {
        'txtZbr':'上海山南勘测设计有限公司',
        'btnSearch':'查询',
        '__VIEWSTATE':'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',
    '__VIEWSTATEGENERATOR':'DF0C86B1',
    '__EVENTVALIDATION':"/wEdACWd8hynU2k90IlIPiFx3aRmYFVDskWoBzzIrjzhjMGivogI9Z3UT/Np2jYuM7RA6V0ao6o3sRSHcU5sf0XALLa6A18+64hmj2eWnRPDW4+ryCcBMyY+qjA1ILbkB2FsZTx9Crw1xhUrT0E3/kAmOFugSEbR4F4+APsGZUeEFoAWebqKz6BbAEmBmG4HqNVJizPICRVKEKSQGLkVVlwN8YDPY+hv0FGmXYLYLs870l7gTJ3AHD63+4oeB+Ybs0yx6bezf6ezZYHW9PnV8gr0GSwxqJFi/ODgwBuBWFR1hNYkWI7U3Vc0WZ+wxclqyPFfzmPkILkKejWkjx6dQ/Apk3HyYDdyYMdmueZO9G+32xcfonJVtGz6Fn5fSb329wpJcKDym1WM+tuQFAQhY3+AbRLTnALvOh+tWKGkJjMWZUySvEJ5fFYhh0kwIhiTKrHeHVHCZiumaro7TsTworhjqiSotlbCk61yHgkq1hzr/l2oujEMD0YtxKUu81vRTJLdWw8gDeS2CPxC3zNevwye2lvOJttITsL3ldBFABFwpoeyWaEqX98l6odgwQMGJM3ORvhHHVIInUrzz1CVM2aBrvIe4wo8r+UDy1cfCTiPR1Z81EBIoIXPm1wvnetu0tVB9bUXetMwQsQrenIdg26mFm4+sSzuIKWEz3J7wCt2CYfbaC2BT6o+AJsIt7rIqeg88jKCWw8e2RW4sSXaZ41WgCOvBQrkruhtdIdSP+9EWtWg75VAvfcPBwT2CyX5SWqeUuXo4IhN3ye+ITHxICzEbGkTcDfKUoTdA0c6n7d2juDNVyFxXs0="
    }
        resp = requests.post(url, data=data, headers=self.headers) #proxies=self.proxies,vertify=False
        return resp.text

    def get_each_page(self,url,i,j):
        # i第几页  j第几个标
        # url = 'https://www.ciac.sh.cn/XmZtbbaWeb/gsqk/ZbjgGkList.aspx'
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url)
        input = browser.find_element_by_id('txtZbr')
        input.send_keys('上海山南勘测设计有限公司')
        browser.find_element_by_id('btnSearch').click()
        browser.find_element_by_xpath('//*[@id="gvZbjgGkList"]/tbody/tr[14]/td/table/tbody/tr/td[{}]/a'.format(i)).click()
        try:
            browser.find_element_by_id('gvZbjgGkList_lbXmmc_{}'.format(j)).click()
        except:
            print("最后一页索引已完结")
        else:
            global r_text
            r_text = browser.page_source
        finally:
            browser.quit()
        return r_text

    def parse_each_page(self,r_text):
        html1 = etree.HTML(r_text)
        href_list = html1.xpath("//table[@id='gvZbjgGkList']//tr/td[2]/a/@href")  #每页的12个标
        # print(href)
        res_href_list = href_list[:-1] #将最后换页的js去除
        return res_href_list

    def request_detail(self,href):
        eventtargrt_id = re.search('\$ct(.*)\$lbXmmc',href).group(1)
        # print(eventtargrt_id)
        data = {
        "__EVENTTARGET":"gvZbjgGkList$ct{}$lbXmmc".format(eventtargrt_id),
        "__VIEWSTATE": "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",
        "__VIEWSTATEGENERATOR": "DF0C86B1",
        "__EVENTVALIDATION": "/wEdACUzolRc5+XHmB15vhg3Im1+YFVDskWoBzzIrjzhjMGivogI9Z3UT/Np2jYuM7RA6V0ao6o3sRSHcU5sf0XALLa6A18+64hmj2eWnRPDW4+ryCcBMyY+qjA1ILbkB2FsZTx9Crw1xhUrT0E3/kAmOFugSEbR4F4+APsGZUeEFoAWebqKz6BbAEmBmG4HqNVJizPICRVKEKSQGLkVVlwN8YDPY+hv0FGmXYLYLs870l7gTJ3AHD63+4oeB+Ybs0yx6bezf6ezZYHW9PnV8gr0GSwxqJFi/ODgwBuBWFR1hNYkWI7U3Vc0WZ+wxclqyPFfzmPkILkKejWkjx6dQ/Apk3HyYDdyYMdmueZO9G+32xcfonJVtGz6Fn5fSb329wpJcKDym1WM+tuQFAQhY3+AbRLTnALvOh+tWKGkJjMWZUySvEJ5fFYhh0kwIhiTKrHeHVHCZiumaro7TsTworhjqiSotlbCk61yHgkq1hzr/l2oujEMD0YtxKUu81vRTJLdWw8gDeS2CPxC3zNevwye2lvOJttITsL3ldBFABFwpoeyWaEqX98l6odgwQMGJM3ORvhHHVIInUrzz1CVM2aBrvIe4wo8r+UDy1cfCTiPR1Z81EBIoIXPm1wvnetu0tVB9bUXetMwQsQrenIdg26mFm4+sSzuIKWEz3J7wCt2CYfbaC2BT6o+AJsIt7rIqeg88jKCWw8e2RW4sSXaZ41WgCOvBQrkruhtdIdSP+9EWtWg75VAvfcPBwT2CyX5SWqeUuXo4IhN3ye+ITHxICzEbGkTQ2b8KW/EeXpQg75cKSQmK1PW7vw=",
        "txtZbr": "上海山南勘测设计有限公司"
    }
        url = 'https://www.ciac.sh.cn/XmZtbbaWeb/gsqk/ZbjgGkList.aspx'
        resp = requests.post(url, data=data, headers=self.headers)
        # print(resp.text)
        return resp.text
    def parse_detail(self,each_text):
        html1 = etree.HTML(each_text)
        zb_type = ''.join(html1.xpath("//table[@class='table01']//tr[2]/td[4]/span/text()"))
        biaoming = ''.join(html1.xpath("//table[@class='table01']//tr[3]/td[2]/span/text()"))
        zhaobiaoren = ''.join(html1.xpath("//table[@class='table01']//tr[4]/td[2]/span/text()"))
        daili = ''.join(html1.xpath("//table[@class='table01']//tr[5]/td[2]/span/text()"))
        zhongbiaoren = ''.join(html1.xpath("//table[@class='table01']//tr[6]/td[2]/span/text()"))
        zbj = ' '.join(html1.xpath("//table[@class='table01']//tr[7]/td[2]/span/text()"))
        zb_time = ''.join(html1.xpath("//table[@class='table01']//tr[7]/td[4]/span/text()"))
        pb =  '、'.join(html1.xpath("//table[@class='table01']//tr[8]/td[2]/span/text()"))
        # print(type,biaoming,zhaobiaoren,daili,zhongbiaoren,zbj,time,pb)
        return zb_type,biaoming,zhaobiaoren,daili,zhongbiaoren,zbj,zb_time,pb

    def save_detail(self,zb_type,biaoming,zhaobiaoren,daili,zhongbiaoren,zbj,zb_time,pb):
        self.connect = pymysql.connect('localhost','root','123456','zhuli')
        self.cursor = self.connect.cursor()
        sql = "INSERT INTO zb_imformation (zb_type,biaoming,zhaobiaoren,daili,zhongbiaoren,zbj,zb_time,pb)\
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(zb_type,biaoming,zhaobiaoren,daili,zhongbiaoren,zbj,zb_time,pb)
        self.cursor.execute(sql)
        self.connect.commit()
        print('数据存入完毕...')
if __name__ == '__main__':
    zb = Zhongbiao()
    url = 'https://www.ciac.sh.cn/XmZtbbaWeb/gsqk/ZbjgGkList.aspx'
    for i in range(1,12): #第1到11页
        time.sleep(1)
        if i == 1:
            r_text = zb.get_index(url)
            res_href_list = zb.parse_each_page(r_text)
            for href in res_href_list:
               each_text = zb.request_detail(href)
               zb_type, biaoming, zhaobiaoren, daili, zhongbiaoren, zbj, zb_time, pb = zb.parse_detail(each_text)
               zb.save_detail(zb_type,biaoming,zhaobiaoren,daili,zhongbiaoren,zbj,zb_time,pb)
        else:
            for j in range(12):
                time.sleep(0.5)
                each_text = zb.get_each_page(url,i,j)
                res = zb.parse_detail(each_text)
                # print(res)
                zb_type = res[0]
                biaoming = res[1]
                zhaobiaoren = res[2]
                daili = res[3]
                zhongbiaoren = res[4]
                zbj = res[5]
                zb_time = res[6]
                pb = res[7]
                zb.save_detail(zb_type, biaoming, zhaobiaoren, daili, zhongbiaoren, zbj, zb_time, pb)

