# Desafio Extra: Saudação personalizada com a hora atual do sistema
# Importamos o módulo 'datetime' que possui funções para lidar com datas e horas
from datetime import datetime

# Captura o nome do usuário
nome = input("Por favor, digite o seu nome: ")

# Obtém o horário atual do computador
agora = datetime.now()

# Formata a hora para exibir apenas Hora:Minuto (exemplo: 14:35)
# %H representa a hora (00-23) e %M representa os minutos
hora_formatada = agora.strftime("%H:%M")

# Exibe a mensagem final unindo todas as informações
print(f"Olá, {nome}! Agora são {hora_formatada}. Tenha um ótimo dia de estudos!")