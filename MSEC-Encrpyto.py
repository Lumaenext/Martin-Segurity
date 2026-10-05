import hashlib
import os
import tkinter as tk

def criptografa(caminho_arquivo):
    if not caminho_arquivo or not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado!")
        return

    # Lendo o conteúdo do arquivo
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Gerando o hash SHA-256
    cripto = hashlib.sha256()
    cripto.update(conteudo[::-1].encode("utf-8"))
    hash_hex = cripto.hexdigest()

    # Escrevendo o hash no novo arquivo
    novo_nome = caminho_arquivo + "_MSEC"
    with open(novo_nome, "w", encoding="utf-8") as nf:
        nf.write(hash_hex)

    os.remove(caminho_arquivo)
    print(f"Arquivo processado e salvo como: {novo_nome}")

# Interface Tkinter

janela = tk.Tk()
janela.title("Martin Security")
janela.geometry("400x300")

titulo = tk.Label(janela, text="MSEC - Encryption", font=("Arial", 20), fg="green")
titulo.pack(pady=10)

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

botao = tk.Button(janela, text="ENVIAR", command=lambda: criptografa(entrada.get()))
botao.pack(pady=10)

janela.mainloop()