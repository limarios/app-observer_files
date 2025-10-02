import os
import time
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pystray
from pystray import MenuItem as item, Icon
from PIL import Image

# Variáveis globais
watch_folder = ""
destination_folder = ""
observer = None

class FileCopyHandler(FileSystemEventHandler):
    """Manipulador de eventos para copiar arquivos automaticamente"""
    def on_created(self, event):
        if not event.is_directory:
            try:
                src_path = event.src_path
                filename = os.path.basename(src_path)
                dest_path = os.path.join(destination_folder, filename)
                
                time.sleep(1)  # Espera para garantir que o arquivo está pronto
                
                shutil.copy2(src_path, dest_path)
                print(f"Arquivo copiado: {src_path} -> {dest_path}")
            except Exception as e:
                print(f"Erro ao copiar arquivo: {e}")

def selecionar_pasta_origem():
    """Abre uma caixa de diálogo para selecionar a pasta de origem"""
    global watch_folder
    watch_folder = filedialog.askdirectory(title="Selecione a pasta a ser monitorada")

def selecionar_pasta_destino():
    """Abre uma caixa de diálogo para selecionar a pasta de destino"""
    global destination_folder
    destination_folder = filedialog.askdirectory(title="Selecione a pasta de destino")

def iniciar_monitoramento():
    """Inicia o monitoramento das pastas"""
    global observer
    if not watch_folder or not destination_folder:
        messagebox.showwarning("Atenção", "Selecione ambas as pastas antes de iniciar.")
        return

    # Salvar configurações
    with open("config.txt", "w") as f:
        f.write(f"{watch_folder}\n{destination_folder}")

    # Iniciar o monitoramento em uma thread separada
    observer = Observer()
    event_handler = FileCopyHandler()
    observer.schedule(event_handler, watch_folder, recursive=False)
    observer.start()
    
    messagebox.showinfo("Monitoramento", "Monitoramento iniciado! O programa continuará rodando em segundo plano.")
    
    # Fechar a interface e mover para bandeja do sistema
    root.withdraw()
    threading.Thread(target=executar_bandeja, daemon=True).start()

def executar_bandeja():
    """Cria um ícone na bandeja do sistema"""
    image = Image.new('RGB', (64, 64), (0, 0, 255))  # Ícone azul simples

    menu = (item('Sair', sair_programa),)
    icon = Icon("MonitorCopias", image, menu=menu)
    icon.run()

def sair_programa(icon, item):
    """Para o monitoramento e fecha o programa"""
    global observer
    if observer:
        observer.stop()
        observer.join()
    icon.stop()
    sys.exit()

# Criar a janela principal
root = tk.Tk()
root.title("Configuração do Monitor de Cópia")

tk.Label(root, text="Selecione a pasta a ser monitorada:").pack(pady=5)
tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta_origem).pack()

tk.Label(root, text="Selecione a pasta de destino:").pack(pady=5)
tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta_destino).pack()

tk.Button(root, text="Iniciar Monitoramento", command=iniciar_monitoramento).pack(pady=20)

# Carregar configurações salvas (se existirem)
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        lines = f.readlines()
        if len(lines) >= 2:
            watch_folder = lines[0].strip()
            destination_folder = lines[1].strip()

# Rodar interface
root.mainloop()
