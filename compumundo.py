#*****************************************************************************************************************
# FUNCIÓN para ARMAR lista de celulares REPETIDOS POR FECHA de COMPUMUNDO 
# Recibe: lista de celulares de la DB editada (list)
# Retorna: lista de celulares REPETIDOS CON FECHA de COMPUMUNDO (list)
#*****************************************************************************************************************
def compumundo_list(edited_db_list):  
    compumundo_date_repeated_list=[]

    for i in edited_db_list:
        if i not in compumundo_date_repeated_list and i[5]=="Compumundo":
            compumundo_date_repeated_list.append(i)

    return compumundo_date_repeated_list


#*****************************************************************************************************************
# FUNCIÓN para FILTRAR un celular que sea de COMPUMUNDO
# Recibe: celular de HOY sin fecha (list)
# Retorna: Mensaje "Compumundo" (str)
#*****************************************************************************************************************
def filter_today_cellphone_compumundo(today_cellphone):
    if today_cellphone[4]=="Compumundo":

        return "Compumundo"


#*****************************************************************************************************************
# FUNCIÓN para CREAR lista FINAL de COMPUMUNDO con ESTADO
# Recibe: Lista de celulares de HOY de COMPUMUNDO (list) y Lista de celulares REPETIDOS CON FECHA de COMPUMUNDO (list)
# Retorna: Lista FINAL de COMPUMUNDO SIN REPETIDOS y CON ESTADO (list)
#*****************************************************************************************************************
def create_compumundo_final_list(compumundo_today_list,compumundo_date_repeated_list):
    compumundo_not_repeated_list_with_state=[]
    state=""
    for compumundo_cellphone in compumundo_today_list:
        flag=True
        menor=compumundo_cellphone[1]
        for compumundo_repeated_product in compumundo_date_repeated_list:
            if compumundo_repeated_product[0]==compumundo_cellphone[0]:
                if compumundo_repeated_product[1]!=compumundo_cellphone[1]:
                    flag=False
                    if compumundo_repeated_product[1]<menor:
                        menor=compumundo_repeated_product[1]
                        fecha=compumundo_repeated_product[4]                        
                else:
                        state="Hoy se mantuvo el precio"
        if flag==False:
            if menor==compumundo_cellphone[1]:
                state="El precio de hoy es el más bajo!"
            else:
                state="El precio de hoy no es el más bajo. El más bajo fue $"+str(menor)+" el día "+fecha

        cellphone_not_repeated=[]
        cellphone_not_repeated.append(compumundo_cellphone[0])
        cellphone_not_repeated.append(compumundo_cellphone[1])
        cellphone_not_repeated.append(compumundo_cellphone[2])
        cellphone_not_repeated.append(compumundo_cellphone[3])
        cellphone_not_repeated.append(state)

        compumundo_not_repeated_list_with_state.append(cellphone_not_repeated)
        
    return compumundo_not_repeated_list_with_state