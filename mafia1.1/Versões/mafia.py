import random
import time
import os

Jogadores = []
Classes = []
salvados = [""]
Atribuido = {}

def cadastraJogadores():
    jogador = ""
    numJog=0
    while True:
        numJog = int(input("--Diga quantos jogadores terá: "))
        if numJog < 5:
            print("Numero de jogadores menor que 5, insuficiente, digite novamente")
        elif numJog >=10:
            print("Numero de jogadores maior que o permitido(9), digite novamente")
        else:
            break
    for x in range(numJog):
        n = x+1
        while True:
            jogador=input("--Nome do Jogador %d: "%n)
            ver=verificaJogadoremJogadores(jogador)
            if ver == 0:
                print("Jogadores nao podem ter o mesmo nome, digite novamente")
            elif ver == 1:
                if jogador != "":
                    Jogadores.insert(x,jogador)
                    break
                elif jogador == "":
                    print("Jogador precisa ter um nome, digite novamente")
    random.shuffle(Jogadores)
    os.system('cls')
    return numJog

def criaClasses(numJog):
    #numJog = cadastraJogadores()
    if numJog < 5:
        print("Número mínimo não alcançado")
        return
    elif numJog < 10:
        if numJog == 5:
            Classes.insert(0,"Mafia")
            Classes.insert(1,"Medico")
            Classes.insert(2,"Suicida")
            Classes.insert(3,"Civil 1")
            Classes.insert(4,"Civil 2")
        elif numJog == 6:
            Classes.insert(0,"Mafia")
            Classes.insert(1,"Medico")
            Classes.insert(2,"Suicida")
            Classes.insert(3,"Civil 1")
            Classes.insert(4,"Civil 2")
            Classes.insert(5,"Civil 3")
        elif numJog == 7:
            Classes.insert(0,"Mafia")
            Classes.insert(1,"Sacerdote")
            Classes.insert(2,"Medico")
            Classes.insert(3,"Suicida")
            Classes.insert(4,"Civil 1")
            Classes.insert(5,"Civil 2")
            Classes.insert(6,"Civil 3")
        elif numJog == 8:
            Classes.insert(0,"Mafia")
            Classes.insert(1,"Sacerdote")
            Classes.insert(2,"Medico")
            Classes.insert(3,"Detetive")
            Classes.insert(4,"Suicida")
            Classes.insert(5,"Civil 3")
            Classes.insert(6,"Civil 4")
            Classes.insert(7,"Civil 5")
        elif numJog == 9:
            Classes.insert(0,"Mafia")
            Classes.insert(1,"Sacerdote")
            Classes.insert(2,"Medico")
            Classes.insert(3,"Detetive")
            Classes.insert(4,"Suicida")
            Classes.insert(5,"Civil 3")
            Classes.insert(6,"Civil 4")
            Classes.insert(7,"Civil 5")
            Classes.insert(8,"Civil 6")
    return

def atribuicoes():
    #criaClasses()
    qtd=0
    tamC = len(Classes)
    for x in range(tamC):
        classe = Classes[x]
        nomeJogador = Jogadores[x]
        Atribuido[classe] = nomeJogador
        print("--" + classe + ": " + nomeJogador)
    #print(Atribuido["Mafia"])
    #print(Atribuido)
    return

def mostraJogadores():
    print("------Lista dos Jogadores:")
    for x in Atribuido:
        print(x + ": " + Atribuido[x])
    return

def mataJogador(acusado, qtd, mafia, suicida, qtdM):
    tamAtribuido = len(Atribuido)
    qtdAcusando = tamAtribuido - qtdM - 1
    metadeAcusando = qtdAcusando//2
    if qtd>metadeAcusando:
        if acusado == mafia:
            return 0 #acusado era o mafia, fim de jogo
        elif acusado == suicida:
            return 2 #acusado era o suicida, fim de jogo
        
        else:
            for x in Atribuido:
                if acusado == Atribuido[x]:
                    Atribuido[x] = "morto"
                    #Jogadores.remove(acusado)
                    return 3 #acusado nao era o mafia, continua
    else:
        return 1 #Ninguem morreu
        
    return 1

def verificaJogador(nome):
    for x in Atribuido:
        if nome == Atribuido[x]:
            return 0 #ACHOU
    return 1 #NAO ACHOU

