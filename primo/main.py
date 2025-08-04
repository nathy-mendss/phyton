def main():
    numero = int (input ("digite um número: "))


    i = 2

    while numero != i and numero != 1:
        if numero % i == 0:
            break
        i += 1
    if numero == i:
        print("O numero", numero, "é primo")
    elif numero == i:
        print("O numero 1 não é primo")
    else:
        print("o numero", numero, "não primo porque é divisivel po", i)
    


    return 0
main()