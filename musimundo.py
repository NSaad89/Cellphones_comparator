#*****************************************************************************************************************
# FUNCIÓN para ARMAR lista de celulares REPETIDOS POR FECHA de MUSIMUNDO 
# Recibe: lista de celulares de la DB editada (list)
# Retorna: lista de celulares REPETIDOS CON FECHA de MUSIMUNDO (list)
#*****************************************************************************************************************
def musimundo_list(edited_db_list):  
    musimundo_date_repeated_list=[]

    for i in edited_db_list:
        if i not in musimundo_date_repeated_list and i[5]=="Musimundo":
            musimundo_date_repeated_list.append(i)

    return musimundo_date_repeated_list


#*****************************************************************************************************************
# FUNCIÓN para FILTRAR un celular que sea de MUSIMUNDO
# Recibe: celular de HOY sin fecha (list)
# Retorna: Mensaje "Musimundo" (str)
#*****************************************************************************************************************
def filter_today_cellphone_musimundo(today_cellphone):
    if today_cellphone[4]=="Musimundo":

        return "Musimundo"


#*****************************************************************************************************************
# FUNCIÓN para CREAR lista FINAL de MUSIMUNDO con ESTADO
# Recibe: Lista de celulares de HOY de MUSIMUNDO (list) y Lista de celulares REPETIDOS CON FECHA de MUSIMUNDO (list)
# Retorna: Lista FINAL de MUSIMUNDO SIN REPETIDOS y CON ESTADO (list)
#*****************************************************************************************************************
def create_musimundo_final_list(musimundo_today_list,musimundo_date_repeated_list):
    musimundo_not_repeated_list_with_state=[]
    state=""
    for musimundo_cellphone in musimundo_today_list:
        flag=True
        menor=musimundo_cellphone[1]
        for musimundo_repeated_product in musimundo_date_repeated_list:
            if musimundo_repeated_product[0]==musimundo_cellphone[0]:
                if musimundo_repeated_product[1]!=musimundo_cellphone[1]:
                    flag=False
                    if musimundo_repeated_product[1]<menor:
                        menor=musimundo_repeated_product[1]
                        fecha=musimundo_repeated_product[4]                        
                else:
                        state="Hoy se mantuvo el precio"
        if flag==False:
            if menor==musimundo_cellphone[1]:
                state="El precio de hoy es el más bajo!"
            else:
                state="El precio de hoy no es el más bajo. El más bajo fue $"+str(menor)+" el día "+fecha

        cellphone_not_repeated=[]
        cellphone_not_repeated.append(musimundo_cellphone[0])
        cellphone_not_repeated.append(musimundo_cellphone[1])
        cellphone_not_repeated.append(musimundo_cellphone[2])
        cellphone_not_repeated.append(musimundo_cellphone[3])
        cellphone_not_repeated.append(state)

        musimundo_not_repeated_list_with_state.append(cellphone_not_repeated)
        
    return musimundo_not_repeated_list_with_state