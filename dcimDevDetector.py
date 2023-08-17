from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import sys
import time
import re

user = "usernmu"
passwd = "passwordmu"
url = "https://dcim.domain.tld/dcim/device-types/"

def aplikasi():
    print("\n\\\    /ttt==============\\")
    print("|=====|    DCIM Audit    ==|>")
    print("//    \\============ttt==/")
    print("1. Tampilkan Jumlah Device Types")
    print("2. Tampilkan Semua Detail Device Types")
    print("3. Tampilkan Detail Setiap Instances")
    inputan = int(input("Silahkan pilih menu diatas: "))
    
    def menu3():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        chrome_driver = '/chromedriver_win32'
        driver = webdriver.Chrome(chrome_driver, chrome_options=options)
        driver.get(url)
        time.sleep(1)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[3]')
        lapo.send_keys(user)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[4]')
        lapo.send_keys(passwd)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/button')
        lapo.click()
        time.sleep(5)
        
        td2s = driver.find_elements(By.XPATH, '//td[2]')
        tttt = []
        td7s = driver.find_elements(By.XPATH, '//td[7]')
        ttt = []
        
        for t2 in td2s:
            macul2 = t2.find_element(By.TAG_NAME, 'a')
            auau = macul2.text
            tttt.append(auau)
        
        for t7 in td7s:
            macul = t7.find_element(By.TAG_NAME, 'a')
            link = macul.get_attribute('href')    
            ttt.append(link)
                
        b = 0
        for tek, tektek in zip(ttt, tttt):
            a = 0    
            print("\n\n",tektek)
            
            driver.get(tek)
            halaman = driver.page_source
            nyekrop = BeautifulSoup(halaman, "html.parser")
            awak = nyekrop.select_one('table > tbody')
            target = awak.find_all("tr")    
            
            for row in target:
                td1 = row.select_one('td:nth-of-type(2)')
                td2 = row.select_one('td:nth-of-type(3)')
                td7 = row.select_one('td:nth-of-type(11)')
                if td1 and td2 and td7:
                    a += 1
                    b += 1
                    val1 = td1.get_text()
                    val2 = td2.get_text()
                    val3 = td7.get_text()
                    teks1 = re.sub(r'\s{2,}',' ',val1)
                    teks2 = re.sub(r'\s{2,}',' ',val2)
                    print("====================")
                    print("Nama   :",teks1)
                    print("Status : ",teks2)
                    print("IP     : ",val3)
            print("====================")
            print(" Jumlah Instances:", a)
        print("\n/=================================================\\")
        print("| Total Keseluruhan Instances: ", b, "bossqueee :V")
        print("\=================================================/\n")
            
    def menu2():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        chrome_driver = '/chromedriver_win32'
        driver = webdriver.Chrome(chrome_driver, chrome_options=options)
        driver.get(url)
        time.sleep(1)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[3]')
        lapo.send_keys(user)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[4]')
        lapo.send_keys(passwd)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/button')
        lapo.click()
        time.sleep(5)
        
        halaman = driver.page_source
        nyekrop = BeautifulSoup(halaman, "html.parser")
        awak = nyekrop.select_one('table > tbody')
        target = awak.find_all("tr")
        
        for row in target:
            td1 = row.select_one('td:nth-of-type(2)')
            td2 = row.select_one('td:nth-of-type(3)')
            td7 = row.select_one('td:nth-of-type(7)')
            if td1 and td2 and td7:
                val1 = td1.get_text()
                val2 = td2.get_text()
                val3 = td7.get_text()
                print("Device Type: ", val1)
                print("Manufacture: ", val2)
                print("Instances  : ", val3)
    
    def menu1():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        chrome_driver = '/chromedriver_win32'
        driver = webdriver.Chrome(chrome_driver, chrome_options=options)
        driver.get(url)
        time.sleep(1)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[3]')
        lapo.send_keys(user)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[4]')
        lapo.send_keys(passwd)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/button')
        lapo.click()
        time.sleep(5)
        
        halaman = driver.page_source
        nyekrop = BeautifulSoup(halaman, "html.parser")
        target = nyekrop.find_all("span", class_='badge bg-secondary')
        for tulisan in target:
            print("\nJumlah Device-Type DCIM:",tulisan.text,"\n")
            
    if inputan == 1:
        try:
            sc = requests.get(url)
            if sc.status_code == 200:
                menu1()
        except requests.exceptions.ConnectionError:
            print("Tidak bisa konek, coba cek jaringan dan vpn ya bosss")
    elif inputan == 2:
        try:
            sc = requests.get(url)
            if sc.status_code == 200:
                menu2()
        except requests.exceptions.ConnectionError:
            print("Tidak bisa konek, coba cek jaringan dan vpn ya bosss")
    elif inputan == 3:
        try:
            sc = requests.get(url)
            if sc.status_code == 200:
                menu3()
        except requests.exceptions.ConnectionError:
            print("Tidak bisa konek, coba cek jaringan dan vpn ya bosss")
    else:
        print("Maaf karena inputan tidak jelas, maka program auto close ya bosqueee")
        sys.exit()
        
aplikasi()