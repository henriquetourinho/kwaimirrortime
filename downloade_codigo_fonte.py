import requests

# URL da página que você deseja baixar
url = 'URL_DA_PAGINA'  # Substitua pela URL real

# Faz o download do conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Salva o código-fonte em um arquivo
    with open('pagina.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Código-fonte salvo com sucesso.")
else:
    print(f"Falha ao baixar a página. Status code: {response.status_code}")

