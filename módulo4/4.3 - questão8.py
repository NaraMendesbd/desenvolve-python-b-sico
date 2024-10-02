def calculadora():
    try:
        resultado = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    while True:
        operacao = input("Digite a operação (+ ou -) ou 'Fim' para encerrar: ")

        if operacao.lower() == "fim":
            break

        if operacao not in ['+', '-']:
            print("Operação inválida! Tente novamente.")
            continue

        try:
            num = float(input("Digite o próximo número: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if operacao == '+':
            resultado += num
        elif operacao == '-':
            resultado -= num

    print("Resultado final:", resultado)

calculadora()