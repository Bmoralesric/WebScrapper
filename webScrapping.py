from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import f1_score
import time
import pandas as pd
import numpy as np
from datetime import datetime
import math 
import re
import random
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from textblob import TextBlob
import pickle
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PIL import Image
import requests

#class Retailer():
#     def __init__(self,retailer):
#         self.retailer =retailer

#     def urlRetailer(self,retailer):
#         if retailer == 'Selecto Easy Shop':
#             retailerPage = "https://www.selectoseasyshop.com"
#         elif retailer == 'WalMart':
#             retailerPage = "https://www.walmart.com"
#         elif retailer == 'Walgreens':
#             retailerPage = 'https://www.walgreens.com/'
#         return retailerPage
class Functions():
    def __init__(self):
        pass

    def check_digit_ean(self, codigo):
        while len(codigo)<12:
            codigo = "0"+codigo
        primer_suma = 0
        if len(codigo) == 12:
            try:
                for i in range(len(codigo)):
                    j = -1*(2*i + 1)
                    # Selecionamos la posicin en el codigo
                    primer_suma = primer_suma + int(codigo[j])
                    if j == -1*(len(codigo)-1):
                        break
                primer_suma = primer_suma*3
                segunda_suma = 0
                for i in range(1,len(codigo)):
                    j = -1*(2*i)
                    # Selecionamos la posicin en el codigo
                    segunda_suma = segunda_suma + int(codigo[j])
                    if j == -1*(len(codigo)):
                        break
                suma_total = primer_suma + segunda_suma
                round_ten = int(suma_total/10)*10 + 10 
                x = round_ten - suma_total
                if x == 10:
                    x = 0
                else:
                    x = x
                new_codigo = codigo + str(x)
            except KeyError as E:
                pass
        else:
            new_codigo = codigo 
        # por lo tanto el numero que falta sería x, debemos concatenar al ultimo del código
        # print(new_codigo)
        return new_codigo

    def CompleteBC(self, codigo):
        while len(codigo)<14:
            codigo = "0"+codigo
        return codigo

    def Get_adjectives(self, text):
        blob = TextBlob(text)
        return [ word for (word,tag) in blob.tags if tag.startswith("JJ")] 
    
    def make_clickable(self, val):
        return '<a href="{}">{}</a>'.format(val,val)

    def Chedraui(self):
        path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"
        driver =webdriver.Chrome(path)
        driver.get('https://www.chedraui.com.mx/')
        search = driver.find_element_by_id('searchBox')
        search.click()
        search.send_keys('2529300170')
        search.send_keys(Keys.RETURN)
        pageMatch = BeautifulSoup(driver.page_source,'lxml')
        details = driver.find_element_by_xpath('//*[@id="productTabs"]/div[1]/div[2]/div/div/div/div/div/p[1]')
        details = details.text
        sku = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[2]/div[2]/div[2]/span[2]')
        sku = sku.text
        precio = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[3]/div[3]/div/div/div[1]/p')
        precio = precio.text
        imageUrl = pageMatch.find("div",attrs={"class":'zoomImgMask'})
        tipo = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[3]/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/span')
        tipo = tipo.text
        marca = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[3]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[2]/span/a')
        marca = marca.text
        print(details)
        print(sku)
        print(precio)
        print(tipo)
        print(marca)
        print('--')
    def Walmart(self):
        path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"
        driver =webdriver.Chrome(path)
        driver.get('https://super.walmart.com.mx/')
        search = driver.find_element_by_xpath('//*[@id="headerId"]/div/div[1]/div[2]/div/div/div/input')
        time.sleep(4)
        search.click()
        search.send_keys('00750105536750')
        search.send_keys(Keys.RETURN)
        time.sleep(9)
        found = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div/div[3]/div[2]/div/div[2]/div/div[1]')
        found.click()
        time.sleep(5)
        details = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[3]/div/div[2]/div/p[3]')
        details = details.text
        time.sleep(6)
        upc = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[2]/div[2]/div[2]/p')
        upc = upc.text
        time.sleep(2)
        precio = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[2]/div[2]/div[3]/h4')
        url_product = driver.current_url
        print(details)
        print(upc)
        print(precio)
        print(url_product)
        print('---')
    def Comer(self):
        path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"
        driver =webdriver.Chrome(path)
        driver.get('https://super.walmart.com.mx/')
        search = driver.find_element_by_xpath('//*[@id="headerId"]/div/div[1]/div[2]/div/div/div/input')
        time.sleep(4)
        search.click()
        search.send_keys('00750105536750')
        search.send_keys(Keys.RETURN)

class htmlComposition():

    def __init__(self) :
        pass

    def urlRetailer(self,retailer):
        if retailer == 'SELECTOS':
            retailerPage = "https://www.selectoseasyshop.com"
            return retailerPage
        elif retailer == 'WALMART':
            retailerPage = "https://www.walmart.com"
            return retailerPage
        elif retailer == 'WALGREENS':
            retailerPage = 'https://www.walgreens.com/'
            return retailerPage

    def webSearcher(self, retailer):
        if retailer == 'Selecto Easy Shop':
            htmlSearcher = "fp-input-search"
            
        return htmlSearcher

    def firstMatch (self,retailer):
        if retailer == 'Selecto Easy Shop':
            matchUrl = 'div.fp-item-name a[href]'

        return matchUrl

    def itemDescHtml (self,retailer):
        if retailer =='Selecto Easy Shop':
            itemDescription="fp-page-header fp-page-title"
        return itemDescription

    def itemDetailsHtml (self,retailer):
        if retailer == 'Selecto Easy Shop':
            itemDet = "fp-item-description-content"
        return itemDet

    def itemSkuHtml (self,retailer):
        if retailer == 'Selecto Easy Shop':
            itemSkuUpc = "fp-margin-top fp-item-upc"
        return itemSkuUpc

    def itemSkuHtml2 (self,retailer):
        if retailer == 'Selecto Easy Shop':
            itemSkuUpc = "fp-margin-top fp-item-upc fp-item-upc-no-desc"
        return itemSkuUpc

    def itemNotFound (self,retailer):
        if retailer == 'Selecto Easy Shop':
            itmNotFound = "fp-product-not-found fp-not-found"
        return itmNotFound

    def imageHtml (self,retailer):
        if retailer == 'Selecto Easy Shop':
            imgHtml = 'fp-item-image fp-item-image-large'
        return imgHtml

    def imageNotFound(self,retailer):
        if retailer == 'Selecto Easy Shop':
            imageUrlNot = 'https://ipcdn.freshop.com/resize?url=https://images.freshop.com/5554875/09c1c58d54ae3e309c8cfce88eb1a764_large.png&width=512&type=webp&quality=80'
        return imageUrlNot
    
    def check_digit_ean(self, codigo):
        while len(codigo)<12:
            codigo = "0"+codigo
        primer_suma = 0
        if len(codigo) == 12:
            try:
                for i in range(len(codigo)):
                    j = -1*(2*i + 1)
                    # Selecionamos la posicin en el codigo
                    primer_suma = primer_suma + int(codigo[j])
                    if j == -1*(len(codigo)-1):
                        break
                primer_suma = primer_suma*3
                segunda_suma = 0
                for i in range(1,len(codigo)):
                    j = -1*(2*i)
                    # Selecionamos la posicin en el codigo
                    segunda_suma = segunda_suma + int(codigo[j])
                    if j == -1*(len(codigo)):
                        break
                suma_total = primer_suma + segunda_suma
                round_ten = int(suma_total/10)*10 + 10 
                x = round_ten - suma_total
                if x == 10:
                    x = 0
                else:
                    x = x
                new_codigo = codigo + str(x)
            except KeyError as E:
                pass
        else:
            new_codigo = codigo 
        # por lo tanto el numero que falta sería x, debemos concatenar al ultimo del código
        # print(new_codigo)
        return new_codigo
    
    def UPCdigit(self,x):
        #add leading zeros
        while len(x)<11:
            x = "0"+x
        #calculate sums for odd and even digits
        sum_odd = 0
        sum_even = 0
        for i in range(1,len(x),2):
            sum_even += int(x[i])
        for i in range(0,len(x),2):
            sum_odd += int(x[i])

        #calculate modulo
        m = (sum_odd*3+sum_even) % 10

        #determine check_digit
        if m == 0:
            check_digit = 0
        else:
            check_digit = 10-m

        #construct upc
        upc = x+str(check_digit)
        
        return upc