def verificaJogadoremJogadores(nome):
    for x in Jogadores:
        if nome == x:
            return 0 #ACHOU
    return 1 #NAO ACHOU

def qtdMortos(): #Conta quantas pessoas estao mortas
    qtd = 0
    for x in Atribuido:
        if Atribuido[x] == "morto":
            qtd = qtd + 1
    return qtd

def scriptNoite():

    vitimaNoite = ""
    vitimaSacerdote = "."
    ultimoSalvado = len(salvados) - 1
    tamAtribuido = len(Atribuido)
    mafia = Atribuido["Mafia"]

    vitimas = []
    
    if tamAtribuido == 7 or tamAtribuido == 8 or tamAtribuido ==9:
        sacerdote = Atribuido["Sacerdote"]
    if tamAtribuido == 8 or tamAtribuido == 9:
        detetive = Atribuido["Detetive"]

    ########MAFIA#########    
    while True:
        vitimaNoite = input("Se você pegou o mafia, digite quem você quer matar: ")
        verifica = verificaJogador(vitimaNoite)
        if verifica == 0:
            if vitimaNoite == mafia: #Mafia nao pode se matar
                print("Mafia nao pode se matar")
            else:
                break
        elif verifica == 1:
            print("--Nome passado nao corresponde aos jogadores disponiveis")
    ##################################

    ########SACERDOTE#########
    if tamAtribuido == 7 or tamAtribuido == 8 or tamAtribuido == 9:       
        while True:
            respSacerdote = input("Se você pegou o sacerdote, me fale se quer matar(s/n): ")
            if sacerdote != "morto":
                if respSacerdote == "s":
                    while True:
                        vitimaSacerdote = input("--Quem: ")
                        verifica = verificaJogador(vitimaSacerdote)
                        if verifica == 0:
                            if vitimaSacerdote == sacerdote: #Sacerdote nao pode se matar
                                print("Sacerdote nao pode se matar")
                            else:
                                break
                        elif verifica == 1:
                            print("--Nome passado nao corresponde aos jogadores disponiveis")
                    break
                elif respSacerdote == "n":
                    break
            else:
                vitimaSacerdote = "." #Se o Sacerdote estiver morto, nao pode matar ninguem
                break             
    ##################################  

    ########MEDICO#########
    while True:
        salvado = input("Se você pegou o medico, digite quem você quer salvar: ")
        if Atribuido["Medico"] != "morto":
            verifica = verificaJogador(salvado)
            if verifica == 0:
                if salvado != salvados[ultimoSalvado]:
                    salvados.append(salvado)
                    break
                else:
                    print("Nao pode salvar a mesma pessoa duas vezes seguidas")
            elif verifica == 1:
                print("--Nome passado nao corresponde aos jogadores disponiveis")
        else:
            salvado = "" #Se o medico estiver morto nao pode salvar ninguem
            break
    ##################################

    ########DETETIVE#########
    if tamAtribuido == 8 or tamAtribuido == 9:    
        while True:
            investigado = input("Se você pegou o detetive, digite quem você acha que eh mafia: ")
            if Atribuido["Detetive"] != "morto":
                verificaInvestigado = verificaJogador(investigado)
                if verificaInvestigado == 0: #Achou jogador
                    if investigado == Atribuido["Detetive"]:
                        print("Detetive nao pode se investigar, digite novamente")
                    elif investigado == mafia:
                        print("Eh mafia")
                        break
                    else:
                        print("Nao eh mafia")
                        break
                else:
                    print("--Nome passado nao corresponde aos jogadores disponiveis")

    ##################################

    if tamAtribuido == 7 or tamAtribuido == 8 or tamAtribuido == 9:
        if sacerdote != "morto":
            if vitimaSacerdote == mafia:
                vitimas.append(mafia)
                Atribuido["Mafia"] = "morto" #Mata o mafia
            elif vitimaSacerdote == ".":
                vitimaSacerdote = "."
            else:
                if vitimaNoite != sacerdote:
                    if salvado != sacerdote:
                        vitimas.append(sacerdote)
                        Atribuido["Sacerdote"] = "morto"
                else:
                    if salvado == sacerdote:
                        vitimas.append(sacerdote)
                        Atribuido["Sacerdote"] = "morto"

    tamVitimas = len(vitimas)

    os.system('cls')
    if tamVitimas == 0:  #Significa que o sacerdote nao fez nada
        if vitimaNoite == salvado: 
            print("Ninguem morreu essa noite.")
        else:
            for x in Atribuido:
                if vitimaNoite == Atribuido[x]:
                    Atribuido[x] = "morto"
                    #Jogadores.remove(vitimaNoite)
                    break
            print("A vitima da noite foi: %s"%vitimaNoite)
    else:
        if Atribuido["Sacerdote"] == "morto":
            if vitimaNoite == salvado:
                print("A vitima da noite foi: %s"%vitimas[0])
            else:
                for x in Atribuido:
                    if vitimaNoite == Atribuido[x]:
                        Atribuido[x] = "morto"
                        #Jogadores.remove(vitimaNoite)
                        break
                print("As vitimas da noite foram: %s e %s"%(vitimaNoite,vitimas[0]))
        elif Atribuido["Mafia"] == "morto":
            if vitimaNoite == salvado:
                print("A vitima da noite foi: %s"%vitimas[0])
            else:
                for x in Atribuido:
                    if vitimaNoite == Atribuido[x]:
                        Atribuido[x] = "morto"
                        #Jogadores.remove(vitimaNoite)
                        break
                print("As vitimas da noite foram: %s e %s"%(vitimaNoite,vitimas[0]))
    
    return

