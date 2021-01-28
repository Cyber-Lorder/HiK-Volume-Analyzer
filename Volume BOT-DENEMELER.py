from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.binance.com/en/markets")
btcbutton = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div[2]/div[1]/div[1]/div/button[3]")
btcbutton.click()
bilgiler = []
"""for i in range(5):
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.PAGE_DOWN)

Burada sayfayı aşşağıya kaydırarak diğer coinlere ulaşmayı denedim.
sayfayı aşşağıya kaydırma çalışıyor fakat bizim işimize yaramadı.	
	"""

for i in range(1, 16):
    coinler = (driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/main/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[""" + str(
            i) + """]/div/div[2]""")).text
    yuzdelik_gunluk = (driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/main/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[""" + str(
            i) + """]/div/div[4]""")).text
    volume_gunluk = (driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/main/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[""" + str(
            i) + """]/div/div[8]""")).text
    deger_usd = (driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/main/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[""" + str(
            i) + """]/div/div[3]/div[2]""")).text

    satir = ["coinler=", coinler, "24Saatlik HACİM", volume_gunluk, "fiyat", deger_usd]
    bilgiler.append(satir)

with open('binanceVOLUMEdeneme.csv', 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\n')
    w.writerow(bilgiler)  # Bilgileri CSV formatında yazdır.
pass
driver.close()  # Otomatik Chrome'u kapat.
