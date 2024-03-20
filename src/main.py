import subprocess


def main():

    print("Compiling program")
    # Compilar o código em C
    subprocess.run(['gcc', '-o', 'src/main', 'src/main.c'])

    print("Compiling done")


    print("Starting C program")

    # Chamar o programa em C e passar dados de entrada
    process = subprocess.Popen('src/main', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Ler a saída do programa em C
    output = process.stdout.readline().strip()
    print(output)


    # Loop para receber entrada do usuário e enviar para o programa em C
    while True:
        user_input = input("")
        process.stdin.write(user_input + '\n')
        process.stdin.flush()  # Limpar o buffer de entrada
        process.stdout.flush()

        # Ler a saída do programa em C
        output = process.stdout.readline().strip()
        print(output)

if __name__ == "__main__":
    main()
