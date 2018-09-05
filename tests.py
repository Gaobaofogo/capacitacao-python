import unittest
from dados import Animal, PetShop

class TestPetshop(unittest.TestCase):

    def test_animal(self):
        animal1 = Animal('Vitório', 'gato', 3)
        animal2 = Animal('Rose', 'gato', 8)

        self.assertEqual(animal1.nome, 'Vitório')
        self.assertEqual(str(animal1), 'Vitório')
        self.assertEqual(animal1.tipo_de_animal, 'gato')
        self.assertEqual(animal1.minha_idade(), 'Estou na flor da idade')
        self.assertEqual(animal2.minha_idade(), 'Estou ficando velho')
    
    def test_petshop(self):
        animal1 = Animal('Vitório', 'gato', 3)
        animal2 = Animal('Rose', 'gato', 8)
        lista1 = [animal1, animal2]
        lista2 = [animal1]
        petshop = PetShop()

        petshop.adiciona_animal(animal1)
        petshop.adiciona_animal(animal2)

        self.assertEqual(petshop.lista_de_animais, lista1)
        self.assertEqual(petshop.pega_animal('Vitório'), str(animal1))
        self.assertEqual(petshop.pega_animal('Raika'), str("O animal não está no petshop"))
        
        petshop.remove_animal('Rose')

        self.assertEqual(petshop.lista_de_animais, lista2)