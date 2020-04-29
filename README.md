# django-restful-api-crawler-test

Uma aplicação multifacetada para testes, que consiste em uma API restful feita com o framework [Django](https://www.djangoproject.com/), um web crawler e um script de conversão de arquivos CSV para JSON ambos desenvolvidos com a linguagem [Python](https://www.python.org/).

# Propostas

- Desenvolver um aplicativo que consiga trazer os nomes dos foros presentes no combobox do link : https://esaj.tjsp.jus.br/cpopg/open.do no formato JSON utilizando a ferramenta requests do Python.

- Desenvolver uma API com as operações de CRUD em uma base de dados Postgresql, utilizando classes divisões previstas em uma modelagem MVC, bem como a utilização de padrões de projetos.

- Criar uma pipeline de transformação de um arquivo texto fornecido, para um formato json utilizando como base o RabbitMQ como no exemplo a seguir:

  - Do formato CSV:

  ```
  "00242689020168190087";DANO MORAL;REGIONAL DE ALCANTARA;2020-01-10 00:00:00;Procedimento do Juizado Especial Cível/Fazendário
  ```

  - Para o formato JSON:

  ```
  {
    "nuprocesso": "00242689020168190087",
    "deassunto": "DANO MORAL",
    "devara": "REGIONAL DE ALCANTARA"
    "dtcoleta": "2020-01-10 00:00:00",
    "declasse": "Procedimento do Juizado Especial Cível/Fazendário"
  }
  ```

# Como usar

Para que a aplicação seja executada via [Docker](https://www.docker.com/), entre na pasta do projeto e execute os seguintes comandos:

```
docker-compose build
docker-compose up
```

Após a criação dos containers as aplicações já podem ser testadas, para isso bastante seguir as instruções abaixo para cada uma das funcionalidades do projeto:

- Crawler.
  - Após a execução dos comandos Docker citados acima, acessar via linha de comando o container chamado **python**, e dentro do diretório **/home/csvtojson** executar o seguinte comando:
  
  ```
  python csvtojson.py [input.csv] [output.json]
  ```
  
  Sendo os parâmetros **input.csv** e **output.json** opcionais. Caso eles não sejam fornecidos, o script utilizará os arquivos padrão contidos em seu diretório.

- Django restful API.
  - Após a criação dos containers a API poderá ser acessada através do navegador no link:
  http://localhost:8000/api/book/
  
- Script conversão.
  - Após a execução dos comandos Docker citados acima, acessar via linha de comando o container chamado **python**, e dentro do diretório **/home/getforostjsp** executar o seguinte comando:
  
  ```
  python getforostjsp.py [output.json]
  ```
  
  Sendo o parâmetro **output.json** opcional. Caso ele não seja fornecido, o script utilizará os arquivo padrão contido em seu diretório.
