import unittest

from util.calculo import Calculo
from util.lista_dimensao import Multiverso


class TestUM(unittest.TestCase):

    """
    Verifica o retorno correto das distâncias ou rotas mesmo em ordens diferentes,
    Exemplo [20, 50, 30] e [50, 20, 30] serão considerados iguais.
    """
    def test_distancia_A_a_C_passando_B(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.a, chegada=Multiverso.c, passando=Multiverso.b)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(list(set(calculo.get_distancias()) - set([140, 90, 200])), [])

    def test_distancia_A_a_D(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.a, chegada=Multiverso.d)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(list(set(calculo.get_distancias()) - set([180, 50, 130])), [])

    def test_distancia_A_a_C_passando_D(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.a, chegada=Multiverso.c, passando=Multiverso.d)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(list(set(calculo.get_distancias()) - set([90, 200])), [])

    def test_distancia_A_a_C_menor_rota(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.a, chegada=Multiverso.c, menor_rota=True)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_valor_menor_rota(), 90)

    def test_distancia_B_a_B_menor_rota(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.b, menor_rota=True)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_valor_menor_rota(), 90)

    def test_distancia_C_a_C_paradas_3(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.c, num_paradas_max=3)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_distancias().__len__(), 3)


    def test_distancia_A_a_C_paradas_4(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.a, chegada=Multiverso.c, num_paradas_max=4)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_distancias().__len__(), 4)

    def test_distancia_C_a_C_unidades_300(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.c, num_unidades_max=300)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_distancias().__len__(), 3)

    def test_distancia_A_a_A(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.a)
        except RecursionError:
            pass
        self.assertEqual(calculo.get_distancias().__len__(), 0)

    def test_distancia_E_a_E_unidades_300(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.e, num_unidades_max=100)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_distancias().__len__(), 1)

    def test_distancia_D_a_B_menor_rota(self):
        try:
            calculo = Calculo()
            calculo.definir_rotas_universos(partida=Multiverso.d, chegada=Multiverso.b, menor_rota=True)
        except RecursionError:
            raise ValueError("Inpossível chegar ao universo")
        self.assertEqual(calculo.get_valor_menor_rota(), 90)