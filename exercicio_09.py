# Programa para converter a temperatura de Celsius para Fahrenheit e vice-versa

while True:
    # Verificar em qual unidade a temperatura está.
    tipo_media = input("A unidade de medida está em Celsius (°C) ou Fahrenheit (°F): ")
    if tipo_media[0].upper() != "C" and  tipo_media[0].upper() != "F":
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue
    else:
        # Converter para a temperatura oposta
        valor_temperatura = float(input("Digite o valor da temperatura: "))
        if tipo_media.upper() == "C":
            temperatura_convertida = valor_temperatura * 1.8 + 32
            converter_para = "°F"
        elif tipo_media.upper() == "F":
            temperatura_convertida = (valor_temperatura - 32) / 1.8
            converter_para = "°C"
            
    # Formatação do texto
    formatacao_unidade = f"{temperatura_convertida:.2f} {converter_para}"
    print(f"O valor da medida convertida é: {formatacao_unidade}")
    break