def Main(retailer):
    start_time = datetime.now()
    #scrappingRetailer = Retailer(retailer)
    htmlAttr = htmlComposition()
    urlRetailer = htmlAttr.urlRetailer(retailer)
    pd.set_option('display.max_colwidth', 0)
    listSku=[]
    listDescription=[]
    listDetails = []
    listImagen = []
    listItemsNotFound = []
    listurl = []
    pattern = r"[^a-zA-Z0-9]"
    dfItems = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\ITEMS PR.xlsx')
    #dfItems['Calculo de digito verif'] = dfItems['BARCODE'].apply(lambda x: len(str(x)))
    #dfItems['Calculo de digito verif'] = dfItems['BARCODE'].apply(lambda x: htmlAttr.check_digit_ean(str(x)))
    #dfItems['BARCODE'] = dfItems['BAR CODE']
    #dfItems['Número_digitos'] = dfItems['BAR CODE'].apply(lambda x: len(str(math.trunc(x))))
    dfItems['New_Codigo'] = dfItems['BARCODE'].apply(lambda x: htmlAttr.check_digit_ean(str(math.trunc(x))))
    
    #dfItems['Número_digitos2'] = dfItems['New_Codigo'].apply(lambda x: len(str(x)))
    listItems = dfItems['BARCODE'].tolist()
    path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"
    driver =webdriver.Chrome(path)
    driver.get(urlRetailer)
    time.sleep(5)
    for item in listItems:
        htmlSearcher = htmlAttr.webSearcher(retailer)
        firstMatch = htmlAttr.firstMatch(retailer)
        itemDescHtml = htmlAttr.itemDescHtml(retailer)
        itemDetailsHtml = htmlAttr.itemDetailsHtml(retailer)
        itemSkuHtml = htmlAttr.itemSkuHtml(retailer)
        itemSku2Html = htmlAttr.itemSkuHtml2(retailer)
        itemImage = htmlAttr.imageHtml(retailer)
        imageUrlNot = htmlAttr.imageNotFound(retailer)
        search = driver.find_element_by_name(htmlSearcher)
        search.send_keys(int(item))
        search.send_keys(Keys.RETURN)
        randomSleep = np.random.choice([8,9,10])
        time.sleep(randomSleep)
        pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
        productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})
        if productNotFound:
            search = driver.find_element_by_name(htmlSearcher)
            search.send_keys(Keys.CONTROL+"a")
            search.send_keys(Keys.DELETE)
            listItemsNotFound.append(item)
            continue
        linkItem = pageSearchResults.select(firstMatch)
        linksItem =[str(linkItem['href']) for linkItem in linkItem]
        linkItemFirst = linksItem[0]
        urlMatch = urlRetailer + linkItemFirst
        driver.get(urlMatch)
        url_product = driver.current_url
        randomSleep = np.random.choice([8,9,10])
        time.sleep(randomSleep)
        pageMatch = BeautifulSoup(driver.page_source,'lxml')

        itemDesc = pageMatch.find("div",attrs={"class":itemDescHtml})
        itemDetails = pageMatch.find('div',attrs={"class":itemDetailsHtml})
        itemSku =pageMatch.find("div",attrs={"class":itemSkuHtml})
        imageUrl = pageMatch.find("div",attrs={"class":itemImage})
        imageUrl = imageUrl.find('img')
        imageUrl = imageUrl['src']
        if imageUrl == imageUrlNot:
            listItemsNotFound.append(item)
            continue
        imageUrl = '<img src="'+ imageUrl + '" width="80" >'
        if not itemSku:
            itemSku =pageMatch.find("div",attrs={"class":itemSku2Html})
        itemSku = itemSku.text
        itemSku = int("".join(c for c in itemSku if c.isdigit()))
        listurl.append(url_product)
        listSku.append(itemSku)
        listDescription.append(itemDesc.text)
        listDetails.append(itemDetails.text)
        listImagen.append(imageUrl)
        df=pd.DataFrame(list(zip(listSku,listDescription,listDetails,listImagen, listurl)),columns=['SKU','DESCRIPTION','DETAILS','IMAGE', 'PRODUCT LINK'])
        df.to_html('test_html.html', escape=False)

        ###Agregado para la busqueda en google

    if listItemsNotFound:
        imageUrlNot = htmlAttr.imageNotFound(retailer)
        print(listItemsNotFound)
        dfDescItemsNotF = dfItems[dfItems['BAR CODE'].isin(listItemsNotFound)]
        dfDescItemsNotF[' ITEM DESCRIPTION'] = dfDescItemsNotF[' ITEM DESCRIPTION'].apply(lambda x: re.sub(pattern, ' ', x))
        dfDescItemsNotF[' ITEM DESCRIPTION'] = dfDescItemsNotF[' ITEM DESCRIPTION'].apply(lambda x: re.sub(r'[0-9]', '', x))
        listBarcodesNotFound  = dfDescItemsNotF['BAR CODE'].tolist()
        listDescsNotFound = dfDescItemsNotF[' ITEM DESCRIPTION'].tolist()
        driver.get("https://www.google.com.mx/imghp?hl=es-419&tab=ri&ogbl")
        time.sleep(6)

        for barcode,descripcion in zip(listBarcodesNotFound,listDescsNotFound):
            search = driver.find_element_by_name("q")
            search.send_keys(descripcion)
            search.send_keys(Keys.RETURN)
            randomSleep = np.random.choice([6,9])
            time.sleep(randomSleep)
            pageMatch = BeautifulSoup(driver.page_source,'lxml')
            imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
            imageUrl = imageUrl.find('img')
            imageUrl = imageUrl['src']
            imageUrl = '<img src="'+ imageUrl + '" width="80" >'
            if imageUrl == imageUrlNot:
                continue
            randomSleep = np.random.choice([6,9])
            time.sleep(randomSleep)
            listSku.append(barcode)
            listDescription.append(descripcion)
            listDetails.append('Found On Google')
            listImagen.append(imageUrl)
            df=pd.DataFrame(list(zip(listSku,listDescription,listDetails,listImagen)),columns=['SKU','DESCRIPTION','DETAILS','IMAGE'])
            df.to_html('test_html.html', escape=False)
            search = driver.find_element_by_name("q")
            search.send_keys(Keys.CONTROL+"a")
            search.send_keys(Keys.DELETE)
    end_time = datetime.now()
    executionTime = (end_time - start_time)
    print('Finalizado en ', executionTime)

