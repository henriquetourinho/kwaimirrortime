import os
import re
import sys
import requests
from bs4 import BeautifulSoup

// Função para carregar mais conteúdo
function carregarMaisConteudo() {
    // Aqui você pode colocar o código para carregar mais conteúdo, como fazer uma requisição AJAX para buscar mais dados do servidor
    console.log("Carregando mais conteúdo...");
}

// Função para verificar se o usuário está próximo do final da página
function verificarFimPagina() {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) { // Se a soma da altura visível da janela mais a posição vertical de rolagem for maior ou igual à altura total do corpo do documento, então o usuário está próximo do final da página
        carregarMaisConteudo(); // Chama a função para carregar mais conteúdo
    }
}

// Adiciona um evento de rolagem à janela
window.addEventListener('scroll', function() {
    verificarFimPagina();
});



# Função para baixar o código-fonte da página
def save_html_source(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print("Código-fonte salvo com sucesso.")
    else:
        print(f"Falha ao baixar a página. Status code: {response.status_code}")

# Função para extrair os links dos vídeos .mp4
def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    video_links = [link.get('href') for link in links if link.get('href') and link.get('href').endswith('.mp4')]
    print("Links dos vídeos encontrados:")
    for link in video_links:
        print(link)
    return video_links

# Função para baixar e salvar os arquivos
def download_files(links, directory):
    os.makedirs(directory, exist_ok=True)
    for link in links:
        # Substitui "\." por "."
        link = link.replace("\.", ".")
        file_name = os.path.basename(link)
        file_path = os.path.join(directory, file_name)
        try:
            response = requests.get(link, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"Download concluído: {file_path}")
            else:
                print(f"Falha ao baixar {link}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Erro ao baixar {link}. Erro: {e}")

# Função para obter o URL completo com base no nome de usuário
def get_full_url(username):
    return f"https://www.kwai.com/@{username}"

if __name__ == "__main__":
    # Verifica se o número de argumentos é correto
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <URL ou Nome de Usuário>")
        sys.exit(1)

    # Obtém o URL ou nome de usuário a partir dos argumentos da linha de comando
    user_input = sys.argv[1]

    # Verifica se o input é um URL completo ou apenas um nome de usuário
    if user_input.startswith("https://www.kwai.com/@"):
        url = user_input
    else:
        url = get_full_url(user_input)

    # Diretório principal onde serão salvos os perfis
    profiles_dir = "perfis"

    # Salva o código-fonte da página no diretório do perfil
    response = requests.get(url)
    if response.status_code == 200:
        # Extrai o nome de usuário da URL usando expressão regular
        match = re.search(r'@(.+)', url)
        if match:
            username = match.group(1)
            # Substitui caracteres inválidos para nomes de diretório
            username = re.sub(r'[^\w\-_\.]', '_', username)
            # Cria o diretório do perfil dentro de 'profiles' se não existir
            user_dir = os.path.join(profiles_dir, username)
            os.makedirs(user_dir, exist_ok=True)
            print(f"Diretório do perfil criado: {user_dir}")

            # Salva o código-fonte como index.html no diretório do perfil
            html_file_path = os.path.join(user_dir, 'index.html')
            save_html_source(url, html_file_path)
            print(f"Código-fonte salvo em {html_file_path}")

            # Extrai os links dos vídeos desejados do HTML
            video_links = extract_links(response.text)
            if video_links:
                # Diretório para salvar os arquivos de vídeo dentro do diretório do perfil
                media_dir = os.path.join(user_dir, 'media')
                # Baixa e salva os arquivos
                download_files(video_links, media_dir)
            else:
                print("Nenhum link de vídeo encontrado.")
        else:
            print("Nome de usuário não encontrado na URL.")
    else:
        print(f"Falha ao baixar a página. Status code: {response.status_code}")

