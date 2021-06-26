from flask import Flask, render_template, request
import threading
from db_and_format import format_list
from musimundo import musimundo_list, create_musimundo_final_list
from compumundo import compumundo_list, create_compumundo_final_list
from threads import single_thread
from datetime import datetime

#*****************************************************************************************************************
# FUNCIÓN PRINCIPAL para INICIAR el webscraping y DERIVAR los celulares al HTML
# Recibe: -
# Retorna: template con el archivo HTML de destino y el listado de celulares (list)
#*****************************************************************************************************************
app=Flask(__name__)
@app.route('/')
def myapp():

    musimundo_today_list=[]
    compumundo_today_list=[]

    link="https://www.musimundo.com/telefonia/telefonos-celulares/celulares-liberados/celular-samsung-galaxy-s21-sm-g991b-violeta/p/00320173"
    class_name="mus-pro-name strong"
    class_price="mus-pro-price-number"
    class_screen="value-label"
    class_memory="value-label"
    local="Musimundo"

    t1=threading.Thread(target=single_thread, args=(link,class_name,class_price,class_screen,
                                    class_memory,local,musimundo_today_list,compumundo_today_list))
    t1.start()

    link="https://www.musimundo.com/telefonia/telefonos-celulares/celulares-liberados/celular-samsung-galaxy-s21-gris/p/00320170"
    class_name="mus-pro-name strong"
    class_price="mus-pro-price-number"
    class_screen="value-label"
    class_memory="value-label"
    local="Musimundo"

    t2=threading.Thread(target=single_thread, args=(link,class_name,class_price,class_screen,
                                    class_memory,local,musimundo_today_list,compumundo_today_list))
    t2.start()

    link="https://www.compumundo.com.ar/producto/celular-libre-samsung-galaxy-s21-violeta-sm-g991bzvlaro-cm/9efa5220d5"
    class_name="title-product"
    class_price="og:price:amount"
    class_screen="gb-tech-spec-module gb-tech-spec-cellphone-screen"
    class_memory="gb-tech-spec-cellphone-memory-info"
    local="Compumundo"

    t3=threading.Thread(target=single_thread, args=(link,class_name,class_price,class_screen,
                                    class_memory,local,musimundo_today_list,compumundo_today_list))
    t3.start()

    link="https://www.compumundo.com.ar/producto/celular-libre-samsung-galaxy-s21-gris-sm-g996bzslaro-cm/4ebdc7bc62"
    class_name="title-product"
    class_price="og:price:amount"
    class_screen="gb-tech-spec-module gb-tech-spec-cellphone-screen"
    class_memory="gb-tech-spec-cellphone-memory-info"
    local="Compumundo"

    t4=threading.Thread(target=single_thread, args=(link,class_name,class_price,class_screen,
                                    class_memory,local,musimundo_today_list,compumundo_today_list))
    t4.start()

    t1.join()   
    t2.join()
    t3.join()   
    t4.join()

    list1=create_musimundo_final_list(musimundo_today_list,musimundo_list(format_list()))
    list2=create_compumundo_final_list(compumundo_today_list,compumundo_list(format_list()))

    return render_template('index.html',musimundo_list=list1,compumundo_list=list2)


#*****************************************************************************************************************
# FUNCIÓN para FRENAR el SERVER de la APP
# Recibe: -
# Retorna: -
#*****************************************************************************************************************
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')

    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')

    func()


#*****************************************************************************************************************
# FUNCIÓN que LLAMA a shutdown_server() y MAPEA LA RUTA para FRENAR EL SERVER
# Recibe: -
# Retorna: Mensaje confirmando el freno del servidor (str)
#*****************************************************************************************************************
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    
    return 'Server shutting down...'