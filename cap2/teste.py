# 
# Orientações:
#   01 - instalar o Python  
#   02 - instalar o pillow [ pip install pillow ] - linha de comando
#   03 - criar a pasta carrosselPY na unidade C:
#   04 - criar a pasta img dentro da pasta carrosselPY
#   05 - inserir imagens na pasta img para teste
#   06 - na pasta carrosselPY executar o comando: python carrossel.py
#   07 - a partir deste momento o programa entra em loop
#   08 - inserir novas imagens que serão incluídas na lista de play
#   09 - testar e validar o programa local e em rede
#
 
import os
import tkinter as tk
from PIL import Image, ImageTk
 
# Configuração da pasta das imagens
image_folder = "img"
 
# Função para carregar a lista de imagens
def get_image_files():
    return [f for f in os.listdir(image_folder) if f.endswith(".png")]
 
# Configuração do player
root = tk.Tk()
root.title("Carrossel de Imagens")
 
label = tk.Label(root)
label.pack()
 
index = 0
image_files = get_image_files()  # Carrega inicialmente a lista de imagens
 
def update_image():
    global index, image_files
 
    # Atualiza a lista de imagens para incluir novos arquivos
    image_files = get_image_files()
 
    if image_files:
        img_path = os.path.join(image_folder, image_files[index])
        img = Image.open(img_path)
        img = img.resize((800, 800))  # Ajuste o tamanho conforme necessário
        img = ImageTk.PhotoImage(img)
 
        label.config(image=img)
        label.image = img
 
        index = (index + 1) % len(image_files)
 
    root.after(4000, update_image)  # Intervalo de 2 segundos entre imagens
 
# Inicia o carrossel
update_image()
root.mainloop()