import pytest
import time
from base import *

# https://docs.python.org/3/library/unittest.html  referencias 

def test_nuser():
    # Crear un nuevo usuario 
    result = nuser("JoseWolf", "wolf@ufm.edu", "12345#")
    expected = "True"
    #self.assertEqual(result, expected)
    assert result == expected,"test failed"

# Se verifica la creación de un usuario 
def test_confirm(): 
    result = confirm('cruz', "1234") 
    expected = "True"
    assert result == expected,"test failed"
    
# Se verifica la información de un usuario 
def test_infoUser(): 
    result = infoUser("cruz")
    expected = "{0: {0: 'cruz', 1: 'cldelcid@ufm.edu', 2: '1234'}}"
    assert result == expected,"test failed"

# Se crea una petición
def test_npeti(): 
    result = npeti("Computadora gamer", "Computacion", "Cruz")
    expected = "True"
    assert result == expected,"test failed"

# Se piden todas las peticiones
def test_peticiones(): 
    result = peticiones()
    assert result, "test true" 

# Se solicitan las  peticiones por clasificación 
def test_pet_esp():
    result = pet_esp("Computacion")
    expected = r"{0: {0: 18, 1: 'Recomendacion de buenas computadoras', 2: 'Computacion', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'cruz'}, 1: {0: 24, 1: 'Computadora gamer', 2: 'Computacion', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'Cruz'}}"
    assert result == expected,"test failed"

    result = pet_esp("Viajes")
    expected = r"{0: {0: 20, 1: 'Lindos lugares en Huehue', 2: 'Viajes', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}}"
    assert result == expected,"test failed"

    result = pet_esp("Programación")
    expected = r"{0: {0: 23, 1: 'Mejor lenguaje para hacer bases de datos ', 2: 'Programación ', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'cruz'}}"
    assert result == expected,"test failed"

    result = pet_esp("Tecnologia")
    expected = r"{0: {0: 21, 1: 'Buenas apps para comprar comida', 2: 'Tecnologia', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}}"
    assert result == expected,"test failed"

# Se solicitan las peticiones de un usuario 
def test_pet_per(): 
    result = pet_per("Daniel")
    expected = r"{0: {0: 20, 1: 'Lindos lugares en Huehue', 2: 'Viajes', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}, 1: {0: 21, 1: 'Buenas apps para comprar comida', 2: 'Tecnologia', 3: datetime.datetime(2021, 10, 22, 0, 0), 4: 'daniel'}}"
    assert result == expected,"test failed"
    
# Se solicitan los comentarios de un usuario 
def test_pet_comen(): 
    result = pet_comen("Daniel")
    expected = r"{}"
    assert result == expected,"test failed"
    
# Se borra un peticion con sus comentarios 
def test_duser(): 
    result = duser("Denise")
    expected = "True"
    assert result == expected,"test failed"

def test_shutdown(): 
    shutdown_server()
