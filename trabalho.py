from historia import texto
from historia import escolhas

lanterna = 0
espingarda = 0
balas = 0
chave_metal = 0
senha = 0
chave_saida = 0
monstro_sala_cirurgica = 0

def jogo():
    texto.intro()
    quarto()

def reiniciar():
    while True:
        escolhas.pergunta_reiniciar()
        resposta_reiniciar = int(input())
        if resposta_reiniciar == 1:
            jogo()
        elif resposta_reiniciar == 2:
            texto.agradecimento()
            exit()
        else:
            texto.opcao_invalida()

def quarto():
    while True:
        escolhas.escolha_quarto()
        opcoes_quarto = int(input())
        if opcoes_quarto == 1:
            texto.morte_dormindo()
            reiniciar()
        elif opcoes_quarto == 2:
            texto.analisar_quarto()
            quarto_examinado()
        else:
            texto.opcao_invalida()

def quarto_examinado():
    global chave_metal
    while True:
        escolhas.escolha_quarto_examinado()
        opcoes_quarto_examinado = int(input())
        if opcoes_quarto_examinado == 1:
            texto.morte_cama()
            reiniciar()
        elif opcoes_quarto_examinado == 2 and chave_metal == 0:
            texto.check_porta_metal_falha()
        elif opcoes_quarto_examinado == 2 and chave_metal == 1:
            texto.check_porta_metal_sucesso()
            corredor_duas_portas()
        elif opcoes_quarto_examinado == 3 and chave_metal == 0:
            texto.mesa_de_metal()
            chave_metal += 1
        elif opcoes_quarto_examinado == 3 and chave_metal == 1:
            texto.mesa_de_metal_vazia()
        else:
            texto.opcao_invalida()

def corredor_duas_portas():
    while True:
        escolhas.escolha_corredor_duas_portas()
        opcoes_corredor_duas_portas = int(input())
        if opcoes_corredor_duas_portas == 1 and espingarda == 1 and balas == 1 and lanterna == 1:
            texto.corredor_duas_portas_esquerda_vitoria()
            sala_seguranca()
        elif opcoes_corredor_duas_portas == 1 and (espingarda == 0 or balas == 0 or lanterna == 0):
            texto.corredor_duas_portas_esquerda_morte()
            reiniciar()
        elif opcoes_corredor_duas_portas == 2:
            texto.porta_recepcao()
            recepcao()
        else:
            texto.opcao_invalida()

def sala_seguranca():
    texto.check_sala_seguranca()
    if senha == 0:
        texto.check_sala_seguranca_falhou()
    elif senha == 1:
        texto.check_sala_seguranca_sucesso()
        texto.final_revelacao()
        texto.agradecimento()
        exit()

def recepcao():
    global lanterna
    while True:
        escolhas.escolha_recepcao()
        opcoes_recepcao = int(input())
        if opcoes_recepcao == 1 and lanterna == 0:
            texto.mesa_recepcao()
            lanterna += 1
        elif opcoes_recepcao == 1 and lanterna == 1:
            texto.mesa_recepcao_vazia()
        elif opcoes_recepcao == 2 and chave_saida == 0:
            texto.check_porta_saida_falha()
        elif opcoes_recepcao == 2 and chave_saida == 1:
            texto.check_porta_saida_sucesso()
            texto.final_fuga()
            texto.agradecimento()
            exit()
        elif opcoes_recepcao == 3:
            texto.entrar_corredor_tres_portas()
            corredor_tres_portas()
        elif opcoes_recepcao == 4:
            corredor_duas_portas()
        else:
            texto.opcao_invalida()

def corredor_tres_portas():
    global balas, monstro_sala_cirurgica, espingarda
    while True:
        escolhas.escolha_tres_portas()
        opcoes_tres_portas = int(input())
        if opcoes_tres_portas == 1 and espingarda == 1 and balas == 1:
            texto.sala_cirurgica()
            texto.check_sala_cirurgica_sucesso()
            balas -= 1
            monstro_sala_cirurgica += 1
        elif opcoes_tres_portas == 1 and (espingarda == 0 or balas == 0):
            texto.sala_cirurgica()
            texto.check_sala_cirurgica_falha()
            reiniciar()
        elif opcoes_tres_portas == 1 and monstro_sala_cirurgica == 1:
            texto.sala_cirurgica_vazia()
        elif opcoes_tres_portas == 2:
            sala_enfermagem()
        elif opcoes_tres_portas == 3:
            texto.deposito()
            espingarda += 1
            balas += 1
        elif opcoes_tres_portas == 4:
            recepcao()
        else:
            texto.opcao_invalida()

def sala_enfermagem():
    global chave_saida, senha
    while True:
        escolhas.escolha_enfermagem()
        opcoes_enfermagem = int(input())
        if opcoes_enfermagem == 1:
            texto.armario_enfermagem()
            senha += 1
        elif opcoes_enfermagem == 1 and senha == 1:
            texto.armario_enfermagem_vazio()
        elif opcoes_enfermagem == 2:
            texto.mesa_enfermagem()
            chave_saida += 1
        elif opcoes_enfermagem == 2 and chave_saida == 1:
            texto.mesa_enfermagem_vazia()
        elif opcoes_enfermagem == 3:
            corredor_tres_portas()
        else:
            texto.opcao_invalida()

jogo()