from random import random # Função será usada para geração de números aleatórios (geração inicial da população)
import matplotlib.pyplot as plt # Específica para gerar gráficos em python

# Definindo a classe caminhão para posteriomente passar os parâmetros de cada atributo
class Caminhao():
    def __init__(self, identificador, tipo, carregaA, carregaB, carregaC, descarregaA,
                 descarregaB, descarregaC):
        self.identificador = identificador
        self.tipo = tipo
        self.carregaA = carregaA
        self.carregaB = carregaB
        self.carregaC = carregaC
        self.descarregaA = descarregaA
        self.descarregaB = descarregaB
        self.descarregaC = descarregaC
        
'''        
class Individuo():
    def __init__(self, volume_recebidoA, volume_recebidoB, volume_recebidoC,
                 volume_expedidoA, volume_expedidoB, volume_expedidoC, geracao = 0):
        self.volume_recebidoA = volume_recebidoA
        self.volume_recebidoB = volume_recebidoB
        self.volume_recebidoC = volume_recebidoC
        self.volume_expedidoA = volume_expedidoA
        self.volume_expedidoB = volume_expedidoB
        self.volume_expedidoC = volume_expedidoC
        self. geracao = geracao
        self.nota_avaliacao = 0
        self.cromossomo = []
        
        for i in range(len(volume_recebidoA)):
            if random() < 0.5: 
                self.cromossomo.append(Caminhao.identificador[0])
            else:
                self.cromossomo.append("0")
  '''

