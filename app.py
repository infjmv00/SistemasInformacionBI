import streamlit as st
from tkinter import *
from tkinter import ttk
from llama_index import SimpleDirectoryReader
from llama_index import ServiceContext
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex
from dotenv import  load_dotenv
import os
import openai
import tkinter as tk
load_dotenv()
os.environ['OPENAI_API_KEY']= "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"
#openai.api_key=os.getenv("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")





with st.sidebar:
    st.title("Chatbot con informacion propia")
    st.markdown('''
    ## About 
    This App es implementada con las siguientes tecnologias:
    - [streamlit](https://streamlit.io) 
    - [Llama Index](https://gpt-index.readdocs.io)
    - [OpenAI](https://platform.openai.com/doc/models) LLM Model
                
                ''')


def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry('1240x640')#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="Coral1", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    # Insertarla en una etiqueta.
    image = tk.PhotoImage(file="imagenes/logotipo.png")
    label = ttk.Label(image=image)
    label.pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry('800x600')
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login

    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    # Cargar imagen del disco.
    
    
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 

def kNN():
    print("Algoritmo KNN") 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Recomendador de licitadores publicos")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="LLAMA-INDEX", command=llamaindex).pack() #EJECUTA "borrar_no_usuario()"


    #global ventana_exito
    #ventana_exito = Toplevel(ventana_login)
    #ventana_exito.title("Acceso a recomendador de licitadores publicos")
    #ventana_exito.geometry("800×600")
    #ventana_exito.config(width=300, height=200)
    #boton = ttk.Button(text="¡Hola, mundo!")
    #boton.place(x=50, y=50)
    #ventana_exito.mainloop()
    #Label(ventana_exito, text="Login finalizado con exito").pack()
    #Button(ventana_exito, text="KNN", command=borrar_exito_login).pack()
    #Button(ventana_exito, text="KNN", command=borrar_exito_login).pack()
    #root = tk.Tk()
    #root.config(width=300, height=200)
    #root.title("Botón en Tk")
    
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
    Button(ventana_no_clave, text="otro boton", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS
        
def borrar_pantalla_inicio():
    ventana_principal.destroy()

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()

def llamaindex():
    borrar_exito_login()
    borrar_pantalla_inicio()

    st.header("Chatbot con informacion propia")
    reader = SimpleDirectoryReader(input_dir='./data', recursive = True)
    docs = reader.load_data()
    service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo",temperature=0.5, system_prompt ="eres una machine learning y tu objetivo es responder preguntas"))
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    #print(index)
    query= st.text_input("responde preguntas relacionadas con la informacion")

    if query:

       chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose = True)
       response = chat_engine.chat(query)
       st.write(response.response)



    
if __name__=='__main__':

    #main()
    ventana_inicio()
