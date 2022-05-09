from re import S
from socket import SO_ACCEPTCONN


def get_cheapest_hotel(number):   #DO NOT change the function's name
    list_data = number.split()
    cliente = list_data[0]
    list_data.pop(0)
    s_lak = calcula_valor_Lakewood(cliente,list_data)
    s_bri = calcula_valor_Bridgewood(cliente,list_data)
    s_rid = calculo_valor_Ridgewood(cliente,list_data)
    cheapest_hotel = toma_decisao(s_lak,s_bri,s_rid)
    return cheapest_hotel

def calcula_valor_Lakewood(cliente,list_data):
    soma = 0
    if(cliente == "Regular:"):
        for data in list_data:
            if(data.find("(sun)") != -1 or  data.find("(sat)") != -1):
                soma = soma + 90
            else:
                soma = soma + 110
        return soma
    else:
        for data in list_data:
            soma = soma + 80
        return soma

def calcula_valor_Bridgewood(cliente,list_data):
    soma = 0
    if(cliente == "Regular:"):
        for data in list_data:
            if(data.find("(sun)") != -1 or  data.find("(sat)") != -1):
                soma = soma + 60
            else:
                soma = soma + 160
        return soma
    else:
        for data in list_data:
            if(data.find("(sun)") != -1 or  data.find("(sat)") != -1):
                soma = soma + 50
            else:
                soma = soma + 110
        return soma

def calculo_valor_Ridgewood(cliente,list_data):
    soma = 0
    if(cliente == "Regular:"):
        for data in list_data:
            if(data.find("(sun)") != -1 or  data.find("(sat)") != -1):
                soma = soma + 150
            else:
                soma = soma + 220
        return soma
    else:
        for data in list_data:
            if(data.find("(sun)") != -1 or  data.find("(sat)") != -1):
                soma = soma + 40
            else:
                soma = soma + 100
        return soma

def toma_decisao(s_Lak,s_Bri,s_Rid):
    if(s_Rid <= s_Bri and s_Rid <= s_Lak):#Ridgewood tem preferencia pela classificação 5 em caso de empate
        return "Ridgewood"
    elif(s_Bri <= s_Lak and s_Bri < s_Rid):#Bridgewood tem preferencia sobre o Lakewood em empate
        return "Bridgewood"
    elif(s_Lak < s_Bri and s_Lak < s_Rid):#Lakewood só é escolhido caso o preço for o mais baixo dos três
        return "Lakewood"