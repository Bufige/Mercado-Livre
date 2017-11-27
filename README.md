# Mercado-Livre
Web scrapping para pegar dados do mercado livre. É bem simples e direto, fácil de modificar para coletar mais dados.


# Explicação da lógica utilizada
No main.py definimos um link de pesquisa como exemplo. Esse link é padrão do mercado livre para qualquer pesquisa.

Com isso em mente, nos procuramos nesse link os links de todos os produtos na página atual.
Coletamos os dados da página atual e vamos para a página seguinte até que não exista mais páginas.
Salvamos esses links num arquivo.

Agora vem a parte de acessar os links para pegarmos os dados dos items.
Fazemos isso e em seguida, criamos um arquivo excel e adicionamos os dados encontrados do item na tabela.

# Objetivo

Esse é apenas um software de prova de conceito, é possível fazer otimizações nisso. Como? bom, a página do mercado livre não é totalmente dinãmica, cada "next_page" tem seu próprio link, logo não é recarregado dentro da própria página. Então, poderiamos fazer um script para pegar esses links e utilizar o beatifulsoup para percorrer elas. Isso otimizaria pois não precisariamos utilizar o selenium nesse projeto. Eu apenas adicionei o selenium apenas como demonstração.


# Instalação

Basta ter o pip instalado, com isso, é necessário apenas instalar as seguintes bibliotecas:
* > **pip install openpyxl**
* > **pip install selenium**
* > **pip install requests**
* > **pip install beautifulsoup4**


# Feito agora basta fazer: python main.py para rodar !
