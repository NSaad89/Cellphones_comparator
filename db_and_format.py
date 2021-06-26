import mysql.connector
import re

#*****************************************************************************************************************
# FUNCIÓN para Query INSERT INTO a la BD (ABRE y CIERRA LA CONEXIÓN)
# Recibe: celular (list)
# Retorna: -
#*****************************************************************************************************************
def insert(cellphone):
    connection = mysql.connector.connect(host='localhost',
                                         database='flaskproducts',
                                         user='root',
                                         password='root')
                                         
    try:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO CELLPHONES (Name, Price, ScreenSize, Memory, Date, Local) 
                            VALUES (%s, %s, %s, %s, %s, %s)""",(cellphone[0],cellphone[1],cellphone[2],
                            cellphone[3],cellphone[4],cellphone[5]))
        connection.commit()
    except mysql.connector.Error as e:
        print("Error writing data from MySQL table", )
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")    


#*****************************************************************************************************************
# FUNCIÓN para Query SELECT * FROM a la BD (ABRE y CIERRA LA CONEXIÓN)
# Recibe: -
# Retorna: lista de celulares desde la BD (list)
#*****************************************************************************************************************
def get():
    connection = mysql.connector.connect(host='localhost',
                                         database='flaskproducts',
                                         user='root',
                                         password='root')

    cellphones_list=[]

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM CELLPHONES')
        cellphones_list=cursor.fetchall()
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

    return cellphones_list


#*****************************************************************************************************************
# FUNCIÓN para FORMATEAR los CELULARES que vienen de la BD 
# Recibe: -
# Retorna: lista de celulares REPETIDOS (list)
#*****************************************************************************************************************
def format_list():
    cellphones=get()
    edited_db_list=[]

    for cellphone in cellphones:
        new_cellphones_list=[]
        new_cellphones_list.append(cellphone[0])
        new_cellphones_list.append(cellphone[1])
        new_cellphones_list.append(cellphone[2])
        new_cellphones_list.append(cellphone[3])
        date=str(cellphone[4])
        s=re.findall(r'\d+',date)
        date=str(s[0])+"-"+str(s[1])+"-"+str(s[2])
        new_cellphones_list.append(date)
        new_cellphones_list.append(cellphone[5])
        edited_db_list.append(new_cellphones_list)
    
    return edited_db_list