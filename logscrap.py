from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from xml.etree import ElementTree
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


def tralix_descarga(uuid):
    ser = Service("chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('--safebrowsing-disable-download-protection')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    prefs = {
        'download.prompt_for_download': False,
        'safebrowsing.enabled': True,
        "download.default_directory": r"C:\downloads\\"
    }
    
    capabilities = DesiredCapabilities().CHROME
    chrome_options.add_experimental_option('prefs', prefs)
    capabilities.update(chrome_options.to_capabilities())
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)

    #Set Loging page
    driver.get("")
    a = driver.find_element(By.XPATH,'//*[@id="j_username"]')
    #Type User
    a.send_keys('')
    b = driver.find_element(By.XPATH,'//*[@id="j_password"]')
    #Type pass
    b.send_keys('')
    c = driver.find_element(By.XPATH,'//*[@id="btn-login-accept"]').click()
    d = driver.find_element(By.XPATH,'//*[@id="BaseFormPanel-ok"]/tbody/tr[2]/td[2]/em/button').click()

    ini=138
    for x in range(100):

        pos_uuid='//*[@id="x-auto-{}"]'.format(str(ini))
        pos_sts='//*[@id="x-auto-{}"]'.format(str(ini+1))
        
        hold_place = driver.find_element(By.XPATH,pos_uuid)
        hold_place_text = driver.find_element(By.XPATH,pos_uuid).text

        busca_sts = driver.find_element(By.XPATH,pos_sts).text
        hold_sts = driver.find_element(By.XPATH,pos_sts)
    
        if str(uuid) in str(hold_place_text):
            if 'Válido' in str(busca_sts):
                ActionChains(driver).move_to_element(hold_place).context_click(hold_place).perform()
                download = driver.find_element(By.XPATH,'//*[@id="downloadPrefactura"]').click()
                time.sleep(7)
                return busca_sts
                driver.close()
                break

        if str(uuid) not in str(hold_place_text): 
            ini=ini+11

