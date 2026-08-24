import random


def jogar():
    """Executa o jogo de adivinhação de números com limite fixo de 6 tentativas."""
    # Define o intervalo numérico do jogo
    limite_inferior = 1
    limite_superior = 24

    # Define o limite fixo de tentativas
    max_tentativas = 6

    # Gerando o número secreto aleatório dentro do limite especificado
    numero_secreto = random.randint(limite_inferior, limite_superior)

    # Mensagens de boas-vindas e regras
    print("=== JOGO DA ADIVINHAÇÃO ===")
    print(
        f"Tente adivinhar o número entre {limite_inferior} e {limite_superior}."
    )
    print(f"Você tem {max_tentativas} tentativas!\n")

    tentativas = 0

    # Loop do jogo
    while tentativas < max_tentativas:
        # Tratamento de erro para garantir que a entrada seja um número inteiro
        try:
            palpite = int(
                input(f"Tentativa {tentativas + 1}: Digite seu palpite: ")
            )
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.\n")
            continue

        # Validação para verificar se o palpite está dentro do limite do jogo
        if palpite < limite_inferior or palpite > limite_superior:
            print(
                f"Palpite fora do limite! Escolha um número entre {limite_inferior} e {limite_superior}.\n"
            )
            continue

        tentativas += 1

        # Verificação do palpite do jogador
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
    else:
        # Mensagem exibida caso as 6 tentativas se esgotem
        print(f"\nFim de jogo! O número secreto era {numero_secreto}.")


# Garante que a função jogar() só seja executada diretamente
if __name__ == "__main__":
    jogar()