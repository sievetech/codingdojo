#!/usr/bin/env python3

from unittest import TestCase, main
from palavras_primas import palavras_primas, pegar_numero_da_letra, palavra_numero


class TestPalavrasPrimas(TestCase):

    def teste_a(self):
        entrada = 'a'
        self.assertFalse(palavras_primas(entrada))
        
    def teste_c(self):
        entrada = 'c'
        self.assertTrue(palavras_primas(entrada))
	
    def test_b(self):
        entrada = 'b'
        self.assertTrue(palavras_primas(entrada))

    def test_e(self):
        entrada = 'e'
        self.assertTrue(palavras_primas(entrada))

    def test_ab(self):
        entrada = 'ab'
        self.assertTrue(palavras_primas(entrada))
		
    def test_cb(self):
        entrada = 'cb'
        self.assertTrue(palavras_primas(entrada))

class TestPegarNumeroDaLetra(TestCase):
        
    def teste_a(self):
        entrada = 'a'
        self.assertEqual(pegar_numero_da_letra(entrada), 1)
    
    def teste_b(self):
        entrada = 'b'
        self.assertEqual(pegar_numero_da_letra(entrada), 2)

    def teste_z(self):
        entrada = 'z'
        self.assertEqual(pegar_numero_da_letra(entrada), 26)
    
    def teste_j(self):
        entrada = 'j'
        self.assertEqual(pegar_numero_da_letra(entrada), 10)

    def teste_r(self):
        entrada = 'r'
        self.assertEqual(pegar_numero_da_letra(entrada), 18)

    def teste_A(self):
        entrada = 'A'
        self.assertEqual(pegar_numero_da_letra(entrada), 1)
    
    def teste_B(self):
        entrada = 'B'
        self.assertEqual(pegar_numero_da_letra(entrada), 2)

    def teste_J(self):
        entrada = 'J'
        self.assertEqual(pegar_numero_da_letra(entrada), 10)

class  TestePalavraNumero(TestCase):

    def teste_Ab(self):
        entrada = 'Ab'
        self.assertEqual(palavra_numero(entrada), 3)


if __name__ == '__main__':
    main()

