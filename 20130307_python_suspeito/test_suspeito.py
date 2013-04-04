import unittest
from suspeito import Testemunha, detetive, SUSPEITO,LOCAL,ARMA


class TestTestemunha(unittest.TestCase):

    def test_tudo_correto(self):
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertEqual(0, testemunha.answer(SUSPEITO, LOCAL, ARMA))
        
    def test_arma_errada(self):
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertEqual(3, testemunha.answer(SUSPEITO, LOCAL, "Trezoitão"))
        
    def test_local_errado(self):
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertEqual(2, testemunha.answer(SUSPEITO, "Redmond", ARMA))    
        
    def test_suspeito_errado(self):
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertEqual(1, testemunha.answer("Charles B. Abbage", LOCAL, ARMA))
        
    def test_arma_local_errados(self):
        lista = (2,3,)
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertIn(testemunha.answer(SUSPEITO, "Palo Alto", 'DynaTAC 8000X'), lista)
        
    def test_suspeito_arma_errados(self):
        lista = [1,3]
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertIn(testemunha.answer("Charles B. Abbage", LOCAL, 'Peixeira'), lista)
    
    def test_suspeito_local_errados(self):
        lista = [1,2]
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertIn(testemunha.answer("Charles B. Abbage", "Redmond", ARMA), lista)
        
    def test_tudo_errado(self):
        testemunha = Testemunha(SUSPEITO, LOCAL, ARMA)
        self.assertNotEqual(0, testemunha.answer("Charles B. Abbage", "Redmond", 'Peixeira'))
   
   
class TestDetetive(unittest.TestCase):
                 
    def test_tudo_correto(self):
        self.assertEqual((SUSPEITO,LOCAL,ARMA), detetive())

    def test_arma_errada(self):
        self.assertNotEqual((SUSPEITO,LOCAL,'Peixeira'), detetive())
               
    def test_suspeito_errado(self):
        self.assertNotEqual(("Ada L. Ovelace", LOCAL, ARMA), detetive())
                  
    def test_local_errado(self):
        self.assertNotEqual((SUSPEITO, 'São Paulo', ARMA), detetive())
    
    
        
unittest.main()
        
