Kwaimirrortime: Um script para baixar vídeos do Kwai e organizá-los por perfil e usuário.

Visão geral
O kwaimirrortime é uma ferramenta poderosa para baixar e organizar seus vídeos favoritos do Kwai. Ele automatiza o processo de download, salvando os vídeos em pastas específicas para cada perfil e usuário, facilitando a localização e o gerenciamento dos seus arquivos.

Funcionalidades
Baixa todos os vídeos de um perfil do Kwai: Selecione o perfil que deseja baixar e o kwaimirrortime fará o trabalho duro para você, capturando todos os vídeos disponíveis.
Organização por perfil e usuário: Os vídeos baixados são automaticamente organizados em pastas nomeadas com o perfil e o usuário, garantindo que você sempre saiba de onde cada vídeo veio.
Pasta "media" para armazenamento centralizado: Todos os vídeos baixados de diferentes usuários são armazenados em uma pasta central chamada "media", proporcionando um local único para acessar todos os seus arquivos.
Opções personalizáveis: Personalize o destino dos downloads e os nomes das pastas para atender às suas necessidades de organização.
Instalação
Clone o repositório:
Bash
git clone https://github.com/seu_nome_de_usuario/kwaimirrortime.git
Use o código com cuidado.
content_copy
Instale as dependências:
Bash
pip install requirements.txt
Use o código com cuidado.
content_copy
Uso
Obtenha o link do perfil do Kwai:
Acesse o perfil do Kwai que deseja baixar os vídeos e copie o link da barra de endereço.

Execute o script:
Bash
python kwaimirrortime.py <link_do_perfil>
Use o código com cuidado.
content_copy
Substitua <link_do_perfil> pelo link do perfil que você copiou na etapa 1.

Opções:
-o <pasta_de_saida>: Especifique a pasta de saída para os vídeos. Por padrão, os vídeos são salvos na pasta atual.
-u <usuario>: Defina o nome do usuário dos vídeos que estão sendo baixados. Por padrão, o nome do usuário é o mesmo que o nome do perfil.
Exemplos
Baixar todos os vídeos do perfil https://www.kwai.com/u/123456789 e salvar na pasta /home/usuario/Kwaimirrortime/videos:
Bash
python kwaimirrortime.py https://www.kwai.com/u/123456789 -o /home/usuario/Kwaimirrortime/videos
Use o código com cuidado.
content_copy
Baixar todos os vídeos do perfil https://www.kwai.com/u/123456789 e salvar na pasta /home/usuario/Kwaimirrortime/videos, definindo o nome do usuário para joaodasilva:
Bash
python kwaimirrortime.py https://www.kwai.com/u/123456789 -o /home/usuario/Kwaimirrortime/videos -u joaodasilva
Use o código com cuidado.
content_copy
Observações
Certifique-se de ter uma conexão com a internet estável antes de executar o script.
O tempo de download pode variar dependendo da quantidade de vídeos e da velocidade da sua internet.
Os vídeos baixados serão salvos no formato MP4.
Contribuições
Se você deseja contribuir para o kwaimirrortime, você é bem-vindo! Envie um pull request para o repositório GitHub.


