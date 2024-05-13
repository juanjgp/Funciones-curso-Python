from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By

url_pc_componentes = "https://www.pccomponentes.com/biostar-geforce-gtx-1050ti-extreme-gaming-4gb-gddr5"
url_coolmod = "https://www.coolmod.com/msi-geforce-rtx-3060-ti-gaming-x-lhr-8gb-gddr6-vga-reacondicionado/"

session = HTMLSession()

def pc_componentes(url_pc_componentes,session):
    while True:
        r = session.get(url_pc_componentes)
        buy_zone = r.html.find("#pdp-add-to-cart")
        if len(buy_zone) > 0:
            print("HAY STOCK!!")
            break
        else:
            print("Sigue sin haber stock :(")
        sleep(30)

product_page = session.get(url_coolmod)
found = product_page.html.find("#productbuybutton1")

if len(found) > 0:
    driver = webdriver.Firefox()
    driver.get(url_coolmod)
    sleep(2)
    driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline").click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, "close-icon").click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, "fa-twitter").click()