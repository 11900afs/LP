# Gera os números de fibonacci, a constante fi (de fibonaci) e com erro estimado

import time # para medição dos tempos de execução de funções

FI = 3.3598856662 # constante de fibonacci com 10 casa decimais

# função para gerar números de fibonacci
def fibonacci(number_of_terms):
    """Gera uma lista com os números de Fibonacci"""
    count = 0
    a = 0
    b = 1
    list = []

    while (count < number_of_terms):
        list.append(a)
        next_number = a + b
        a = b
        b = next_number
        count += 1
    return list

# função para gerar a constante fi de fibonacci
def fi(list):
    fi = 0.0
    for i in list:
        fi += 1 / (i + 1)
    return fi

# função main
def main():
    number_of_terms = int(input("Quantos termos de fibonacci necessita? :"))
    if (number_of_terms <= 0):
        print("O número de termos deve ser maior ou igual a 0")
    else:
        list = fibonacci(number_of_terms)
        print("Cálculo dos primeiros " + str(number_of_terms) +  " termos de fibonacci")
        for i in list:
                print(i, end = " ")

        start_time = time.time()
        fi_constant = fi(list)  # constante de fibonacci para o número de termos indicados
        end_time = time.time()
        total_execution_time = end_time - start_time

        print(" --> Cálculo de fi para " + str(number_of_terms) +  " termos:", fi_constant)
        print("O Erro estimado com este numero de termos é de:", fi_constant - FI)
        print(total_execution_time)

main()


