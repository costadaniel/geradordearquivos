#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from time    import time
from os      import urandom
from hashlib import md5, sha256

def generate_random_file(tamanho):
    #Cria arquivo
    arquivo = open("RandomFile.bin", "w+b")

    #Começa a medir o tempo de execução da criação do arquivo.
    comeco = time()
    #Escreve os bytes aleatórios no arquivo de acordo com o tamanho desejado
    arquivo.write(urandom(tamanho))
    #Calcula o tempo de criação do arquivo
    tempo =  int(time() - comeco)
    arquivo.close()

    #Reabre o arquivo para realizar calcular os Hashes dele.
    arquivo = open("RandomFile.bin", "rb")
    temp = arquivo.read()
    hash_md5 = md5(temp).hexdigest()
    hash_sha256 = sha256(temp).hexdigest()
    del temp
    arquivo.close()
    #Quando o processo for terminado mostra o tempo de criação do arquivo e hashes para verificação de integridade
    print("Arquivo gerado em "+str(tempo)+" segundos.\nMD5: "+str(hash_md5)+"\nSHA256: "+str(hash_sha256))

def main():
    #Chamada do programa com o tamanho definido pela linha de comando '$python generaterandomfiles.py tamanho'.
    if len(sys.argv)>1:
        tamanho = int(sys.argv[1])
    #Caso o programa seja executado sem argumento de tamanho o usuário deve definir o tamanho pelo teclado.
    else:
        tamanho = int(input("Entre com o tamanho em BYTES desejado para a criação do arquivo: "))

    #Chamada do da função
    generate_random_file(tamanho)    

if __name__ == '__main__':
    main()
 
