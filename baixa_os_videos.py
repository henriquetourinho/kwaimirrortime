import os
import re

# URL da página do Kwai
url_kawai = 'https://www.kwai.com/@Davidcauaoliveira'

# Extrai o nome de usuário da URL usando expressão regular
match = re.search(r'@(.+)', url_kawai)
if match:
    username = match.group(1)
    # Substitui caracteres inválidos para nomes de diretório
    username = re.sub(r'[^\w\-_\.]', '_', username)
    # Caminho completo do diretório com o nome de usuário dentro de 'videos'
    user_dir = os.path.join('videos', username)
    # Cria o diretório se não existir
    os.makedirs(user_dir, exist_ok=True)
    print(f"Diretório do usuário criado: {user_dir}")
else:
    print("Nome de usuário não encontrado na URL.")


# Diretório para salvar os vídeos
download_dir = 'videos'

# Cria o diretório se não existir
os.makedirs(download_dir, exist_ok=True)

# Função para baixar um arquivo
def download_file(url, dest):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(dest, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Download concluído: {dest}")
        else:
            print(f"Falha ao baixar {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Erro ao baixar {url}. Erro: {e}")

# Baixa cada vídeo
for link in video_links:
    # Extrai o nome do arquivo do link
    file_name = os.path.basename(link)
    # Define o caminho completo para salvar o arquivo
    file_path = os.path.join(download_dir, file_name)
    # Baixa o arquivo
    download_file(link, file_path)

