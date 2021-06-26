from db_and_format import insert
from scraping import webscraping, create_today_cellphone
from musimundo import filter_today_cellphone_musimundo
from compumundo import filter_today_cellphone_compumundo

#*****************************************************************************************************************
# FUNCIÓN para definir la ejecución por HILOS
# Recibe: Url del link (str), Class de la etiqueta del name (str), Class de la etiqueta del price (str), class
# de la etiqueta del local (str), class de la etiqueta de la pantalla (str), class de la etiqueta de la memoria (str), 
# la lista de CELULARES de HOY de MUSIMUNDO (list) y la lista de CELULARES de HOY de COMPUMUNDO (list)
# Retorna: -
#*****************************************************************************************************************
def single_thread(link,class_name,class_price,class_screen,
                                    class_memory,local,musimundo_today_list,compumundo_today_list):
    insert(webscraping(link,class_name,class_price,class_screen,class_memory,local))
    today_cellphone=(create_today_cellphone(webscraping(link,class_name,class_price,class_screen,class_memory,local)))

    if (filter_today_cellphone_musimundo(today_cellphone))=="Musimundo":
        musimundo_today_list.append(today_cellphone)

    if (filter_today_cellphone_compumundo(today_cellphone))=="Compumundo":
        compumundo_today_list.append(today_cellphone)
