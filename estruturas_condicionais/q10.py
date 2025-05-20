tam_arquivo = float(input("Tamanho do arquivo (MB): "))
velocidade_download = float(input("Velocidade de download (MBps): "))

tempo = tam_arquivo / velocidade_download

if velocidade_download <= 1.00:
    print("Velocidade de download: lenta")
elif 1.00 < velocidade_download < 10.00:
    print("Velocidade de download: intermediária")
else:
    print("Velocidade de download: excelente")

print(f"Tempo para baixar o arquivo é de: {tempo:.2f} s")