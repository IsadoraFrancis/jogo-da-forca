import tkinter as tk
from tkinter import messagebox
import random

palavras = ['aranha', 'computador', 'python', 'openai', 'banana']

class JogoForcaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("400x500")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.criar_widgets()
        self.novo_jogo()

    def criar_widgets(self):
        self.titulo = tk.Label(self.root, text="Jogo da forca", font=("Arial", 24, "bold"), bg="white")
        self.titulo.pack(pady=10)

        self.label_palavra_info = tk.Label(self.root, text="Palavra Escolhida:", font=("Arial", 14), bg="white")
        self.label_palavra_info.pack()

        self.label_palavra = tk.Label(self.root, text="", font=("Courier", 30), bg="white")
        self.label_palavra.pack(pady=10)

        self.label_erradas_info = tk.Label(self.root, text="Tentativas erradas:", font=("Arial", 14), bg="white")
        self.label_erradas_info.pack()

        self.label_erradas = tk.Label(self.root, text="", font=("Courier", 20), fg="red", bg="white")
        self.label_erradas.pack(pady=10)

        self.label_palpite = tk.Label(self.root, text="Seu Palpite", font=("Arial", 12), bg="white")
        self.label_palpite.pack()

        self.entrada = tk.Entry(self.root, font=("Arial", 14), width=10, justify='center')
        self.entrada.pack(pady=5)

        self.botao_jogar = tk.Button(self.root, text="Fazer jogo", font=("Arial", 12), bg="#007bff", fg="white",
                                     activebackground="#0056b3", width=15, command=self.tentar_letra)
        self.botao_jogar.pack(pady=10)

        self.botao_reset = tk.Button(self.root, text="Reset", font=("Arial", 12), bg="#dc3545", fg="white",
                                     activebackground="#a71d2a", width=15, command=self.novo_jogo)
        self.botao_reset.pack()

    def novo_jogo(self):
        self.palavra = random.choice(palavras)
        self.letras_descobertas = ['_' for _ in self.palavra]
        self.letras_erradas = []
        self.tentativas = 6
        self.atualizar_tela()

    def tentar_letra(self):
        letra = self.entrada.get().lower()
        self.entrada.delete(0, tk.END)

        if not letra.isalpha() or len(letra) != 1:
            messagebox.showwarning("Erro", "Digite uma única letra.")
            return

        if letra in self.letras_descobertas or letra in self.letras_erradas:
            return

        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.letras_descobertas[i] = letra
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1

        self.atualizar_tela()

        if '_' not in self.letras_descobertas:
            self.fim_de_jogo(True)
        elif self.tentativas == 0:
            self.fim_de_jogo(False)

    def atualizar_tela(self):
        self.label_palavra.config(text=' '.join(self.letras_descobertas))
        self.label_erradas.config(text=' '.join(self.letras_erradas))

    def fim_de_jogo(self, venceu):
        if venceu:
            msg = f"Parabéns! Você acertou a palavra: {self.palavra}"
        else:
            msg = f"Você perdeu! A palavra era: {self.palavra}"

        resposta = messagebox.askyesno("Jogar novamente?", msg + "\n\nDeseja jogar novamente?")
        if resposta:
            self.novo_jogo()
        else:
            messagebox.showinfo("Fim", "Obrigado por jogar!")
            self.root.quit()

# Rodar o jogo
root = tk.Tk()
JogoForcaGUI(root)
root.mainloop()
