from requests import get 

print(get("http://localhost:8888/peticiones").text)