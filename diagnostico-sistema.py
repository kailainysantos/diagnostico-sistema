import os
import socket
import psutil
import platform

# Função para verificar o espaço em disco
def verificar_espaco_disco():
    disco = psutil.disk_usage('/')
    if disco.percent > 80:
        return f'Alerta: O espaço no disco está acima de 80%. Utilização: {disco.percent}%'
    else:
        return f'Espaço no disco OK. Utilização: {disco.percent}%'

# Função para verificar a conexão com a Internet
def verificar_conexao_internet():
    try:
        # Tentando se conectar ao Google
        socket.create_connection(('www.google.com', 80), timeout=10)
        return 'Conexão com a Internet está OK.'
    except (socket.timeout, socket.gaierror):
        return 'Erro: Não foi possível conectar à Internet.'

# Função para verificar a versão do sistema operacional
def verificar_sistema():
    sistema = platform.system()
    versao = platform.version()
    return f'Sistema operacional: {sistema} {versao}'

# Função para verificar o uso de memória
def verificar_memoria():
    memoria = psutil.virtual_memory()
    if memoria.percent > 80:
        return f'Alerta: Uso de memória está acima de 80%. Uso atual: {memoria.percent}%'
    else:
        return f'Uso de memória OK. Uso atual: {memoria.percent}%'

# Função principal para rodar os diagnósticos
def diagnosticar_sistema():
    print('Iniciando diagnóstico...')
    print(verificar_sistema())
    print(verificar_espaco_disco())
    print(verificar_conexao_internet())
    print(verificar_memoria())
    print('Diagnóstico concluído.')

# Chamar a função de diagnóstico
diagnosticar_sistema()
