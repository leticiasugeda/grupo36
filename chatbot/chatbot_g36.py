import pandas as pd
import os
import sys

class Tree():
    def __init__(self):
        pass

    def ask_question(self):
        return self.question

    def check_answer(self,answer):
        if answer == self.answerTrue:
            return self.leftNode
        elif answer == self.answerFalse:
            return self.rightNode
        else:
            return False

texto = pd.read_csv("arvore_grupo36.csv",sep=';',index_col="ID")

def rec_build_tree(linha):
    row = texto.loc[linha]
    if row["Pergunta"] == "NÓ FOLHA":
        return row["A"]
    node = Tree() 
    node.leftNode = rec_build_tree(int(row["Nó A"]))    
    node.rightNode = rec_build_tree(int(row["Nó B"]))
    node.question = row["Pergunta"]
    node.answerTrue = row["A"]
    node.answerFalse = row["B"]
    return node

def is_obj(obj):
    return False if type(obj).__name__ == "str" else True

counter_tickets = 0
while True:
    arvore = rec_build_tree(1)
    count_erros=0
    while True:
        if count_erros == 2:
            print("ERROS SUCESSIVOS\nVERIFIQUE AS OPÇÕES ANTES DE TENTAR NOVAMENTE\n")
            print("\nMuitas informações! :/ \nPor favor me reinicie.")
            break
        opcoes = {1:arvore.answerTrue,2:arvore.answerFalse}
        print("\nEscolha uma das opções abaixo:"+"\n0 para sair"+"\n1 para "+opcoes[1]+"\n2 para "+opcoes[2]+"\n")
        response = input(arvore.ask_question())
        while not response.isnumeric():
            if count_erros == 2:
                print("\nMuitas informações! :/ \nPor favor me reinicie.")
                sys.exit()
            print("\nMe desculpe, não conheço essa opção, vamos tentar novamente? :)\n")
            print("Escolha uma das opções abaixo:"+"\n0 para sair"+"\n1 para "+opcoes[1]+"\n2 para "+opcoes[2])
            response = input(arvore.ask_question())
            count_erros+=1
            
        if int(response) == 0:
            print("\nFim.\n")
            sys.exit()
            
        question = opcoes[int(response)]
        answer = arvore.check_answer(question)
        if answer == False:
            print("\nMe desculpe, não conheço essa opção, vamos tentar novamente? :)")
            count_erros+=1
        elif not is_obj(answer):
            break
        else:
            arvore = answer 
            
    print(answer)
                
    print("-------------------------------------")