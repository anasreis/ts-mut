import unittest
from vestibulando import verificaVestibulando

class TestMethod(unittest.TestCase):

    def test_case1(self):
        nota = 500
        self.assertEqual(verificaVestibulando(nota), 'Você está selecionado')

    def test_case2(self):
        nota = 400
        self.assertEqual(verificaVestibulando(nota), 'Você está na lista de espera')

    def test_case3(self):
        nota = 300
        self.assertEqual(verificaVestibulando(nota), 'Você está na lista de espera')

    def test_case4(self):
        nota = 200
        self.assertEqual(verificaVestibulando(nota), 'Você está na lista de espera')

    def test_case5(self):
        nota = 100
        self.assertEqual(verificaVestibulando(nota), 'Você não foi selecionado')

    def test_case6(self):
        nota = 0
        self.assertEqual(verificaVestibulando(nota), 'É necessário procurar a universidade')

if __name__ == '__main__':
    unittest.main()