# Os indivíduos formam as soluções. Cada indivíduo é uma solução específica do problema
# O cromossomo é o parâmetro que vai representar a solução
# O cromossomo é um atributo do indivíduo
class Individuo():
    def __init__(self, identificador, tipo, cA, cB, cC, dA, dB, dC, limite_tanqueA, limite_tanqueB, limite_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC, geracao = 0):
        self.identificador = identificador
        self.tipo = tipo
        self.cA = cA
        self.cB = cB
        self.cC = cC
        self.dA = dA
        self.dB = dB
        self.dC = dC
        self.limite_tanqueA = limite_tanqueA
        self.limite_tanqueB = limite_tanqueB
        self.limite_tanqueC = limite_tanqueC
        self.volume_tanqueA = volume_tanqueA
        self.volume_tanqueB = volume_tanqueB
        self.volume_tanqueC = volume_tanqueC
        self. geracao = geracao
        self.nota_avaliacao = 0
        self.cromossomo = []
        
        
        for i in range(len(tipo)):
            if random() < 0.5: 
                self.cromossomo.append(self.identificador[i])
            else:
                self.cromossomo.append("000")   
    
                
                
    def avaliacao(self, fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, n_baias):
        self.fator_venda = fator_venda
        self.fator_compra = fator_compra
        self.fator_carrega_transferencia = fator_carrega_transferencia
        self.fator_descarrega_transferencia = fator_descarrega_transferencia
        self.n_baias = n_baias
        verifica_num_CTs = 0
        nota_venda = 0.0
        nota_compra = 0.0
        nota_transferencia = 0.0
        soma_cA = 0
        soma_cB = 0
        soma_cC = 0
        soma_dA = 0
        soma_dB = 0
        soma_dC = 0
        
        # Contando quantos caminhões o indivíduo tem
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] != '000':
                verifica_num_CTs = verifica_num_CTs + 1
        
        if verifica_num_CTs <= n_baias:
            for i in range(len(self.cromossomo)):
                if self.cromossomo[i] != '000':
                    soma_cA += self.cA[i]
                    soma_cB += self.cB[i]
                    soma_cC += self.cC[i]
                    soma_dA += self.dA[i]
                    soma_dB += self.dB[i]
                    soma_dC += self.dC[i]
                                
                    if self.tipo[i] == "Venda":
                        nota_venda = nota_venda + (self.fator_venda * (self.cA[i] + self.cB[i] + self.cC[i]))
                    if self.tipo[i] == "Compra":
                        nota_compra = nota_compra + (self.fator_compra * (self.dA[i] + self.dB[i] + self.dC[i]))
                    if self.tipo[i] == "Transferencia":
                        nota_transferencia = nota_transferencia + (self.fator_carrega_transferencia * (self.cA[i] + self.cB[i] + self.cC[i])) + (self.fator_descarrega_transferencia * (self.dA[i] + self.dB[i] + self.dC[i]))
            '''
            #Testando se as somas estão certas (testado e estão ok)
            print('Teste somas')
            print(soma_cA)
            print(soma_cB)
            print(soma_cC)
            print(soma_dA)
            print(soma_dB)
            print(soma_dC)
            
            #Testando se as notas estão certas (testado e estão ok)
            print('Teste notas')
            print(nota_venda)
            print(nota_compra)
            print(nota_transferencia)
            '''
            
            self.volume_tanqueA = volume_tanqueA - soma_cA + soma_dA
            self.volume_tanqueB = volume_tanqueB - soma_cB + soma_dB
            self.volume_tanqueC = volume_tanqueC - soma_cC + soma_dC
            
            
            if (self.volume_tanqueA > self.limite_tanqueA) or (self.volume_tanqueA < 0):
                nota_venda = 1
                nota_compra = 1
                nota_transferencia = 1
                #print("Houve problema de volume no tanque A")
            if (self.volume_tanqueB > self.limite_tanqueA) or (self.volume_tanqueB < 0):
                nota_venda = 1
                nota_compra = 1
                nota_transferencia = 1
                #print("Houve problema de volume no tanque B")
            if (self.volume_tanqueC > self.limite_tanqueA) or (self.volume_tanqueC < 0):
                nota_venda = 1
                nota_compra = 1
                nota_transferencia = 1
                #print("Houve problema de volume no tanque C")
                
        else:
            nota_venda = 1
            nota_compra = 1
            nota_transferencia = 1
            
        self.nota_avaliacao = nota_venda + nota_compra + nota_transferencia
        
            
    def crossover(self, outro_individuo):
        ponto_corte = round(random() * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:ponto_corte] + self.cromossomo[ponto_corte::]
        filho2 = self.cromossomo[0:ponto_corte] + outro_individuo.cromossomo[ponto_corte::]
        
        filhos = [Individuo(self.identificador, self.tipo, self.cA, self.cB, self.cC, self.dA, self.dB, self.dC,
                            self.limite_tanqueA, self.limite_tanqueB, self.limite_tanqueC, self.volume_tanqueA, self.volume_tanqueB, self.volume_tanqueC, self.geracao + 1),
                  Individuo(self.identificador, self.tipo, self.cA, self.cB, self.cC, self.dA, self.dB, self.dC,
                            self.limite_tanqueA, self.limite_tanqueB, self.limite_tanqueC, self.volume_tanqueA, self.volume_tanqueB, self.volume_tanqueC, self.geracao + 1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    
    def mutacao(self, taxa_mutacao):
        # print("Antes %s " % self.cromossomo)
        
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '000':
                    self.cromossomo[i] = self.identificador[i]
                else:
                    self.cromossomo[i] = '000'
        
        # print("Depois %s " % self.cromossomo)        
            
        return self
            
        #for i in range(len(self.cromossomo)):
            #if cromossomo[i] != '000':
        
     # def avaliacao(self):
    #nota = 0
   # soma_espacos = 0
   # for i in range(len(self.cromossomo)):
     #   if self.cromossomo[i] == '1':
      #      nota += self.valores[i]
     #       soma_espacos += self.espacos[i]
     #   if soma_espacos > self.limite_espacos:
      #      nota = 1 # Abaixando muito a nota para cromossomos que ultrapassam o limite do caminhão
      #  self.nota_avaliacao = nota
      #  self.espaco_usado = soma_espacos       
        
        
'''        
class Baias():
    def __init__(self, cA, cB, cC, dA, dB, dC):
        self.cA = cA
        self.cB = cB
        self.cC = cC
        self.dA = dA
        self.dB = dB
        self.dC = dC
'''        

class AlgoritmoGenetico():
    
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
        
    def inicia_populacao(self, identificador, tipo, cA, cB, cC, dA, dB, dC, limite_tanqueA, limite_tanqueB, limite_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(identificador, tipo, cA, cB, cC, dA, dB, dC, limite_tanqueA, limite_tanqueB, limite_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("*******\nMelhor solução da geração %s\n Cromossomo: %s\n Avaliação: %s\n*******" % (self.populacao[0].geracao, melhor.cromossomo, melhor.nota_avaliacao))
        
    def executar(self, taxa_mutacao, num_geracoes, identificador, tipo, cA, cB, cC, dA, dB, dC, limite_tanqueA, limite_tanqueB, limite_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC,
                 fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, n_baias):
        
        self.inicia_populacao(identificador, tipo, cA, cB, cC, dA, dB, dC, limite_tanqueA, limite_tanqueB, limite_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC)
        
        for individuo in self.populacao:
            individuo.avaliacao(fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, n_baias)
            
        self.ordena_populacao()
        
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
        
        self.visualiza_geracao()
        
        for geracao in range(num_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, ag.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
        
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
                
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao(fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, n_baias)
            
            self.ordena_populacao()
        
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.nota_avaliacao)
            self.melhor_individuo(melhor)            
            
        print("\nMelhor solução\nGeração: %s\nAvaliação: %s\nCromossomo: %s" % (self.melhor_solucao.geracao,
                                                                                self.melhor_solucao.nota_avaliacao,
                                                                                self.melhor_solucao.cromossomo))
        
        return self.melhor_solucao.cromossomo
    
            
        
if __name__ == '__main__': 
    # lista_caminhoes = ("identificador", "tipo", "cA", "cB", "cC", "dA", "dB", "dC")
    lista_caminhoes = []
    lista_caminhoes.append(Caminhao("001", "Venda", 15000, 0, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("002", "Venda", 22000, 0, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("003", "Venda", 0, 25000, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("004", "Venda", 0, 0, 18000, 0, 0, 0))
    lista_caminhoes.append(Caminhao("005", "Venda", 0, 18000, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("006", "Compra", 0, 0, 0, 60000, 0, 0))
    lista_caminhoes.append(Caminhao("007", "Compra", 0, 0, 0, 0, 60000, 0))
    lista_caminhoes.append(Caminhao("008", "Compra", 0, 0, 0, 0, 0, 60000))
    lista_caminhoes.append(Caminhao("009", "Transferencia", 0, 58000, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("010", "Transferencia", 0, 0, 0, 0, 0, 58000))
    lista_caminhoes.append(Caminhao("011", "Venda", 15000, 0, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("012", "Venda", 22000, 0, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("013", "Venda", 0, 25000, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("014", "Venda", 0, 0, 18000, 0, 0, 0))
    lista_caminhoes.append(Caminhao("015", "Venda", 0, 18000, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("016", "Compra", 0, 0, 0, 60000, 0, 0))
    lista_caminhoes.append(Caminhao("017", "Compra", 0, 0, 0, 0, 60000, 0))
    lista_caminhoes.append(Caminhao("018", "Compra", 0, 0, 0, 0, 0, 60000))
    lista_caminhoes.append(Caminhao("019", "Transferencia", 0, 58000, 0, 0, 0, 0))
    lista_caminhoes.append(Caminhao("020", "Transferencia", 0, 0, 0, 0, 0, 58000))
    
    # Inicializa as listas vazias que serão usadas no for
    identificadores = []
    tipos = []
    cA = []
    cB = []
    cC = []
    dA = []
    dB = []
    dC = []
        
    # Adiciona nas listas as informações dos produtos 
    for caminhao in lista_caminhoes:
        identificadores.append(caminhao.identificador)
        tipos.append(caminhao.tipo)
        cA.append(caminhao.carregaA)
        cB.append(caminhao.carregaB)
        cC.append(caminhao.carregaC)
        dA.append(caminhao.descarregaA)
        dB.append(caminhao.descarregaB)
        dC.append(caminhao.descarregaC)
        
    # Limite de volume (em litros) dos tanques
    capacidade_tanqueA = 2400000
    capacidade_tanqueB = 2400000
    capacidade_tanqueC = 1500000
    volume_tanqueA = 2350000
    volume_tanqueB = 30000
    volume_tanqueC = 500000
    
    # Importância de cada operação (valores entre 0.5 e 2.5, onde 0.5 é menos importante e 2.5 é mais importante)
    fator_venda = 2
    fator_compra = 1
    fator_carrega_transferencia = 1
    fator_descarrega_transferencia = 0.5
    
    # Número de baias na plataforma
    num_baias = 5
    
    # Indica quantas gerações o algoritmo gerará (critério de parada)
    num_geracoes = 100
    
    # Indica quantos indivíduos por população (necessário para iniciar o Algoritmo Genético)
    tamanho_populacao = 20
    
    # Lista vazia para receber os filhos depois de realizado o crossover entre os pais
    nova_populacao = []
    
    # Taxa de mutação (usada na mutacao)
    prob_mutacao = 0.1
    
    # Iniciando o algoritmo passando o tamanho da população
    ag = AlgoritmoGenetico(tamanho_populacao)
    
    resultado = ag.executar(prob_mutacao, 
                            num_geracoes, 
                            identificadores, 
                            tipos, 
                            cA, cB, cC, 
                            dA, dB, dC, 
                            capacidade_tanqueA, capacidade_tanqueB, capacidade_tanqueC, 
                            volume_tanqueA, volume_tanqueB, volume_tanqueC,
                            fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, 
                            num_baias)
    
    for i in range(len(lista_caminhoes)):
        if resultado[i] != "000":
            if lista_caminhoes[i].carregaA != 0:
                print("Caminhão %s para carregar %s de %s litros de produto A" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo, lista_caminhoes[i].carregaA))
            if lista_caminhoes[i].carregaB != 0:
                print("Caminhão %s para carregar %s de %s litros de produto B" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo, lista_caminhoes[i].carregaB))
            if lista_caminhoes[i].carregaC != 0:
                print("Caminhão %s para carregar %s de %s litros de produto C" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo, lista_caminhoes[i].carregaC))
            if lista_caminhoes[i].descarregaA != 0:
                print("Caminhão %s para receber %s de %s litros de produto A" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo, lista_caminhoes[i].descarregaA))
            if lista_caminhoes[i].descarregaB != 0:
                print("Caminhão %s para receber %s de %s litros de produto B" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo, lista_caminhoes[i].descarregaB))
            if lista_caminhoes[i].descarregaC != 0:
                print("Caminhão %s para receber %s de %s litros de produto C" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo, lista_caminhoes[i].descarregaC))
                
    
    plt.plot(ag.lista_solucoes)
    plt.title("Evolução da avaliação ao longo das gerações")
    plt.show()
    
    
    '''
    for i in ag.lista_solucoes:
        print(i)
    '''      
    ''' Testando passo a passo
    # Iniciando a população passando os parâmetros de cada indivíduo
    ag.inicia_populacao(identificadores, tipos, cA, cB, cC, dA, dB, dC, capacidade_tanqueA, capacidade_tanqueB, capacidade_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC)
    # Avaliando cada indivíduo dentro da população (preenchendo a nota para cada um deles)
    for i in ag.populacao:
        i.avaliacao(fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, num_baias)
    # Ordenando a população de acordo com a nota (ordem decrescente, ou seja, o melhor avaliado ficará na posição 0)
    ag.ordena_populacao()
    # Escolhendo o melhor indivíduo
    ag.melhor_individuo(ag.populacao[0])
    # Somando as avaliações (esse valor será utilizado para a seleção dos indivíduos "pais" para construção da próxima geração)
    soma = ag.soma_avaliacoes()
    # Selecionando os pais para realizar o crossover, realiza o crossover com os pais selecionados e aplica a mutação nos filhos gerados
    for individuos_gerados in range(0, ag.tamanho_populacao, 2):
        pai1 = ag.seleciona_pai(soma)
        pai2 = ag.seleciona_pai(soma)
        
        filhos = ag.populacao[pai1].crossover(ag.populacao[pai2])
        nova_populacao.append(filhos[0].mutacao(prob_mutacao))
        nova_populacao.append(filhos[1].mutacao(prob_mutacao))
    # Substitui os indivíduos da população pelos indivíduos da nova população (a antiga população é descartada)   
    ag.populacao = list(nova_populacao)
    '''
  
        
    '''    
    print("Soma das avaliações: %s" % soma)
    '''
    '''
    print("Melhor solução para o problema: %s\n" % ag.melhor_solucao.cromossomo,
          "Nota: %s" % ag.melhor_solucao.nota_avaliacao)
    '''
    '''
    for i in range(ag.tamanho_populacao):
        print("*** Indivíduo %s *** \n" % i,
              "teve a nota %s \n" % str(ag.populacao[i].nota_avaliacao),              
              "Cromossomo = %s \n" % str(ag.populacao[i].cromossomo))
    '''
    '''
    # Criando um indivíduo de teste totalmente aleatório. Aqui não há inteligência alguma
    individuo1 = Individuo(identificadores, tipos, cA, cB, cC, dA, dB, dC, capacidade_tanqueA, capacidade_tanqueB, capacidade_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC)
    print("\nIndividuo 1")
    for i in range(len(lista_caminhoes)):
        if individuo1.cromossomo[i] != "000":
            print("Caminhão: %s para %s" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo))          
    individuo1.avaliacao(fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, num_baias)
    print("Nota = %s" % individuo1.nota_avaliacao)
    
    individuo2 = Individuo(identificadores, tipos, cA, cB, cC, dA, dB, dC, capacidade_tanqueA, capacidade_tanqueB, capacidade_tanqueC, volume_tanqueA, volume_tanqueB, volume_tanqueC)
    print("\nIndividuo 2")
    for i in range(len(lista_caminhoes)):
        if individuo2.cromossomo[i] != "000":
            print("Caminhão: %s para %s" % (lista_caminhoes[i].identificador, lista_caminhoes[i].tipo))          
    individuo2.avaliacao(fator_venda, fator_compra, fator_carrega_transferencia, fator_descarrega_transferencia, num_baias)
    print("Nota = %s" % individuo2.nota_avaliacao)
    
    individuo1.crossover(individuo2)
    
    individuo1.mutacao(0.05)
    individuo2.mutacao(0.05)
    '''

# 1- COMO FAZER O CROSSOVER TENDO UM CROMOSSOMO COM MAIS DE 5 POSIÇÕES? (QUANDO FIZER O CROSSOVER COM 2 PAIS A CHANCE DO FILHO TER MAIS DE 5 CTS É GRANDE DEMAIS)
# 2- COMO AVALIAR SE O INDIVIDUO NÃO ESCOLHEU MAIS CAMINHÕES DO QUE AS BAIAS PERMITEM (LIMITAÇÃO DE INFRA)
# 3- DEVO IMPLEMENTAR UM FATOR POR PRODUTO TAMBÉM? POR EXEMPLO: FATOR VENDA A, FATOR VENDA B, FATOR VENDA C, FATOR COMPRA A, FATOR COMPRA B... SE SIM, ELE DEVERIA SER EM FUNÇÃO DO VOLUME DO TANQUE?
# (QUANTO MAIS CHEIO O TANQUE, MENOS PRIORITÁRIO É RECEBER E MAIS PIORITÁRIO É EXPEDIR E VICE VERSA)
# 4- OUTRA IDEIA É COLOCAR O FATOR MENCIONADO NO ITEM 3 PRA FICAR EM FUNÇÃO DO FATOR GERAL TAMBEM (FATOR VENDA, FATOR COMPRA, FATOR TRANSFERENCIA)
    