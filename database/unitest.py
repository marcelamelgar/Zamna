import unittest
import time
from base import *

# https://docs.python.org/3/library/unittest.html  referencias 


class TestingUser(unittest.TestCase):
    
    # Crear un nuevo usuario 
    def test_nuser(self):
        result = nuser("JoseWolf", "wolf@ufm.edu", "12345#")
        expected = "True"
        self.assertEqual(result, expected)


    # Se verifica la creación de un usuario 
    def test_confirm(self): 
        result = confirm('cruz', "1234") 
        expected = "True"
        self.assertEqual(result, expected)
    
    # Se verifica la información de un usuario 
    def test_infoUser(self): 
        result = infoUser("cruz")
        expected = "{0: {0: 'cruz', 1: 'cldelcid@ufm.edu', 2: '1234'}}"
        self.assertEqual(result, expected)

    # Se crea una petición
    def test_npeti(self): 
        result = npeti("Computadora gamer", "Computacion", "Cruz")
        expected = "True"
        self.assertEqual(result, expected)

    # Se piden todas las peticiones
    def test_peticiones(self): 
        result = peticiones()
        self.assertTrue(result) 

    # Se solicitan las  peticiones por clasificación 
    def test_pet_esp(self):
        result = pet_esp("Computacion")
        expected = r"{0: {0: 18, 1: 'Recomendacion de buenas computadoras', 2: 'Computacion', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'cruz'}, 1: {0: 24, 1: 'Computadora gamer', 2: 'Computacion', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'Cruz'}}"
        self.assertEqual(result, expected)

        result = pet_esp("Viajes")
        expected = r"{0: {0: 20, 1: 'Lindos lugares en Huehue', 2: 'Viajes', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}}"
        self.assertEqual(result, expected)

        result = pet_esp("Programación")
        expected = r"{0: {0: 23, 1: 'Mejor lenguaje para hacer bases de datos ', 2: 'Programación ', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'cruz'}}"
        self.assertEqual(result, expected)

        result = pet_esp("Tecnologia")
        expected = r"{0: {0: 21, 1: 'Buenas apps para comprar comida', 2: 'Tecnologia', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}}"
        self.assertEqual(result, expected)

    # Se solicitan las peticiones de un usuario 
    def test_pet_per(self): 
        result = pet_per("Daniel")
        expected = r"{0: {0: 20, 1: 'Lindos lugares en Huehue', 2: 'Viajes', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}, 1: {0: 21, 1: 'Buenas apps para comprar comida', 2: 'Tecnologia', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}}"
        self.assertEqual(result, expected)
    
    # Se solicitan los comentarios de un usuario 
    def test_pet_comen(self): 
        result = pet_comen("Daniel")
        expected = r"{}"
        self.assertEqual(result, expected)
    
    # Se borra un peticion con sus comentarios 
 
    def test_duser(self): 
        result = duser("Denise")
        expected = "True"
        #self.assertEqual(result, expected)

    def test_shutdown(self): 
        shutdown_server()
        
    
if __name__ == '__main__':
    unittest.main()

