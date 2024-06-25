import os

class Restaurante:
    lista_restaurantes = [
        {'restaurante_nome': 'Ligeirin', 'restaurante_categoria': 'FastFood'},
    ]

    def __init__(self, nome, categoria ):
        self._nome = nome
        self._categoria = categoria
        self._ativo= False
        # Adiciona o restaurante na lista de restaurantes
        Restaurante.lista_restaurantes.append({'restaurante_nome': nome, 'restaurante_categoria': categoria}) 
    

    def __str__(self):
        """
        Feito para não retorna valor de mémoria
        """
        return f'{(self._nome).ljust(15)}{'─'*15}   {(self._categoria).ljust(12)} {self._ativo}'

    def ativo(self):
        pass
    
    @classmethod
    def restaurante_add(cls, nome, categoria):
        cls.lista_restaurantes.append({'restaurante_nome': nome, 'restaurante_categoria': categoria})
    """
    Informações:
    ------------
    Responsavel por adicionar novos restaurantes a lista de restaurantes

    Uso:
    ------------
    Restaurante.restaurante_add('Exemplo de Restaurante', 'Churrascaria')
    """

    @classmethod
    def listar_restaurantes(cls):
        """
        Informações:
        -------------
        Capaz de listar os restaurantes
        
        """
        if not cls.lista_restaurantes:
            print('A lista de restaurantes está vazia')
            return
        print('A lista contem os seguintes restaurantes: ')
        for i, restaurante in enumerate(cls.lista_restaurantes, start=1):
           print(f'{i}. Restaurante: {restaurante["restaurante_nome"]}, Categoria: {restaurante["restaurante_categoria"]}')
    