def scriptDia():
    
    mafia = Atribuido["Mafia"]
    suicida = Atribuido["Suicida"]
    tamAtribuido = len(Atribuido)

    acusado = ""
    ver = "a"
    
    qtdAcusacoes = 0
    qtdMortoss = qtdMortos()
    qtdVivos = tamAtribuido - qtdMortoss
    
    if qtdVivos == 2:
        return 2 #MAFIA GANHOU

    if mafia == "morto":
        return 0
    
    print("Amanheceu, vocês tem 2 minutos para conversar")
    while True:
        acusacao = input("--Alguem fez alguma acusação?(s/n): ")
        if acusacao == "s":
            break
        elif acusacao == "n":
            break
        else:
            print("Por favor, digite (s/n)")
    while acusacao=="s":
        while True:
            os.system('cls')
            acusado = input("--Nome do acusado: ")
            verifica = verificaJogador(acusado)
            if verifica == 0:
                break
            print("--Nome passado nao corresponde aos jogadores disponiveis")
        print("Acusado pode fazer sua defesa")
        print("Me mandem mensagem dizendo se querem ou nao matar o acusado(s/n)")
        for x in Atribuido:
            if acusado != Atribuido[x]: #Acusado nao pode votar
                if Atribuido[x] != "morto": #Morto nao pode votar
                    while True:
                        ver = input(Atribuido[x] + ":")
                        if ver == "s":
                            qtdAcusacoes = qtdAcusacoes + 1
                            break
                        elif ver == "n":
                            break
                        print("Mensagem nao valida, por favor digite (s/n)")

        matanca = mataJogador(acusado,qtdAcusacoes,mafia,suicida,qtdMortoss)
        if matanca == 0:
            return 0 #ACABOU O JOGO
        elif matanca == 3:
            print("O acusado: " + acusado + " morreu")
            print("Continua o jogo")
            return 4 #ACABOU O DIA
        elif matanca == 2:
            return 3 #ACABOU O JOGO
        elif matanca == 1:
            print("Votos nao suficiente para matar")
        acusacao = input("--Alguem fez alguma acusação?(s/n): ")

    os.system('cls')
    
    return 1

def jogo():

    numJog=cadastraJogadores()
    criaClasses(numJog)
    atribuicoes()
    
    print("-------------ANOITECEU-------------")
    scriptNoite()
    print("-------------AMANHECEU-------------")
    mostraJogadores()
    dia = scriptDia()
    
    while dia == 1 or dia ==4:
        
        print("-------------ANOITECEU-------------")
        mostraJogadores()
        scriptNoite()
        
        print("-------------AMANHECEU-------------")
        mostraJogadores()
        dia = scriptDia()
    if dia==0:
        print("Mafia morreu")
        print("Cidade ganhou!!!")
        time.sleep(15)
        return
    elif dia==2:
        print("Mafia ganhou!!!")
        time.sleep(15)
        return
    elif dia==3:
        print("Suicida morreu")
        print("Suicida ganhou!!!")
        time.sleep(15)
        return

    return

jogo()
