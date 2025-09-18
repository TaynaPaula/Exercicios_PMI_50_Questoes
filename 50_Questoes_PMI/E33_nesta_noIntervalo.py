#Crie um programa que verifique se um número está em um intervalo
n =0
while n < 40 or n > 50:
    try:
        s = (input("digite um valor no intervalo de [40, 50]:"))
        n = int (s)
    except:
        print("{} não é um número.".format(s))
        n=0
        
    else:
        if n <40 or n >50:
            print("o valor lido {} esta forra do intervalo" .format(n))
        else:
            print("o valor lido {} esta ok" .format(n))
            break 
        
    finally:
        print("\n\n");#repetição do código
    