import requests
# API
api_key = ""
endpoint = ""
# Entrada
prompt = "teste"
model = "text-davinci-002"

# Corpo
data = {
    "prompt": prompt,
    "model": model,
    "max_tokens": 100
}

# Solicitação
response = requests.post(endpoint, json=data, headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer{api_key}"
})

# output
print(response.json())
