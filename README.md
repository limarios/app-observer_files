# 📁 Monitor de Cópia Automática de Arquivos

Este é um utilitário Python com interface gráfica (GUI) que monitora uma pasta em tempo real e copia automaticamente arquivos novos para uma pasta de destino. Ideal para automatizar cópias de arquivos de entrada em sistemas que precisam receber arquivos de uma origem comum.


## 🚀 Funcionalidades

- 📂 Interface gráfica para seleção das pastas.

- 👁️ Monitoramento automático de novos arquivos com watchdog.

- 📥 Cópia imediata para a pasta de destino.

- 🛠️ Armazena configurações da última execução.

- 🖥️ Funciona em segundo plano com ícone na bandeja do sistema.

- ✅ Compatível com Windows, Linux e macOS.



## 🧰 Tecnologias Utilizadas

- ``tkinter`` – Interface gráfica.

- ``watchdog`` – Monitoramento de sistema de arquivos.

- ``pystray`` – Ícone na bandeja do sistema.

- ``Pillow (PIL)`` – Para criar o ícone da bandeja.

- ``shutil`` – Cópia de arquivos.

- ``threading, os, time`` – Utilitários do sistema e execução em paralelo.



## 📦 Instalação

#### 1. Clone o repositório
```
git clone https://github.com/seu-usuario/app-observer_files.git
cd app-observer_files
```

#### 2. Crie um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

#### 3. Instale as dependências
```
pip install watchdog pystray pillow
```


## ▶️ Como Usar

1. Execute o script:

    ```
    python monitor_copias.py
    ```


2. Na interface gráfica:

    - Clique em "Selecionar Pasta" para escolher a pasta a ser monitorada.

    - Clique em "Selecionar Pasta" para escolher a pasta de destino.

    - Clique em "Iniciar Monitoramento".


3. O programa:

    - Salva as configurações em config.txt.

    - Começa a rodar em segundo plano.

    - Exibe um ícone azul na bandeja do sistema.

4. Para encerrar, clique com o botão direito no ícone da bandeja e selecione "Sair".



## 📝 Observações

- O monitoramento não é recursivo: apenas arquivos criados diretamente na pasta de origem serão copiados.

- Existe um pequeno delay para garantir que o arquivo esteja totalmente salvo antes da cópia (time.sleep(1)).

- O programa não exclui ou move os arquivos originais, apenas faz uma cópia.



## 🔒 Permissões

Certifique-se de que o script tenha permissões suficientes para ler a pasta de origem e escrever na pasta de destino.



## 🛠️ Possíveis Melhorias Futuras

- Monitoramento recursivo (subpastas).

- Suporte a múltiplas pastas de origem.

- Log detalhado com arquivos copiados.

- Configuração de filtros (por extensão, tamanho, etc).



## 📄 Licença

Este projeto está licenciado sob a MIT License.


## 🤝 Contribuições

Contribuições são bem-vindas! 
Sinta-se livre para abrir issues ou pull requests.