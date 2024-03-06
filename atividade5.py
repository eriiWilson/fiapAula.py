tamanho_arquivo = float(input('Qual o tamanho do arquivo (em MB)?: '))
velocidade_download = float(input('Qual a velocidade do seu download (em Mbps)?: '))


download_minuto = velocidade_download / 8 * 60  

tempo_download_minuto = tamanho_arquivo / download_minuto

horas = int(tempo_download_minuto // 60)
minutos = int(tempo_download_minuto % 60)
print(f'O tempo esperado de download: {horas} horas e {minutos} minutos')
