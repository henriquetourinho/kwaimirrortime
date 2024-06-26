from bs4 import BeautifulSoup

# Carrega o código-fonte salvo
with open('pagina.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Cria o objeto BeautifulSoup para análise do HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extrai todos os links (neste exemplo, estamos procurando por tags <a>)
links = soup.find_all('a')

# Filtra os links desejados (neste caso, links que terminam em .mp4)
video_links = [link.get('href') for link in links if link.get('href') and link.get('href').endswith('.mp4')]

# Imprime os links extraídos
for link in video_links:
    print(link)

