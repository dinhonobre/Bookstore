import requests

# CONFIGURAÇÃO
BASE_URL = "http://127.0.0.1:8000/api_new/"
USERNAME = "andersonnobre"   # coloque seu usuário do Django
PASSWORD = "L@risse12"     # coloque sua senha

# 1️⃣ Obter token
r = requests.post(f"{BASE_URL}api-token-auth/", json={"username": USERNAME, "password": PASSWORD})
token = r.json().get("token")
if not token:
    print("Erro: não foi possível gerar token. Verifique usuário/senha")
    print(r.text)
    exit()

print("Token gerado:", token)

# 2️⃣ Testar endpoint protegido (primeira página)
headers = {"Authorization": f"Token {token}"}
r1 = requests.get(f"{BASE_URL}items/", headers=headers)
print("\nItens página 1:")
print(r1.json())

# 3️⃣ Testar segunda página (paginação)
r2 = requests.get(f"{BASE_URL}items/?page=2", headers=headers)
print("\nItens página 2:")
print(r2.json())
