# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:26:53 2022

@author: Lenovo
"""

import requests
import bs4 
base_url="https://books.toscrape.com/catalogue/page-{}.html"
tst=[]
for j in range(1,51):
    turl=base_url.format(j)
    res=requests.get(turl)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    products=(soup.select(".product_pod"))
    for i in products:
        if i.select(".star-rating.Two")!=[]:
            title=(i.select("a")[1])['title']
            tst.append(title)
print(tst)