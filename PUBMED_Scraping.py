from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from re import search
import time

with open('Scraping_Sonuclari.csv', 'w', encoding="utf-8") as file:
    file.write("BASLIK; ACIKLAMA \n")

servis = Service("C:/Users/merta/Desktop/PythonKurs/geckodriver.exe")
driver = webdriver.Firefox(service=servis)

def fonksiyon():
    web_sitesi = "https://pubmed.ncbi.nlm.nih.gov/"
    driver.get(web_sitesi)
    driver.maximize_window()
    time.sleep(3)
    tiklama = driver.find_element(By.XPATH, '//*[@id="id_term"]')
    tiklama.send_keys(program.get())
    time.sleep(3)
    tiklama.send_keys(Keys.ENTER)
    time.sleep(3)

    for i in range(5):
        time.sleep(1)
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[9]/div[2]/section/div[2]/button'))).click()
    time.sleep(3)

    baslik = driver.find_elements(By.CSS_SELECTOR, 'html body main#search-page.search-page div.inner-wrap div#search-results.search-results section.search-results-list div.search-results-chunks div.search-results-chunk.results-chunk article.full-docsum div.docsum-wrap div.docsum-content a.docsum-title')
    aciklama = driver.find_elements(By.CSS_SELECTOR, 'html body main#search-page.search-page div.inner-wrap div#search-results.search-results section.search-results-list div.search-results-chunks div.search-results-chunk.results-chunk article.full-docsum div.docsum-wrap div.docsum-content div.docsum-snippet')
    
    with open('Scraping_Sonuclari.csv', 'a', encoding="utf-8") as file:
        for n in range(len(baslik)):
            file.write(baslik[n].text + ";" + aciklama[n].text + "\n")
    
    driver.quit()
    ekran.quit()

ekran = Tk()
ekran.title("PUBMED Scraping Uygulaması")
ekran.geometry("400x100")
search = Label(ekran, text="Aranacak Kelime:", font='times 16 bold')
search.place(x=10, y=10)
program = Entry(ekran)
program.place(x=200, y=15)
arama_butonu = Button(ekran, text="Ara", command=fonksiyon, width=15, bg='green')
arama_butonu.place(x=150, y=60)
ekran.mainloop()