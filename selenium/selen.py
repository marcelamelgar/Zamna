from os import getcwd
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


# paht = r'C:\\Users\\carlos\\Desktop\\spotify\\seleniumpruebas\\chromedriver.exe'

path = getcwd() + r"\chromedriver.exe"
#paht = r'D:\\spotify\\seleniumpruebas\\chromedriver.exe'  #<----- Hay que cambiar el path donde esta el driver de chrome
driver = webdriver.Chrome(path)
driver.maximize_window()

driver.get("http://localhost:5000/login")
time.sleep(1)

# Registro de usuario nuevo 
driver.find_element_by_name("newregis").click()
time.sleep(1)
driver.find_element_by_name("username").send_keys("Marito")
time.sleep(1)
driver.find_element_by_name("email").send_keys("mariopisquiy@ufm.edu")
time.sleep(1)
driver.find_element_by_name("pass").send_keys("1234")
time.sleep(1)
driver.find_element_by_name("pass2").send_keys("1234")
time.sleep(1)
driver.find_element_by_name("register").click()
time.sleep(1)

# Nueva petición
driver.find_element_by_id("newpetition").click()
time.sleep(1)
driver.find_element_by_name("comment").clear()
driver.find_element_by_name("comment").send_keys("Buenos lugares para comprar shecas en Xela, no soy de aquí.")
time.sleep(1)
driver.find_element_by_name("categ").send_keys("Comida")
time.sleep(1)
driver.find_element_by_name("post").click()
time.sleep(1)

# Nuevo comentario 
driver.find_element_by_link_text("Comida").click()
time.sleep(1)
driver.find_element_by_name("id").click()
time.sleep(1)
driver.find_element_by_name("comment").send_keys("Xelapan es el mejor para comprar shecas. ¡Recomendado!")
time.sleep(1)
driver.find_element_by_name("post").click()
time.sleep(2)
driver.find_element_by_link_text("Zamna").click()
time.sleep(1)



# Borrar usuario 
driver.find_element_by_class_name("circle").click()
time.sleep(1)
driver.find_element_by_id("deleteuser").click()
time.sleep(1)

# Hacer login y logout 
driver.find_element_by_name("username").send_keys("cruz")
time.sleep(1)
driver.find_element_by_name("pass").send_keys("1234")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(2)
driver.find_element_by_link_text("LOGOUT").click()
time.sleep(3)
driver.quit()



"""
driver.find_element_by_name("play").click()
time.sleep(1)
driver.find_element_by_name("autor").send_keys("Queen")
time.sleep(1)
driver.find_element_by_name("cancion").send_keys("We are the champions")
time.sleep(1)
driver.find_element_by_name("album").send_keys("Live Killers")
time.sleep(1)
driver.find_element_by_name("añadir_cancion").click()
time.sleep(3)
driver.find_element_by_id("play We are the champions").click()
time.sleep(3)
driver.find_element_by_id("play Levitating").click()
time.sleep(3)
driver.find_element_by_name("Play_Previous").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_id("cola The Nights").click()
time.sleep(3)
driver.find_element_by_id("eliminar Mas").click()
time.sleep(3)
driver.find_element_by_id("cola Back In Black").click()
time.sleep(3)
driver.find_element_by_id("cola Africa").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_id("eliminar cola Back In Black").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("autor").send_keys("Bad Bunny")
time.sleep(1)
driver.find_element_by_name("cancion").send_keys("Te mudaste")
time.sleep(1)
driver.find_element_by_name("album").send_keys("El Ultimo Tour Del Mundo")
time.sleep(1)
driver.find_element_by_name("añadir_cancion").click()
time.sleep(3)
driver.find_element_by_id("play Te mudaste").click()
time.sleep(3)
driver.find_element_by_name("cancion_buscar").send_keys("Azul Oscuro")
time.sleep(3)
driver.find_element_by_name("buscar_cancion").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("casa1").send_keys("I")
time.sleep(3)
driver.find_element_by_name("casa2").send_keys("M")
time.sleep(3)
driver.find_element_by_name("caminos").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(3)
driver.find_element_by_name("Play_Next").click()
time.sleep(5)
driver.quit()

"""