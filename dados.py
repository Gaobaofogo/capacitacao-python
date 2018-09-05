class Animal:
    def __init__(self, nome, tipo_de_animal, idade):
        self.nome = nome
        self.tipo_de_animal = tipo_de_animal
        self.idade = idade

    def __str__(self):
        return self.nome

    def minha_idade(self):
        if self.idade > 7:
            return "Estou ficando velho"
        else:
            return "Estou na flor da idade"

class PetShop:
    def __init__(self):
        self.lista_de_animais = []

    def pega_animal(self, nome_do_animal):
        animal_encontrado = None

        for animal in self.lista_de_animais:
            if nome_do_animal == animal.nome:
                animal_encontrado = animal
                break
        
        if animal_encontrado:
            return str(animal_encontrado)
        else:
            return "O animal não está no petshop"
    
    def adiciona_animal(self, animal):
        self.lista_de_animais.append(animal)

    def remove_animal(self, nome_do_animal):
        animal_encontrado = None

        for animal in self.lista_de_animais:
            if nome_do_animal == animal.nome:
                animal_encontrado = animal
                break
        
        if animal_encontrado:
            self.lista_de_animais.remove(animal_encontrado)
        else:
            return "O animal não está no petshop"