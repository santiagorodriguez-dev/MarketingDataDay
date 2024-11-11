from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

def datos_rains(url, web):
    df_rain = pd.DataFrame()

    try:
        url_sopa = url

        res = requests.get(url_sopa)
        sopa = BeautifulSoup(res.content, "html.parser")

        resultado = sopa.find("div", {"class": "grid gap-y-6 lg:gap-y-10 mb-18 grid-cols-2 lg:grid-cols-4"})
        result_tr = resultado.findAll("div", {"class": "product-item @container"})
        
        if (res.status_code == 200 and resultado and result_tr):
 
            lista = []
            titulo = ''
            precio = ''
            for tr in result_tr:
                titulo = tr.find("p", {"class": "w-full @xs:w-auto font-bold"})
                precio = tr.find("span", {"class": "flex gap-1"})

                lista_inter = []
                lista_inter.append(titulo,precio,web)
                lista.append(lista_inter)

        df_rain = pd.DataFrame(lista)

    except:
        print("error en datos_rains(url)")
 
    return df_rain

def datos_minimalismbrand_camisetas(url, web, categorias):
    df_rain = pd.DataFrame()

    #try:
    url_sopa = url

    res = requests.get(url_sopa)
    sopa = BeautifulSoup(res.content, "html.parser")

    #resultado = sopa.find("div", {"class": "product-list product-list--per-row-3 product-list--per-row-mob-2 product-list--per-row-mob-2 product-list--image-shape-shortest"})
    #print(resultado)
    result_tr = sopa.findAll("div", {"class": "product-info"})
    
    #if (res.status_code == 200 and resultado and result_tr):

    lista = []
    titulo = ''
    precio = ''
    for tr in result_tr:
        try:
            titulo = str(tr.find("h3").text).strip()
        except:
            titulo = ''
        try:
            precio = str(tr.find("div", {"class": "product-price"}).text).strip()
            precio = precio.split("\n")[0]
        except:
            precio = '0'

        if (titulo and precio):
            lista_inter = []
            lista_inter.append(titulo)
            lista_inter.append(precio)
            lista_inter.append(web)
            lista_inter.append(categorias)
            
            lista.append(lista_inter)

    df_rain = pd.DataFrame(lista)

    #except:
    #    print("error en datos_minimalismbrand(url)")
 
    return df_rain

def datos_minimalismbrand_cullote(url, web, categorias):
    df_rain = pd.DataFrame()

    #try:
    url_sopa = url

    res = requests.get(url_sopa)
    sopa = BeautifulSoup(res.content, "html.parser")

    #resultado = sopa.find("div", {"class": "product-list product-list--per-row-3 product-list--per-row-mob-2 product-list--per-row-mob-2 product-list--image-shape-shortest"})
    #print(resultado)
    result_tr = sopa.findAll("div", {"class": "product-info"})
    
    #if (res.status_code == 200 and resultado and result_tr):

    lista = []
    titulo = ''
    precio = ''
    for tr in result_tr:
        try:
            titulo = str(tr.find("h3").text).strip()
        except:
            titulo = ''
        try:
            precio = str(tr.find("div", {"class": "product-price"}).text).strip()
            precio = precio.split("\n")[0]
        except:
            pass
        
        if (titulo):
            lista_inter = []
            lista_inter.append(titulo)
            lista_inter.append(precio)
            lista_inter.append(web)
            lista_inter.append(categorias)
            
            lista.append(lista_inter)

    
    df_rain = pd.DataFrame(lista)

    #except:
    #    print("error en datos_minimalismbrand(url)")
 
    return df_rain