class Scrapper(object):
    #############vARIABLES GLOBLALES###################
    log = None #Modelo a guardar log regresion
    vectorizer = None # CountVectorizer

    def __init__(self):
        pass
    
    def Scraping(self, dfItems):
        #####Llamado de las clases a utilizar
        fun = Functions()
        htmlAttr = htmlComposition()

        #Variables globales
        pattern = r"[^a-zA-Z0-9]"

        #Lista de Retails donde buscar
        retails = ['SELECTOS', 'WALMART', 'WALGREENS']

        #Lectura del archivo y path del driver chrome
        #dfItems = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\ITEMS SELECTOS2.xlsx')
        path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"

        #Cálculo del dígito verificador y limpieza de la descripción
        dfItems['New_Codigo'] = dfItems['BARCODE'].apply(lambda x: fun.check_digit_ean(str(math.trunc(x))))
        #dfItems['BARCODE'] = dfItems['BARCODE'].apply(lambda x: fun.CompleteBC(str(math.trunc(x))))
        dfItems['ITEM DESCRIPTION'] = dfItems['ITEM DESCRIPTION'].apply(lambda x: re.sub(pattern, ' ', x))
        #dfItems['ITM_DESC'] = dfItems['ITM_DESC'].apply(lambda x: re.sub(r'[0-9]', '', x))
        driver =webdriver.Chrome(path)

        #Df a listas para utilizar en for
        #retailers = dfItems['RETAILER'].tolist()
        listItems = dfItems['BARCODE'].tolist()
        listItemsCV = dfItems['New_Codigo'].tolist()
        listDesc = dfItems['ITEM DESCRIPTION'].tolist()

        #Listas vacías para completar en FOR
        listSku=[]
        listDescription=[]
        listDetails = []
        listImagen = []
        listurl = []
        listImagenBarcode = []
        listurlBarcode = []
        listImagenBarcodeOri = []
        listurlBarcodeOri = []

        for item, itemcv, descripcion in zip(listItems, listItemsCV, listDesc):

            start_time = datetime.now()
            urlRetailer = htmlAttr.urlRetailer(retails[0])
            start_time = datetime.now()
            pd.set_option('display.max_colwidth', 0)
            driver.get(urlRetailer)
            time.sleep(6)
            retailer = 'Selecto Easy Shop'

            #Se utiliza la clase de la page SELECTO
            htmlSearcher = htmlAttr.webSearcher(retailer)
            firstMatch = htmlAttr.firstMatch(retailer)
            itemDetailsHtml = htmlAttr.itemDetailsHtml(retailer)
            itemSkuHtml = htmlAttr.itemSkuHtml(retailer)
            itemSku2Html = htmlAttr.itemSkuHtml2(retailer)
            itemImage = htmlAttr.imageHtml(retailer)
            imageUrlNot = htmlAttr.imageNotFound(retailer)
            search = driver.find_element_by_name(htmlSearcher)

            #Busca el producto con barcode a 13 digitos
            search.send_keys(itemcv)
            search.send_keys(Keys.RETURN)
            randomSleep = np.random.choice([8,9,10])
            time.sleep(randomSleep)
            pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
            productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})

            #Sino encuentra BARCODE a 13 digitos lo busca como viene (formato sin ceros)
            if productNotFound:
                search = driver.find_element_by_name(htmlSearcher)
                search.send_keys(Keys.CONTROL+"a")
                search.send_keys(Keys.DELETE)
                randomSleep = np.random.choice([8,9,10])
                time.sleep(randomSleep)
                search.send_keys(item)
                search.send_keys(Keys.RETURN)
                #urlRetailer = htmlAttr.urlRetailer(retails[1])
                #driver.get(urlRetailer)
                pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})
                time.sleep(6)
                #Sino lo encuentra con ninguno de los 2 formatos del BARCODE, busca en el siguiente retailer "Walmart"
                # if productNotFound:
                #     urlRetailer = htmlAttr.urlRetailer(retails[1])
                #     driver.get(urlRetailer)
                #     time.sleep(5)
                    #Sino lo encuentra en el anterior retailer busca en el siguiente "WALGREENS"
                    #if productNotFound:
                    #   urlRetailer = htmlAttr.urlRetailer(retails[2])
                    #   driver.get(urlRetailer)
                    #   time.sleep(5)
                #Sino lo encuentra en ninguno de los retailers, hace la búsqueda en google y trae la información
                if productNotFound:
                    driver.get("https://www.google.com.pr/imghp?hl=es-419&tab=ri&ogbl")
                    time.sleep(2)
                    search = driver.find_element_by_name("q")
                    search.send_keys(descripcion)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([8,9,10])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    linksearch = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                    imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                    imageUrl = imageUrl.find('img')
                    imageUrl = imageUrl['src']
                    imageUrlDes = '<img src="'+ imageUrl + '" width="80" >'
                    if imageUrl == imageUrlNot:
                        continue
                    randomSleep = np.random.choice([4,6])
                    time.sleep(randomSleep)

                    #Busqueda por Barcode 13 digitos
                    search = driver.find_element_by_name("q")
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(itemcv)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([6,7,8])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuentra valores regresa not found
                    if Notfound != None :
                        linksearchbar13 = 'Not Found'
                        imageUrlbar13 = 'Not Found'
                    elif Notfound == None:
                        linksearchbar13 = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbar13 = '<img src="'+ imageUrl + '" width="80" >'

                    #Busqueda por Barcode Original
                    search = driver.find_element_by_xpath('//*[@id="REsRA"]')
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(item)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([4,5])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound2 = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuientra valores regresa not found
                    if Notfound2 != None :
                        linksearchbarOri = 'Not Found'
                        imageUrlbarOri = 'Not Found'
                    elif Notfound2 == None:
                        linksearchbarOri = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbarOri = '<img src="'+ imageUrl + '" width="80" >'

                    #Recoleccion de información en las listas
                    listurl.append(linksearch)
                    listSku.append(item)
                    listDescription.append(descripcion)
                    listDetails.append(' Web Found On Google')
                    listImagen.append(imageUrlDes)
                    listImagenBarcode.append(imageUrlbar13)
                    listurlBarcode.append(linksearchbar13)
                    listImagenBarcodeOri.append(imageUrlbarOri)
                    listurlBarcodeOri.append(linksearchbarOri)
                    df=pd.DataFrame(list(zip(listSku,listDescription,listDetails,listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS','IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                    df = df.sort_values(by=['DETAILS'])
                    df.to_html('test_html.html', escape=False)
                    continue

            #Si encuentra el producto en el primer retailer trae la información
            linkItem = pageSearchResults.select(firstMatch)
            time.sleep(4)
            linksItem =[str(linkItem['href']) for linkItem in linkItem]
            linkItemFirst = linksItem[0]
            urlMatch = urlRetailer + linkItemFirst
            driver.get(urlMatch)
            url_product = driver.current_url
            randomSleep = np.random.choice([8,9,10])
            time.sleep(randomSleep)

            #Busqueda de elementos en la page cuando encuentra el producto
            pageMatch = BeautifulSoup(driver.page_source,'lxml')
            itemDesc = driver.find_element_by_xpath('//*[@id="page-title"]/div[1]/div/div/h1')
            itemDetails = pageMatch.find('div',attrs={"class":itemDetailsHtml})
            itemSku =pageMatch.find("div",attrs={"class":itemSkuHtml})
            imageUrl = pageMatch.find("div",attrs={"class":itemImage})
            imageUrl = imageUrl.find('img')
            imageUrl = imageUrl['src']
            # if imageUrl == imageUrlNot:
            #     listItemsNotFound.append(item)
            #     continue
            imageUrl = '<img src="'+ imageUrl + '" width="80" >'
            if not itemSku:
                itemSku =pageMatch.find("div",attrs={"class":itemSku2Html})
            itemSku = itemSku.text
            itemSku = int("".join(c for c in itemSku if c.isdigit()))
            linksearchbar13 = 'No search'
            imageUrlbar13 = 'No search'
            linksearchbarOri = 'No search'
            imageUrlbarOri = 'No search'
            randomSleep = np.random.choice([5,6,7])
            time.sleep(randomSleep)

            #Se hace append a las listas antes creadas para ir capturando la información
            listurl.append(url_product)
            listSku.append(itemSku)
            listDescription.append(itemDesc.text)
            listDetails.append(itemDetails.text.replace('\n', ''))
            listImagen.append(imageUrl)
            listImagenBarcode.append(imageUrlbar13)
            listurlBarcode.append(linksearchbar13)
            listImagenBarcodeOri.append(imageUrlbarOri)
            listurlBarcodeOri.append(linksearchbarOri)

            #Se genera un DF con las listas para después generar un html con la información
            df = pd.DataFrame(list(zip(listSku,listDescription,listDetails,listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,linksearchbarOri)),columns=['SKU','DESCRIPTION','DETAILS','IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
            df = df.sort_values(by=['DETAILS'])
            #df['PRODUCT LINK(DESCRIPTION)'].apply(lambda x: fun.make_clickable(x))
            #df.style.format({'PRODUCT LINK(DESCRIPTION)': fun.make_clickable})
            df.to_html('test_html.html', escape=False)
        dfcsv = df.to_csv('ItemsSearchPR.csv', index=False)
        driver.close()

    def ScrapingPredict(self, dfItems):
                #####Llamado de las clases a utilizar
        fun = Functions()
        htmlAttr = htmlComposition()

        #Variables globales
        pattern = r"[^a-zA-Z0-9]"

        #Lista de Retails donde buscar
        retails = ['SELECTOS', 'WALMART', 'WALGREENS']

        #Lectura del archivo y path del driver chrome
        #dfItems = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\ITEMS SELECTOS2.xlsx')
        path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"

        #Cálculo del dígito verificador y limpieza de la descripción
        dfItems['New_Codigo'] = dfItems['BARCODE'].apply(lambda x: fun.check_digit_ean(str(math.trunc(x))))
        #dfItems['BARCODE'] = dfItems['BARCODE'].apply(lambda x: fun.CompleteBC(str(math.trunc(x))))
        dfItems['ITEM DESCRIPTION'] = dfItems['ITEM DESCRIPTION'].apply(lambda x: re.sub(pattern, ' ', x))
        #dfItems['ITM_DESC'] = dfItems['ITM_DESC'].apply(lambda x: re.sub(r'[0-9]', '', x))
        driver =webdriver.Chrome(path)

        ##Df a listas para utilizar en for
        #retailers = dfItems['RETAILER'].tolist()
        listItems = dfItems['BARCODE'].tolist()
        listItemsCV = dfItems['New_Codigo'].tolist()
        listDesc = dfItems['ITEM DESCRIPTION'].tolist()

        ##Listas vacías para completar en FOR
        listSku=[]
        listDescription=[]
        listDetails = []
        listImagen = []
        listurl = []
        listImagenBarcode = []
        listurlBarcode = []
        listImagenBarcodeOri = []
        listurlBarcodeOri = []

        for item, itemcv, descripcion in zip(listItems, listItemsCV, listDesc):
            start_time = datetime.now()
            #urlRetailer = htmlAttr.urlRetailer(retails[0])
            #Condición para tomar en cuenta el retailer del excel
            # if retail in retails:
            #     pd.set_option('display.max_colwidth', 0)
            #     driver.get(urlRetailer)
            #     time.sleep(5)
            # else:
            ##Si no cumple la condición empieza a buscar en orden de los reta ilers agregados
            urlRetailer = htmlAttr.urlRetailer(retails[0])
            start_time = datetime.now()
            pd.set_option('display.max_colwidth', 0)
            driver.get(urlRetailer)
            time.sleep(6)
            retailer = 'Selecto Easy Shop'

            #Se utiliza la clase de la page SELECTO
            htmlSearcher = htmlAttr.webSearcher(retailer)
            firstMatch = htmlAttr.firstMatch(retailer)
            itemDetailsHtml = htmlAttr.itemDetailsHtml(retailer)
            itemSkuHtml = htmlAttr.itemSkuHtml(retailer)
            itemSku2Html = htmlAttr.itemSkuHtml2(retailer)
            itemImage = htmlAttr.imageHtml(retailer)
            imageUrlNot = htmlAttr.imageNotFound(retailer)
            search = driver.find_element_by_name(htmlSearcher)

            #Busca el producto con barcode a 13 digitos
            search.send_keys(itemcv)
            search.send_keys(Keys.RETURN)
            randomSleep = np.random.choice([8,9,10])
            time.sleep(randomSleep)
            pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
            productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})

            #Sino encuentra BARCODE a 13 digitos lo busca como viene (formato sin ceros)
            if productNotFound:
                search = driver.find_element_by_name(htmlSearcher)
                search.send_keys(Keys.CONTROL+"a")
                search.send_keys(Keys.DELETE)
                randomSleep = np.random.choice([8,9,10])
                time.sleep(randomSleep)
                search.send_keys(item)
                search.send_keys(Keys.RETURN)
                #urlRetailer = htmlAttr.urlRetailer(retails[1])
                #driver.get(urlRetailer)
                pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})
                time.sleep(6)

                #Sino lo encuentra con ninguno de los 2 formatos del BARCODE, busca en el siguiente retailer "Walmart"
                # if productNotFound:
                #     urlRetailer = htmlAttr.urlRetailer(retails[1])
                #     driver.get(urlRetailer)
                #     time.sleep(5)
                    #Sino lo encuentra en el anterior retailer busca en el siguiente "WALGREENS"
                    #if productNotFound:
                    #   urlRetailer = htmlAttr.urlRetailer(retails[2])
                    #   driver.get(urlRetailer)
                    #   time.sleep(5)
                #Sino lo encuentra en ninguno de los retailers, hace la búsqueda en google y trae la información
                if productNotFound:
                    driver.get("https://www.google.com.pr/imghp?hl=es-419&tab=ri&ogbl")
                    time.sleep(2)
                    search = driver.find_element_by_name("q")
                    search.send_keys(descripcion)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([8,9,10])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    linksearch = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                    imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                    imageUrl = imageUrl.find('img')
                    imageUrl = imageUrl['src']
                    imageUrlDes = '<img src="'+ imageUrl + '" width="80" >'
                    if imageUrl == imageUrlNot:
                        continue
                    randomSleep = np.random.choice([4,6])
                    time.sleep(randomSleep)

                    #Busqueda por Barcode 13 digitos
                    search = driver.find_element_by_name("q")
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(itemcv)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([6,7,8])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuentra valores regresa not found
                    if Notfound != None :
                        linksearchbar13 = 'Not Found'
                        imageUrlbar13 = 'Not Found'
                    elif Notfound == None:
                        linksearchbar13 = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbar13 = '<img src="'+ imageUrl + '" width="80" >'

                    #Busqueda por Barcode Original
                    search = driver.find_element_by_xpath('//*[@id="REsRA"]')
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(item)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([4,5])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound2 = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuientra valores regresa not found
                    if Notfound2 != None :
                        linksearchbarOri = 'Not Found'
                        imageUrlbarOri = 'Not Found'
                    elif Notfound2 == None:
                        linksearchbarOri = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbarOri = '<img src="'+ imageUrl + '" width="80" >'

                    #Recoleccion de información en las listas
                    listurl.append(linksearch)
                    listSku.append(item)
                    listDescription.append(descripcion)
                    listDetails.append(' Web Found On Google')
                    listImagen.append(imageUrlDes)
                    listImagenBarcode.append(imageUrlbar13)
                    listurlBarcode.append(linksearchbar13)
                    listImagenBarcodeOri.append(imageUrlbarOri)
                    listurlBarcodeOri.append(linksearchbarOri)
                    df=pd.DataFrame(list(zip(listSku,listDescription,listDetails,listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS','IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                    df = df.sort_values(by=['DETAILS'])
                    df.to_html('test_html.html', escape=False)
                    continue

            #Si encuentra el producto en el primer retailer trae la información
            linkItem = pageSearchResults.select(firstMatch)
            time.sleep(4)
            linksItem =[str(linkItem['href']) for linkItem in linkItem]
            linkItemFirst = linksItem[0]
            urlMatch = urlRetailer + linkItemFirst
            driver.get(urlMatch)
            url_product = driver.current_url
            randomSleep = np.random.choice([8,9,10])
            time.sleep(randomSleep)

            #Busqueda de elementos en la page cuando encuentra el producto
            pageMatch = BeautifulSoup(driver.page_source,'lxml')
            itemDesc = driver.find_element_by_xpath('//*[@id="page-title"]/div[1]/div/div/h1')
            itemDetails = pageMatch.find('div',attrs={"class":itemDetailsHtml})
            itemSku =pageMatch.find("div",attrs={"class":itemSkuHtml})
            imageUrl = pageMatch.find("div",attrs={"class":itemImage})
            imageUrl = imageUrl.find('img')
            imageUrl = imageUrl['src']
            # if imageUrl == imageUrlNot:
            #     listItemsNotFound.append(item)
            #     continue
            imageUrl = '<img src="'+ imageUrl + '" width="80" >'
            if not itemSku:
                itemSku =pageMatch.find("div",attrs={"class":itemSku2Html})
            itemSku = itemSku.text
            itemSku = int("".join(c for c in itemSku if c.isdigit()))
            linksearchbar13 = 'No search'
            imageUrlbar13 = 'No search'
            linksearchbarOri = 'No search'
            imageUrlbarOri = 'No search'
            randomSleep = np.random.choice([5,6,7])
            time.sleep(randomSleep)

            #Se hace append a las listas antes creadas para ir capturando la información
            listurl.append(url_product)
            listSku.append(itemSku)
            listDescription.append(itemDesc.text)
            listDetails.append(itemDetails.text.replace('\n', ''))
            listImagen.append(imageUrl)
            listImagenBarcode.append(imageUrlbar13)
            listurlBarcode.append(linksearchbar13)
            listImagenBarcodeOri.append(imageUrlbarOri)
            listurlBarcodeOri.append(linksearchbarOri)

            #Se genera un DF con las listas para después generar un html con la información
            df = pd.DataFrame(list(zip(listSku,listDescription,listDetails,listImagen, listurl, listImagenBarcode,listurlBarcode, listImagenBarcodeOri, linksearchbarOri)), columns=['SKU','DESCRIPTION','DETAILS','IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
            df = df.sort_values(by=['DETAILS'])
            #df['PRODUCT LINK(DESCRIPTION)'].apply(lambda x: fun.make_clickable(x))
            #df.style.format({'PRODUCT LINK(DESCRIPTION)': fun.make_clickable})
        driver.close()
        itemsprueba = df['DESCRIPTION'].tolist()
        
        #Se carga el modelo guardado y el vectorizador
        log, vectorizer = self.Extractmodel()

        #Se hace hace una limpieza a los detalles que se trajeron el scraping y se sacan las palabras adjetivas que pueden proporcionar más información al producto
        df['DETAILS'] = df['DETAILS'].apply(lambda x: re.sub(r'[0-9]', '', str(x)))
        Adjetives = df['DETAILS'].apply(lambda x: fun.Get_adjectives(str(x)))
        Adjetives = Adjetives.apply(lambda x: " ".join(x))

        #Se junta la descripción normal más los adjetivos
        DetailsAdj = df['DESCRIPTION'] + Adjetives
        df.insert(3, 'DESCRIPTION + ADJETIVES DETAILS', DetailsAdj)
        itemspruebaadj = df['DESCRIPTION + ADJETIVES DETAILS'].tolist()
        new_testadj = vectorizer.transform(itemspruebaadj)
        newresultadj = log.predict(new_testadj)

        #Se cargan los modelos generados con los datos insertados
        new_test = vectorizer.transform(itemsprueba)
        newresult = log.predict(new_test)
        df['Prediction'] = newresult
        df['Prediction with Adjetives'] = newresultadj

        df.to_csv('Prueba_Predict_Scraping.csv', index=False)
        df.to_html('test_html_predict_and_scraping.html', escape=False)

    def ProductCategoryTrain(self):
        #Se cargan archivos de entrenamiento y prueba
        items = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\training.xlsx')
        #items = items.iloc[0:20000]
        prueba = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\ITEMS SELECTOS.xlsx')
        items = items.rename(columns={"ITEM DESCRIPTIONS": "Desc", "PRODUCT GROUP": "PC"})
        items['Desc'] = items['Desc'].apply(lambda x: str(x).replace(",", " "))   
        #adjprueba = pd.read_csv(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\ItemsSearchPR.csv')
        #adjprueba['Details'] = adjprueba['Details'].apply(lambda x: re.sub(r'[0-9]', '', str(x)))
        #adjprueba['Adjectives'] = adjprueba['Details'].apply(lambda x: fun.Get_adjectives(str(x)))
        #items['PC'] = items['PC'].apply(lambda x: re.sub(r'[0-9]', '', x))
        itemsprueba = prueba['ITEM DESCRIPTION'].tolist()
        #labels = items.PC.unique().tolist()

        #Pasamos las columnas a utilizar a variables iundependientes
        X = items.Desc
        y = items.PC

        #Generamos un arreglo con cada una de las variables
        X = X.to_numpy()
        y = y.to_numpy()

        #Generamos el train split con .8 de train y semilla 42
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

        #Vectorizamos la información
        vectorizer = CountVectorizer()
        X_train_vectors = vectorizer.fit_transform(X_train)
        X_test_vectors = vectorizer.transform(X_test)
        
        #Cargamos los items de prueba a analizar
        new_test = vectorizer.transform(itemsprueba)

        #### SVC Model
        # clf = svm.SVC(kernel='linear')
        # clf.fit(X_train_vectors, y_train)
        # clf.predict(new_test)

        ##### Decision Tree Model
        # tree_model = DecisionTreeClassifier()
        # tree_model.fit(X_train_vectors, y_train)
        # tree_model.predict(new_test)
        
        #### Logistic Regression model
        log = LogisticRegression(solver='liblinear')
        log.fit(X_train_vectors, y_train)
        log.predict(new_test)

        #Medidos la precisión de cada modelo para determinar el más eficiente
        # new_result = log.predict(new_test)
        # prueba['Prediction'] = new_result
        # prueba.to_csv('Prueba_Predict.csv', index=False)

        # print(clf.score(X_test_vectors, y_test))
        # print(tree_model.score(X_test_vectors, y_test))
        print(log.score(X_test_vectors, y_test))
        self.log = log
        self.vectorizer = vectorizer
        return self.log, self.vectorizer

    def ProductCategoryPredict(self, prueba):
        fun = Functions()
        #Se cargan el archivo a prueba a predecir
        #prueba = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\ITEMS PR - SIN CREAR.xlsx')
        adjprueba = pd.read_csv(r'C:\Users\mobr1001\Documents\WebScrapper\Prueba_Predict_Scraping.csv')
        itemsprueba2 = adjprueba['DESCRIPTION'].tolist()
        adjprueba['DETAILS'] = adjprueba['DETAILS'].apply(lambda x: re.sub(r'[0-9]', '', str(x)))
        Adjetives = adjprueba['DETAILS'].apply(lambda x: fun.Get_adjectives(str(x)))
        Adjetives = Adjetives.apply(lambda x: " ".join(x))
        DetailsAdj = adjprueba['DESCRIPTION'] + Adjetives
        adjprueba.insert(3, 'DESCRIPTION + ADJETIVES DETAILS', DetailsAdj)
        itemspruebaadj = adjprueba['DESCRIPTION + ADJETIVES DETAILS'].tolist()

        #Se cargan los modelos generados con los datos insertados
        log, vectorizer = self.ExtractmodelSG()
        itemsprueba = prueba['ITEM DESCRIPTION'].tolist()

        new_test = vectorizer.transform(itemsprueba)
        new_test2 = vectorizer.transform(itemsprueba2)
        new_testadj = vectorizer.transform(itemspruebaadj)
        
        newresult2 = log.predict(new_test2)
        newresultadj = log.predict(new_testadj)
        newresult = log.predict(new_test)
        
        proba = log.predict_proba(new_test)
        proba = pd.DataFrame([max(x) for x in proba], columns = ['Probability Super Group'])

        prueba['Prediction Super Group'] = newresult
        prueba['Prediction Probability Super Group'] = proba
        #prueba = prueba.loc[prueba['Prediction Probability Super Group'] >= .70]

        adjprueba['Prediction'] = newresult2
        adjprueba['Prediction with Adjetives'] = newresultadj
        
        logPG, vectorizerPG =self.ExtractmodelPG()
        new_test2 = vectorizerPG.transform(itemsprueba)
        newresultPG = logPG.predict(new_test2)
        probaPG = logPG.predict_proba(new_test)
        probaPG = pd.DataFrame([max(x) for x in probaPG], columns = ['Probability Product Group'])

        prueba['Prediction Product Group'] = newresultPG
        prueba['Prediction Probability Product Group'] = probaPG

        prueba = prueba.loc[prueba['Prediction Probability Super Group'] >= .70]
        prueba = prueba.loc[prueba['Prediction Probability Product Group'] >= .70]


        prueba = prueba.to_csv('Prueba_Predict.csv', index=False)
        return prueba

    def Savemodel(self):
        #Se guarda el modelo de regresión y el CountVectorizer
        with open("C:\\Users\\mobr1001\\Documents\\WebScrapper\\Models\\Productgroup_classifier.pkl", 'wb') as f:
            pickle.dump(self.log, f)
        with open("C:\\Users\\mobr1001\\Documents\\WebScrapper\\Models\\Productgroup_vectorizer.pkl", 'wb') as f:
            pickle.dump(self.vectorizer, f)

    def ExtractmodelSG(self):
        #Se carga el modelo de regresión y el CountVectorizer
        with open("C:\\Users\\mobr1001\\Documents\\WebScrapper\\Models\\category_classifierSG.pkl", 'rb') as f:
            log = pickle.load(f)
        with open("C:\\Users\\mobr1001\\Documents\\WebScrapper\\Models\\category_vectorizerSG.pkl", 'rb') as f:
            vectorizer = pickle.load(f)
        return log, vectorizer

    def ExtractmodelPG(self):
        with open("C:\\Users\\mobr1001\\Documents\\WebScrapper\\Models\\Productgroup_classifier.pkl", 'rb') as f:
            log = pickle.load(f)
        with open("C:\\Users\\mobr1001\\Documents\\WebScrapper\\Models\\Productgroup_vectorizer.pkl", 'rb') as f:
            vectorizer = pickle.load(f)
        return log, vectorizer

# class MyApp(QtWidgets.QMainWindow):
#     def __init__(self):
#         S = Scrapper()
#         QtWidgets.QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)
#         self.Selecto = QtWidgets.QCheckBox('S')
#         self.pushButton1.clicked.connect(self.getCSV)  #Aquí van los botones
#         self.pushButton2.clicked.connect(self.ScrapPredict)
#         self.pushButton3.clicked.connect(self.Scrap)
#         self.pushButton4.clicked.connect(self.Predict)

#     #Aquí van las nuevas funciones
#     #Esta función abre el archivo CSV    
#     def getCSV(self):
#         filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
#         if filePath != "":
#             print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
#             self.df = pd.read_excel(str(filePath))
#     def Scrap(self):
#         S = Scrapper()
#         dfItems = S.Scraping(self.df)
#     def Predict(self, dfItems):
#         S = Scrapper()
#         S.ProductCategoryPredict(self.df)
#     def ScrapPredict(self):
        S = Scrapper()
        S.ScrapingPredict(self.df)


path_gui = os.getcwd()
path_gui_style = path_gui.replace('\\', '/')
style = ''' QWidget{{
    background-image: url("{path_gui_style}/GUI_WorkingFiles/fondo2.jpg");
}} '''.format(path_gui_style = path_gui_style)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 624)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(150, 20, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background-color: rgb(24, 177, 118);")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.getCSV)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(150, 310, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("background-color: rgb(71, 152, 41);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.ScrapPredict)

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(150, 490, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("background-color: rgb(50, 90, 36);")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.clicked.connect(self.Predict)

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(150, 400, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color: rgb(50, 90, 36);")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.clicked.connect(self.Scrap)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 130, 131, 21))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 130, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(57, 216, 218);")
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(160, 210, 111, 20))
        self.checkBox.setStyleSheet("color: rgb(57, 216, 218);")
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 180, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(57, 216, 218);")
        self.label_2.setObjectName("label_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 240, 111, 20))
        self.checkBox_2.setStyleSheet("color: rgb(57, 216, 218);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(280, 210, 171, 20))
        self.checkBox_3.setStyleSheet("color: rgb(57, 216, 218);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(280, 240, 151, 20))
        self.checkBox_4.setStyleSheet("color: rgb(57, 216, 218);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(-10, -10, 571, 651))
        self.lineEdit.setStyleSheet(style)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.raise_()
        self.pushButton1.raise_()
        self.pushButton2.raise_()
        self.pushButton4.raise_()
        self.pushButton3.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.checkBox.raise_()
        self.label_2.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scrapper V1"))
        MainWindow.setWindowIcon(QtGui.QIcon("{path_gui_style}/GUI_WorkingFiles/nielsen-IQ.png".format(path_gui_style = path_gui_style)))
        self.pushButton1.setText(_translate("MainWindow", "Import Items File"))
        self.pushButton2.setText(_translate("MainWindow", "Scraping and Predict SG and PG"))
        self.pushButton4.setText(_translate("MainWindow", "Predict Super Group and Product Group"))
        self.pushButton3.setText(_translate("MainWindow", "Start Scraping"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Puerto Rico"))
        self.comboBox.setItemText(1, _translate("MainWindow", "México"))
        self.label.setText(_translate("MainWindow", "Select Country "))
        self.checkBox.setText(_translate("MainWindow", "SELECTOS"))
        self.label_2.setText(_translate("MainWindow", "Select Retailers to Search:"))
        self.checkBox_2.setText(_translate("MainWindow", "WALMART SUPER"))
        self.checkBox_3.setText(_translate("MainWindow", "CHEDRAUI"))
        self.checkBox_4.setText(_translate("MainWindow", "LA COMER"))

    def getCSV(self, MainWindow):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_excel(str(filePath))

    def Scrap(self):
        pais = self.comboBox.currentText()
        start_time = datetime.now()
        #S = Scrapper()
        dfItems = self.df
        selectos = self.checkBox.isChecked()
        walmart = self.checkBox_2.isChecked()
        chedraui = self.checkBox_3.isChecked()
        lacomer = self.checkBox_4.isChecked()
                #####Llamado de las clases a utilizar
        fun = Functions()
        htmlAttr = htmlComposition()

        #Variables globales
        pattern = r"[^a-zA-Z0-9]"

        #Lista de Retails donde buscar
        retails = ['SELECTOS', 'WALMART', 'WALGREENS']

        #Lectura del archivo y path del driver chrome
        #dfItems = pd.read_excel(r'C:\Users\mobr1001\Documents\WebScrapper\Archivos\ITEMS SELECTOS2.xlsx')
        path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"

        #Cálculo del dígito verificador y limpieza de la descripción
        dfItems['Codigo WM'] = dfItems['BARCODE'].apply(lambda x: fun.CompleteBC(str(math.trunc(x))))
        dfItems['New_Codigo'] = dfItems['BARCODE'].apply(lambda x: fun.check_digit_ean(str(math.trunc(x))))
        #dfItems['BARCODE'] = dfItems['BARCODE'].apply(lambda x: fun.CompleteBC(str(math.trunc(x))))
        dfItems['ITEM DESCRIPTION'] = dfItems['ITEM DESCRIPTION'].apply(lambda x: re.sub(pattern, ' ', x))
        #dfItems['ITM_DESC'] = dfItems['ITM_DESC'].apply(lambda x: re.sub(r'[0-9]', '', x))
        driver =webdriver.Chrome(path)

        #Df a listas para utilizar en for
        #retailers = dfItems['RETAILER'].tolist()
        listItems = dfItems['BARCODE'].tolist()
        listItemsCV = dfItems['New_Codigo'].tolist()
        listItemsWM = dfItems['Codigo WM'].tolist()
        listDesc = dfItems['ITEM DESCRIPTION'].tolist()

        #Listas vacías para completar en FOR
        listSku=[]
        listDescription=[]
        listDetails = []
        listImagen = []
        listurl = []
        listImagenBarcode = []
        listurlBarcode = []
        listImagenBarcodeOri = []
        listurlBarcodeOri = []
        listprice = []
        listtype = []
        listmarca = []
        listwebsite = []

        for item, itemcv, descripcion, itemwm in zip(listItems, listItemsCV, listDesc, listItemsWM):
                
                #Búsqueda para la página de Selectos
                if selectos == True:
                    start_time = datetime.now()
                    urlRetailer = htmlAttr.urlRetailer(retails[0])
                    pd.set_option('display.max_colwidth', 0)
                    driver.get(urlRetailer)
                    time.sleep(6)
                    retailer = 'Selecto Easy Shop'

                    #Se utiliza la clase de la page SELECTO
                    htmlSearcher = htmlAttr.webSearcher(retailer)
                    firstMatch = htmlAttr.firstMatch(retailer)                                                                                                                                                                                                  
                    itemDetailsHtml = htmlAttr.itemDetailsHtml(retailer)
                    itemSkuHtml = htmlAttr.itemSkuHtml(retailer)
                    itemSku2Html = htmlAttr.itemSkuHtml2(retailer)
                    itemImage = htmlAttr.imageHtml(retailer)
                    imageUrlNot = htmlAttr.imageNotFound(retailer)
                    search = driver.find_element_by_name(htmlSearcher)

                    #Busca el producto con barcode a 13 digitos
                    search.send_keys(itemcv)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([8,9,10])
                    time.sleep(randomSleep)
                    pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                    productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})
                    #Sino encuentra BARCODE a 13 digitos lo busca como viene (formato sin ceros)
                    if productNotFound != None:
                        pass
                        # search = driver.find_element_by_name(htmlSearcher)
                        # search.send_keys(Keys.CONTROL+"a")
                        # search.send_keys(Keys.DELETE)
                        # randomSleep = np.random.choice([8,9,10])
                        # time.sleep(randomSleep)
                        # search.send_keys(item)
                        # search.send_keys(Keys.RETURN)
                        # pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                        # productNotFound = pageSearchResults.find("div",attrs={"class":"fp-product-not-found fp-not-found"})
                        # time.sleep(6)

                        #Sino encuentra el producto con ninguno de los barcodes, lo busca en google Puerto Rico por descripción
                        # if productNotFound:
                        #     driver.get("https://www.google.com.pr/imghp?hl=es-419&tab=ri&ogbl")
                        #     time.sleep(2)
                        #     search = driver.find_element_by_name("q")
                        #     search.send_keys(descripcion)
                        #     search.send_keys(Keys.RETURN)
                        #     randomSleep = np.random.choice([8,9,10])
                        #     time.sleep(randomSleep)
                        #     pageMatch = BeautifulSoup(driver.page_source,'lxml')
                        #     linksearch = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        #     imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        #     imageUrl = imageUrl.find('img')
                        #     imageUrl = imageUrl['src']
                        #     imageUrlDes = '<img src="'+ imageUrl + '" width="80" >'
                        #     if imageUrl == imageUrlNot:
                        #         continue
                        #     randomSleep = np.random.choice([4,6])
                        #     time.sleep(randomSleep)

                        #     #Busqueda por Barcode 13 digitos
                        #     search = driver.find_element_by_name("q")
                        #     search.send_keys(Keys.CONTROL+"a")
                        #     search.send_keys(Keys.DELETE)
                        #     search.send_keys(itemcv)
                        #     search.send_keys(Keys.RETURN)
                        #     randomSleep = np.random.choice([6,7,8])
                        #     time.sleep(randomSleep)
                        #     pageMatch = BeautifulSoup(driver.page_source,'lxml')
                        #     Notfound = pageMatch.find("div",attrs={"class":"eUYiW"})

                        #     #Si no encuentra valores regresa not found
                        #     if Notfound != None :
                        #         linksearchbar13 = 'Not Found'
                        #         imageUrlbar13 = 'Not Found'
                        #     elif Notfound == None:
                        #         linksearchbar13 = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        #         imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        #         imageUrl = imageUrl.find('img')
                        #         imageUrl = imageUrl['src']
                        #         imageUrlbar13 = '<img src="'+ imageUrl + '" width="80" >'

                        #     #Busqueda por Barcode Original
                        #     search = driver.find_element_by_xpath('//*[@id="REsRA"]')
                        #     search.send_keys(Keys.CONTROL+"a")
                        #     search.send_keys(Keys.DELETE)
                        #     search.send_keys(item)
                        #     search.send_keys(Keys.RETURN)
                        #     randomSleep = np.random.choice([4,5])
                        #     time.sleep(randomSleep)
                        #     pageMatch = BeautifulSoup(driver.page_source,'lxml')
                        #     Notfound2 = pageMatch.find("div",attrs={"class":"eUYiW"})

                        #     #Si no encuientra valores regresa not found
                        #     if Notfound2 != None :
                        #         linksearchbarOri = 'Not Found'
                        #         imageUrlbarOri = 'Not Found'
                        #     elif Notfound2 == None:
                        #         linksearchbarOri = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        #         imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        #         imageUrl = imageUrl.find('img')
                        #         imageUrl = imageUrl['src']
                        #         imageUrlbarOri = '<img src="'+ imageUrl + '" width="80" >'

                        #     #Recoleccion de información en las listas
                        #     listurl.append(linksearch)
                        #     listSku.append(item)
                        #     listDescription.append(descripcion)
                        #     listDetails.append(' Web Found On Google')
                        #     listImagen.append(imageUrlDes)
                        #     listImagenBarcode.append(imageUrlbar13)
                        #     listurlBarcode.append(linksearchbar13)
                        #     listImagenBarcodeOri.append(imageUrlbarOri)
                        #     listurlBarcodeOri.append(linksearchbarOri)
                        #     listprice.append('Not Found')
                        #     listmarca.append("Not Found")
                        #     listtype.append("Not Found")
                        #     listwebsite.append("SELECTOS")
                        #     df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                        #     df = df.sort_values(by=['DETAILS'])
                        #     df.to_html('test_html.html', escape=False)
                    
                    #Si encuentra el producto en el primer retailer trae la información 
                    if productNotFound == None:
                        linkItem = pageSearchResults.select(firstMatch)
                        time.sleep(4)
                        linksItem =[str(linkItem['href']) for linkItem in linkItem]
                        linkItemFirst = linksItem[0]
                        urlMatch = urlRetailer + linkItemFirst
                        driver.get(urlMatch)
                        url_product = driver.current_url
                        randomSleep = np.random.choice([8,9,10])
                        time.sleep(randomSleep)

                        #Busqueda de elementos en la page cuando encuentra el producto
                        pageMatch = BeautifulSoup(driver.page_source,'lxml')
                        itemDesc = driver.find_element_by_xpath('//*[@id="page-title"]/div[1]/div/div/h1')
                        itemDetails = pageMatch.find('div',attrs={"class":itemDetailsHtml})
                        itemSku =pageMatch.find("div",attrs={"class":itemSkuHtml})
                        imageUrl = pageMatch.find("div",attrs={"class":itemImage})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrl = '<img src="'+ imageUrl + '" width="80" >'
                        if not itemSku:
                            itemSku =pageMatch.find("div",attrs={"class":itemSku2Html})
                        itemSku = itemSku.text
                        itemSku = int("".join(c for c in itemSku if c.isdigit()))
                        linksearchbar13 = 'No search'
                        imageUrlbar13 = 'No search'
                        linksearchbarOri = 'No search'
                        imageUrlbarOri = 'No search'
                        randomSleep = np.random.choice([5,6,7])
                        time.sleep(randomSleep)

                        #Se hace append a las listas antes creadas para ir capturando la información
                        listurl.append(url_product)
                        listSku.append(itemSku)
                        listDescription.append(itemDesc.text)
                        listDetails.append(itemDetails.text.replace('\n', ''))
                        listImagen.append(imageUrl)
                        listImagenBarcode.append(imageUrlbar13)
                        listurlBarcode.append(linksearchbar13)
                        listImagenBarcodeOri.append(imageUrlbarOri)
                        listurlBarcodeOri.append(linksearchbarOri)
                        listprice.append('Not Found')
                        listmarca.append("Not Found")
                        listtype.append("Not Found")
                        listwebsite.append("SELECTOS")
                        
                        #Se genera un DF con las listas para después generar un html con la información
                        df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                        df = df.sort_values(by=['DETAILS'])
                        df.to_html('test_html.html', escape=False)
                
                if selectos == False:
                    productNotFound = 'selectos'
                
                #Búsqueda para la páguina de Walmart Super
                if walmart == True:
                    #path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"
                    #driver =webdriver.Chrome(path)
                    driver.get('https://super.walmart.com.mx/')
                    search = driver.find_element_by_xpath('//*[@id="headerId"]/div/div[1]/div[2]/div/div/div/input')
                    time.sleep(6)
                    search.click()
                    search.send_keys(itemwm)
                    search.send_keys(Keys.RETURN)
                    time.sleep(2)
                    pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                    productNotFoundWalmart = pageSearchResults.find("div",attrs={"class":"no-results_container__jD7-s"})

                    if productNotFoundWalmart != None:
                        pass
                    if productNotFoundWalmart == None:
                        randomSleep = np.random.choice([8,9,10])
                        time.sleep(10)
                        pageMatch = BeautifulSoup(driver.page_source, 'lxml')
                        found = pageMatch.find("div",attrs={"class":"product_name__3ID6d"})
                        found = found.find('a')
                        found = found['href']
                        itemfound = 'https://super.walmart.com.mx'+ found
                        driver.get(itemfound)
                        time.sleep(5)
                        details = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[3]/div/div[2]/div/p[3]')
                        details = details.text
                        time.sleep(6)
                        upc = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[2]/div[2]/div[2]/p')
                        upc = upc.text
                        time.sleep(2)
                        precio = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[2]/div[2]/div[3]/h4/meta').get_attribute('content')
                        url_product = driver.current_url
                        imageUrl = driver.find_element_by_xpath('//*[@id="scrollToTopComponent"]/section/div[1]/div[2]/div[1]/div[1]/div[1]/div/img').get_attribute('src')
                        # pageMatch = BeautifulSoup(driver.page_source, 'lxml')
                        # imageUrl = pageMatch.find("img",attrs={"class":"image_image__mGFxl"})
                        #imageUrl = imageUrl.find('img')
                        # imageUrl = imageUrl['src']
                        imageUrl = '<img src="'+ imageUrl + '" width="90" >'
                        
                        listurl.append(url_product)
                        listSku.append(upc)
                        listDescription.append(descripcion)
                        listDetails.append(details)
                        listImagen.append(imageUrl)
                        listprice.append(precio)
                        listImagenBarcode.append("Not Search")
                        listurlBarcode.append("Not Search")
                        listImagenBarcodeOri.append("Not Search")
                        listurlBarcodeOri.append("Not Search")
                        listmarca.append("Not Found")
                        listtype.append("Not Found")
                        listwebsite.append('WALMART')
                        df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                        df = df.sort_values(by=['DETAILS'])
                        df.to_html('test_html.html', escape=False)
                if walmart == False:
                    productNotFoundWalmart = 'walmart'

                #Busqueda para la página de Chedraui
                if chedraui == True:
                    #path=r"C:\Users\mobr1001\Documents\WebScrapper\ChromeDriver\chromedriver.exe"
                    #driver =webdriver.Chrome(path)
                    driver.get('https://www.chedraui.com.mx/')
                    search = driver.find_element_by_id('searchBox')
                    time.sleep(4)
                    search.click()
                    search.send_keys(item)
                    search.send_keys(Keys.RETURN)
                    pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                    productNotFoundChedraui = pageSearchResults.find("div",attrs={"class":"totalResults not-found"})
                    if productNotFoundChedraui != None:
                        pass
                    if productNotFoundChedraui == None:
                        time.sleep(9)
                        #pageMatch = BeautifulSoup(driver.page_source,'lxml')
                        details = driver.find_element_by_xpath('//*[@id="productTabs"]/div[1]/div[2]/div/div/div/div/div/p[1]')
                        details = details.text
                        sku = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[2]/div[2]/div[2]/span[2]')
                        sku = sku.text
                        precio = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[3]/div[3]/div/div/div[1]/p')
                        precio = precio.text
                        tipo = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[3]/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/span')
                        tipo = tipo.text
                        marca = driver.find_element_by_xpath('//*[@id="page-content "]/div/div[3]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[2]/span/a')
                        marca = marca.text
                        url_product = driver.current_url
                        pageMatch = BeautifulSoup(driver.page_source, 'lxml')
                        imageUrl = pageMatch.find("div",attrs={"class":"item active"})
                        #image = driver.find_element_by_css_selector('div.image-gallery js-gallery')
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrl = '<img src= https://www.chedraui.com.mx'+ imageUrl + '" width="90" >'
                        #img = Image.open(requests.get(imageUrl, stream = True).raw)

                        listurl.append(url_product)
                        listSku.append(sku)
                        listDescription.append(descripcion)
                        listDetails.append(details)
                        listImagen.append(imageUrl)
                        listprice.append(precio)
                        listImagenBarcode.append("Not Search")
                        listurlBarcode.append("Not Search")
                        listImagenBarcodeOri.append("Not Search")
                        listurlBarcodeOri.append("Not Search")
                        listmarca.append(marca)
                        listtype.append(tipo)
                        listwebsite.append("CHEDRAUI")
                        
                        df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                        df = df.sort_values(by=['DETAILS'])
                        df.to_html('test_html.html', escape=False)
                if chedraui == False:
                    productNotFoundChedraui = 'chedraui'
                
                #Busqueda para la página de La Comer
                if lacomer == True:
                    driver.get('https://www.lacomer.com.mx/')
                    time.sleep(5)
                    search = driver.find_element_by_id('idSearch')
                    time.sleep(4)
                    search.click()
                    search.send_keys(itemcv)
                    search.send_keys(Keys.RETURN)
                    time.sleep(5)
                    pageSearchResults = BeautifulSoup(driver.page_source, 'lxml')
                    productNotFoundComer = pageSearchResults.find("div",attrs={"class":"no_result_busqueda"})
                    #productNotFoundComer = driver.find_element_by_xpath('//*[@id="product_list"]/div/div[2]/div/div/div[1]/div/img').get_attribute('alt')
                    if productNotFoundComer != None:
                        pass
                    if productNotFoundComer == None:
                        time.sleep(5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                        #pageMatch = BeautifulSoup(driver.page_source,'lxml')
                        found = driver.find_element_by_xpath('//*[@id="product_list"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/a')
                        found.click()                   
                        time.sleep(5)
                        precio = driver.find_element_by_xpath('//*[@id="detalleSection"]/div[3]/ng-template/ng-template/span')
                        precio = precio.text
                        url_product = driver.current_url
                        pageMatch = BeautifulSoup(driver.page_source, 'lxml')
                        imageUrl = pageMatch.find("img",attrs={"class":"img-product-detail centerImg"})
                        #image = driver.find_element_by_css_selector('div.image-gallery js-gallery')
                        #imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrl = '<img src="'+ imageUrl + '" width="90" >'
                        #img = Image.open(requests.get(imageUrl, stream = True).raw)

                        listurl.append(url_product)
                        listSku.append(itemcv)
                        listDescription.append("Not Found")
                        listDetails.append("Not Found")
                        listImagen.append(imageUrl)
                        listprice.append(precio)
                        listImagenBarcode.append("Not Search")
                        listurlBarcode.append("Not Search")
                        listImagenBarcodeOri.append("Not Search")
                        listurlBarcodeOri.append("Not Search")
                        listmarca.append("Not Found")
                        listtype.append("Not Found")
                        listwebsite.append("LA COMER")
                        
                        df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                        df = df.sort_values(by=['DETAILS'])
                        df.to_html('test_html.html', escape=False)
                    if lacomer == False:
                        pass
                if lacomer == False:
                    productNotFoundComer = 'lacomer'

                #Busqueda en google para Puerto Rico
                if productNotFound != None and productNotFoundWalmart != None and productNotFoundChedraui != None and productNotFoundComer != None and pais== 'Puerto Rico':
                    driver.get("https://www.google.com.pr/imghp?hl=es-419&tab=ri&ogbl")
                    time.sleep(2)
                    search = driver.find_element_by_name("q")
                    search.send_keys(descripcion)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([8,9,10])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    linksearch = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                    imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                    imageUrl = imageUrl.find('img')
                    imageUrl = imageUrl['src']
                    imageUrlDes = '<img src="'+ imageUrl + '" width="80" >'
                    randomSleep = np.random.choice([4,6])
                    time.sleep(randomSleep)

                    #Busqueda por Barcode 13 digitos
                    search = driver.find_element_by_name("q")
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(itemcv)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([6,7,8])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuentra valores regresa not found
                    if Notfound != None :
                        linksearchbar13 = 'Not Found'
                        imageUrlbar13 = 'Not Found'
                    elif Notfound == None:
                        linksearchbar13 = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbar13 = '<img src="'+ imageUrl + '" width="80" >'

                    #Busqueda por Barcode Original
                    search = driver.find_element_by_xpath('//*[@id="REsRA"]')
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(item)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([4,5])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound2 = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuientra valores regresa not found
                    if Notfound2 != None :
                        linksearchbarOri = 'Not Found'
                        imageUrlbarOri = 'Not Found'
                    elif Notfound2 == None:
                        linksearchbarOri = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbarOri = '<img src="'+ imageUrl + '" width="80" >'
                    
                    #Recoleccion de información en las listas
                    listurl.append(linksearch)
                    listSku.append(item)
                    listDescription.append(descripcion)
                    listDetails.append('Not Found')
                    listImagen.append(imageUrlDes)
                    listImagenBarcode.append(imageUrlbar13)
                    listurlBarcode.append(linksearchbar13)
                    listImagenBarcodeOri.append(imageUrlbarOri)
                    listurlBarcodeOri.append(linksearchbarOri)
                    listprice.append('Not Found')
                    listmarca.append("Not Found")
                    listtype.append("Not Found")
                    listwebsite.append("Google")
                    df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                    df = df.sort_values(by=['DETAILS'])
                    df.to_html('test_html.html', escape=False)
                    continue

                #Busqueda en google cuando se selecciona Mexico
                if productNotFound != None and productNotFoundWalmart != None and productNotFoundChedraui != None and productNotFoundComer != None and pais== 'México':
                    driver.get("https://www.google.com.mx/imghp?hl=es-419&tab=ri&ogbl")
                    time.sleep(2)
                    search = driver.find_element_by_name("q")
                    search.send_keys(descripcion)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([8,9,10])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    linksearch = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                    imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                    imageUrl = imageUrl.find('img')
                    imageUrl = imageUrl['src']
                    imageUrlDes = '<img src="'+ imageUrl + '" width="80" >'
                    randomSleep = np.random.choice([4,6])
                    time.sleep(randomSleep)

                    #Busqueda por Barcode 13 digitos
                    search = driver.find_element_by_name("q")
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(itemcv)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([6,7,8])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuentra valores regresa not found
                    if Notfound != None :
                        linksearchbar13 = 'Not Found'
                        imageUrlbar13 = 'Not Found'
                    elif Notfound == None:
                        linksearchbar13 = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbar13 = '<img src="'+ imageUrl + '" width="80" >'

                    #Busqueda por Barcode Original
                    search = driver.find_element_by_xpath('//*[@id="REsRA"]')
                    search.send_keys(Keys.CONTROL+"a")
                    search.send_keys(Keys.DELETE)
                    search.send_keys(item)
                    search.send_keys(Keys.RETURN)
                    randomSleep = np.random.choice([4,5])
                    time.sleep(randomSleep)
                    pageMatch = BeautifulSoup(driver.page_source,'lxml')
                    Notfound2 = pageMatch.find("div",attrs={"class":"eUYiW"})

                    #Si no encuientra valores regresa not found
                    if Notfound2 != None :
                        linksearchbarOri = 'Not Found'
                        imageUrlbarOri = 'Not Found'
                    elif Notfound2 == None:
                        linksearchbarOri = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute('href')
                        imageUrl = pageMatch.find("div",attrs={"class":"bRMDJf islir"})
                        imageUrl = imageUrl.find('img')
                        imageUrl = imageUrl['src']
                        imageUrlbarOri = '<img src="'+ imageUrl + '" width="80" >'
                    
                    #Recoleccion de información en las listas
                    listurl.append(linksearch)
                    listSku.append(item)
                    listDescription.append(descripcion)
                    listDetails.append('Not Found')
                    listImagen.append(imageUrlDes)
                    listImagenBarcode.append(imageUrlbar13)
                    listurlBarcode.append(linksearchbar13)
                    listImagenBarcodeOri.append(imageUrlbarOri)
                    listurlBarcodeOri.append(linksearchbarOri)
                    listprice.append('Not Found')
                    listmarca.append("Not Found")
                    listtype.append("Not Found")
                    listwebsite.append("Google")
                    df=pd.DataFrame(list(zip(listSku,listDescription,listDetails, listprice, listmarca, listtype, listwebsite, listImagen, listurl, listImagenBarcode,listurlBarcode,listImagenBarcodeOri,listurlBarcodeOri)),columns=['SKU','DESCRIPTION','DETAILS', 'PRICE', "COMMERCIAL BRAND", "TYPE", 'SEARCH SITE' ,'IMAGE (DESCRIPTION)', 'PRODUCT LINK(DESCRIPTION)', 'IMAGE(BARCODE 13 DIGITS)', 'PRODUCT LINK(BARCODE 13 DIGITS)', 'IMAGE(BARCODE ORIGINAL)', 'PRODUCT LINK(BARCOCE ORIGINAL)'])
                    df = df.sort_values(by=['DETAILS'])
                    df.to_html('test_html.html', escape=False)
                    continue
        end_time = datetime.now()
        executionTime = (end_time - start_time)
        print('Finalizado en ', executionTime)
            #dfcsv = df.to_csv('ItemsSearchPR.csv', index=False)
        driver.close()

    def Predict(self, dfItems):
        S = Scrapper()
        S.ProductCategoryPredict(self.df)

    def ScrapPredict(self):
        S = Scrapper()
        S.ScrapingPredict(self.df)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

# S = Functions()
# S.Walmart()
#S.Savemodel()
# S.Extractmodel()
#S.ProductCategoryPredict()
