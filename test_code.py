#####################################
# Contact: awak3ned@protonmail.com  #
#                                   #
# Uso : tk-crypter hash text        #
# Exemplo : tk-crypter md5 abc123   #
#####################################
from tkinter import *
import hashlib
import sys
#####################################
form = Tk()
form.title("tk-crypter by Awak3ned")
#####################################
MD5 = 'md5'
SHA1 = 'sha1'
SHA224 = 'sha224'
SHA256 = 'sha256'
SHA384 = 'sha384'
SHA512 = 'sha512'
HSEsl = 'HASH'
HSEs2 = ''
#####################################
def gerar_senha():
   print ("Gerando sua Hash!")
   print ("Modelo:",sp1.get())
   HSEsl = sp1.get()
   if (HSEsl == '0'):
       HSEs2 = MD5
       print ("TIPO DA HASH:",HSEs2)
   if (HSEsl == '1'):
       HSEs2 = SHA1
       print ("TIPO DA HASH:",HSEs2)
   if (HSEsl == '2'):
       HSEs2 = SHA224
       print ("TIPO DA HASH:",HSEs2)
   if (HSEsl == '3'):
       HSEs2 = SHA256
       print ("TIPO DA HASH:",HSEs2)
   if (HSEsl == '4'):
       HSEs2 = SHA384
       print ("TIPO DA HASH:",HSEs2)
   if (HSEsl == '5'):
       HSEs2 = SHA512
       print ("TIPO DA HASH:",HSEs2)
   la1["text"] = 'Escolha o tipo de hash :', HSEs2
   hash_name = HSEs2
   data = en1.get()
   print(data)
   h = hashlib.new(hash_name)
   h.update(data)
   print(h.hexdigest())
   la3["text"] = 'HASH :',h.hexdigest()
print("Iniciando o script...")
#####################################
def start_form():
   print ("Atualizando o script....")
   print ("Modelo:",sp1.get())
   HSEsl = sp1.get()
   if (HSEsl == '0'):
       HSEs2 = MD5
   if (HSEsl == '1'):
       HSEs2 = SHA1
   if (HSEsl == '2'):
       HSEs2 = SHA224
   if (HSEsl == '3'):
       HSEs2 = SHA256
   if (HSEsl == '4'):
       HSEs2 = SHA384
   if (HSEsl == '5'):
       HSEs2 = SHA512
   la1["text"] = 'Escolha o tipo de hash :', HSEs2
   hash_name = HSEs2
#####################################
lbf1 = LabelFrame(form, text="Multi Ecodificador de strings  :")
lbf1.pack(fill="both", expand="yes")
#####################################
lbf2 = LabelFrame(lbf1, text="Definir :")
lbf2.pack(fill="both", expand="yes")
#####################################
la1 = Label(lbf2, text="{Escolha o tipo de hash :}")
la1.grid(row="01", column="01")
sp1 = Spinbox(lbf2, from_=0, to=5, command=start_form, width="5")
sp1.grid(row="01", column="02")
#####################################
la2 = Label(lbf2, text="Digite o que deseja :")
la2.grid(row="02", column="01")
en1 = Entry(lbf2, width="32")
en1.grid(row="02", column="02")
#####################################
bt1 = Button(lbf2, text="Encoder string !", command=gerar_senha, width="10")
bt1.grid(row="04", column="01")
#####################################
la3 = Label(lbf1, text="HASH :")
la3.pack()
#####################################
start_form()
#####################################
form.resizable(width="FALSE", height="FALSE")
form.geometry("500x150+200+200")
form.mainloop()