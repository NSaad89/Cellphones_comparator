from bs4 import BeautifulSoup as soup
import requests
import datetime
import re

#*****************************************************************************************************************
# FUNCIÓN para WebScraping de un celular con fecha
# Recibe: Url del link (str), Class de la etiqueta del name (str), Class de la etiqueta del price (str), class
# de la etiqueta del local (str), class de la etiqueta de la pantalla (str) y class de la etiqueta de la 
# memoria (str)
# Retorna: celular de HOY con fecha (list)
#*****************************************************************************************************************
def webscraping(link,class_name,class_price,class_screen,
                                    class_memory,local):
    url=requests.get(link)
    page_soup=soup(url.content,"html.parser")

    if local=="Musimundo":
        screensize=0
        memory=""
        name_not_final=page_soup.find("p",{"class":class_name})
        name_not_final=name_not_final.text
        name=""
        for i in range(0, len(name_not_final)): 
            if i>5:
                name=name+name_not_final[i]
        price_span=page_soup.find("span",{"class":class_price})
        price=price_span.find("span")
        price=price.text
        aux=""
        for s in re.findall(r'\d+',price):
            aux+=s
        price=int(aux)
        price=int(price/100)
        cont=1
        for item in page_soup.find_all("tr",{"class":class_screen}):
            if cont==19:
                cont2=1
                for td in item.find_all("td"):
                    if cont2==2:
                        memory_not_final=td
                        memory_not_final=memory_not_final.text
                        memory=""
                        for i in range(0, len(memory_not_final)): 
                            if i>12:
                                memory=memory+memory_not_final[i]
                    cont2+=1
            if cont==21:
                cont2=1
                for td in item.find_all("td"):
                    if cont2==2:
                        screensize=td
                        screensize=screensize.text
                        screensize=float(screensize)
                    cont2+=1
            cont+=1

    if local=="Compumundo":
        screensize=0
        memory=0
        name_div=page_soup.find("div",{"class":class_name})
        name=name_div.find("h1")
        name=name.text
        cont=1
        price=""
        for i in page_soup.find_all("meta"):
            if cont==15:
                price=i["content"]
            cont+=1
        aux=""
        for s in re.findall(r'\d+',price):
            aux+=s
        price=int(aux)
        price=int(price/100)
        screensize_div1=page_soup.find("div",{"class":class_screen})
        screensize_div2=screensize_div1.find("div",{"class":"gb-tech-spec-module-list"})
        screensize=screensize_div2.find("span",{"class":"gb-tech-spec-module-list-description"})
        screensize=screensize.text
        for s in re.findall(r'\d+.\d+',screensize):
            screensize=float(s)
        memory_p=page_soup.find("p",{"class":class_memory})
        memory=memory_p.find("strong")
        memory=memory.text
        memory=memory+" GB"
    
    
    date=datetime.datetime.now()
    date=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
    
    cellphone=[]
    cellphone.append(name)
    cellphone.append(200000)
    cellphone.append(screensize)
    cellphone.append(memory)
    cellphone.append(date)
    cellphone.append(local)

    return cellphone


#*****************************************************************************************************************
# FUNCIÓN para ARMAR un celular de HOY sin fecha
# Recibe: celular de HOY (list) 
# Retorna: celular de HOY sin fecha (list)
#*****************************************************************************************************************

def create_today_cellphone(cellphone):
    
    today_cellphone=[]
    today_cellphone.append(cellphone[0])
    today_cellphone.append(cellphone[1])
    today_cellphone.append(cellphone[2])
    today_cellphone.append(cellphone[3])
    today_cellphone.append(cellphone[5])

    return today_cellphone
