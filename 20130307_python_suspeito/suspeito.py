SUSPEITO = "Donald Duck Knuth"
LOCAL = "Tokio"
ARMA = "Trebuchet"
TEORIA_CORRETA = (SUSPEITO, LOCAL, ARMA)
LISTA_SUSPEITOS = [
    "Charles B. Abbage",
    "Donald Duck Knuth",
    "Ada L. Ovelace",
    "Alan T. Uring",
    "Ivar J. Acobson",
    "Ras Mus Ler Dorf",]
    
LISTA_ARMAS = [
    "Peixeira",
    "DynaTAC 8000X",
    "Trezoitão",
    "Trebuchet",
    "Maça",
    "Gládio",]
    
LISTA_LOCAIS = [
    "Redmond",
    "Palo Alto",
    "San Francisco",
    "Tokio",
    "Restaurante no Fim do Universo",
    "São Paulo",
    "Cupertino",
    "Helsinki",
    "Maida Vale",
    "Toronto",]
    
    
class Testemunha(object):

    def __init__(self, suspeito, local, arma):
        self.suspeito = suspeito
        self.local = local
        self.arma = arma
        
    def answer(self, suspeito, local, arma):
        if(arma != ARMA):
            return 3
        if(local != LOCAL):
            return 2
        if(suspeito != SUSPEITO):
            return 1
        return 0  
    
def detetive():
    return (LISTA_SUSPEITOS[1], LISTA_LOCAIS[3], LISTA_ARMAS[3])
