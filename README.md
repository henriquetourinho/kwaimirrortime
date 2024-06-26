#Kwaimirrortime: Um script para baixar vídeos do Kwai e organizá-los por perfil e usuário.

##Visão geral
O kwaimirrortime é uma ferramenta poderosa para baixar e organizar seus vídeos favoritos do Kwai. Ele automatiza o processo de download, salvando os vídeos em pastas específicas para cada perfil e usuário, facilitando a localização e o gerenciamento dos seus arquivos.

##Funcionalidades
Baixa todos os vídeos de um perfil do Kwai: Selecione o perfil que deseja baixar e o kwaimirrortime fará o trabalho duro para você, capturando todos os vídeos disponíveis.
Organização por perfil e usuário: Os vídeos baixados são automaticamente organizados em pastas nomeadas com o perfil e o usuário, garantindo que você sempre saiba de onde cada vídeo veio.

##main.py:

#Função principal:
Solicita ao usuário o link do perfil do Kwai que deseja baixar os vídeos.
Valida o link do perfil.
Chama a função extrai_os_videos() para obter a lista de links dos vídeos.
Chama a função baixa_os_videos() para baixar cada vídeo da lista.
Organiza os vídeos baixados em pastas por perfil e usuário.
Opções:
-o <pasta_de_saida>: Especifica a pasta de saída para os vídeos. Por padrão, os vídeos são salvos na pasta atual.
-u <usuario>: Define o nome do usuário dos vídeos que estão sendo baixados. Por padrão, o nome do usuário é o mesmo que o nome do perfil.
extrai_os_videos.py:

##Função extrai_os_videos(link_do_perfil):
Recebe como entrada o link do perfil do Kwai.
Envia uma requisição HTTP para o link do perfil.
Extrai os links dos vídeos da página HTML.
Retorna uma lista de links dos vídeos.
baixa_os_videos.py:

##Função baixa_os_videos(link_do_video, pasta_de_saida, nome_do_usuario):
Recebe como entrada o link do vídeo, a pasta de saída e o nome do usuário.
Envia uma requisição HTTP para o link do vídeo.
Extrai o código-fonte da página HTML.
Obtém o link direto para o vídeo a partir do código-fonte.
Envia uma requisição HTTP para o link direto do vídeo.
Baixa o vídeo para a pasta de saída com o nome do usuário e o nome do vídeo.
downloade_codigo_fonte.py:

##Função downloade_codigo_fonte(link_do_video):
Recebe como entrada o link do vídeo.
Envia uma requisição HTTP para o link do vídeo.
Retorna o código-fonte da página HTML.
