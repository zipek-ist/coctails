import streamlit as st
import json
from urllib.request import urlopen
st.text("Made by Ziya İpek")
st.image("https://thumbs.dreamstime.com/b/set-various-cocktails-black-background-set-various-cocktails-shaker-black-background-188649840.jpg")
st.title("Welcome to cocktail recipes page")
st.subheader("1-Choose your wish of ingerident from left sided bar")
st.subheader("2-After that you can choose name of cocktail from below")
st.subheader("3-You can read the instructions from deown below this page")


secim=st.sidebar.selectbox("Ingerident",["Whiskey","Gin","Vodka"])
viskidata=urlopen("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=whiskey").read()
viskiveri=json.loads(viskidata)
viskidrinks=viskiveri["drinks"]
gindata=urlopen("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=gin").read()
ginveri=json.loads(gindata)
gindrinks=ginveri["drinks"]
vodkadata=urlopen("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=vodka").read()
vodkaveri=json.loads(vodkadata)
vodkadrinks=vodkaveri["drinks"]






if secim=="Whiskey":
    secim2=st.sidebar.selectbox("Drinks",viskidrinks)
    link = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=13194"
    x=secim2["idDrink"]
    yenilink=link.replace("13194",x)
    tarif = urlopen(yenilink).read()
    a = json.loads(tarif)
    b = a["drinks"][0]["strInstructions"]
    ing1 = a["drinks"][0]["strIngredient1"]
    ing2 = a["drinks"][0]["strIngredient2"]
    ing3 = a["drinks"][0]["strIngredient3"]
    ing4 = a["drinks"][0]["strIngredient4"]
    ing5 = a["drinks"][0]["strIngredient5"]
    ing6 = a["drinks"][0]["strIngredient6"]
    ingeridents=[ing1,ing2,ing3,ing4,ing5,ing6]
    ingeridentsson = []
    for i in ingeridents:
        if i!=None:
            ingeridentsson.append(i)
    st.image(a["drinks"][0]["strDrinkThumb"])
    st.header("Ingeridents :")
    st.text(ingeridentsson)
    st.header("Instructions :")
    st.text(b)
elif secim=="Gin":
    secim2=st.sidebar.selectbox("Drinks",gindrinks)
    link = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=13194"
    x = secim2["idDrink"]
    yenilink = link.replace("13194", x)
    tarif = urlopen(yenilink).read()
    a = json.loads(tarif)
    b = a["drinks"][0]["strInstructions"]
    ing1 = a["drinks"][0]["strIngredient1"]
    ing2 = a["drinks"][0]["strIngredient2"]
    ing3 = a["drinks"][0]["strIngredient3"]
    ing4 = a["drinks"][0]["strIngredient4"]
    ing5 = a["drinks"][0]["strIngredient5"]
    ing6 = a["drinks"][0]["strIngredient6"]
    ingeridents=[ing1,ing2,ing3,ing4,ing5,ing6]
    ingeridentsson = []
    for i in ingeridents:
        if i!=None:
            ingeridentsson.append(i)
    st.image(a["drinks"][0]["strDrinkThumb"])
    st.header("Ingeridents :")
    st.text(ingeridentsson)
    st.header("Instructions :")
    st.text(b)
elif secim=="Vodka":
    secim2=st.sidebar.selectbox("Drinks",vodkadrinks)
    link = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=13194"
    x = secim2["idDrink"]
    yenilink = link.replace("13194", x)
    tarif = urlopen(yenilink).read()
    a = json.loads(tarif)
    b = a["drinks"][0]["strInstructions"]
    ing1 = a["drinks"][0]["strIngredient1"]
    ing2 = a["drinks"][0]["strIngredient2"]
    ing3 = a["drinks"][0]["strIngredient3"]
    ing4 = a["drinks"][0]["strIngredient4"]
    ing5 = a["drinks"][0]["strIngredient5"]
    ing6 = a["drinks"][0]["strIngredient6"]
    ingeridents = [ing1, ing2, ing3, ing4, ing5, ing6]
    ingeridentsson = []
    for i in ingeridents:
        if i != None:
            ingeridentsson.append(i)
    st.image(a["drinks"][0]["strDrinkThumb"])
    st.header("Ingeridents :")
    st.text(ingeridentsson)
    st.header("Instructions :")
    st.text(b)