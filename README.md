Para ambiente linux.

Com do docker instaldo, caso não tenha -> https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/

Para rodar a aplicação será necessario ter o python instaldo, de preferencia a versão 3.12:
    
    1 - Craindo o ambiente:
        $ python -m venv .venv

    2 - Ativando o ambiente no linux:
        $ source .venv/bin/activate

    3 - Instalando os requisitos:
        $ pip install -r requierements.txt

    3.1 - Ou com poetry (versão python 3.12):
        $ pip install poetry
        $ poetry init

    4 - Para rodar o projeto, na raiz do projeto:
        $ python -m main
   
    4.1 - Ou com gunicorn:
        $ gunicorn --bind 127.0.0.1:5000 src.application.server:app
   
    5 - Para rodar os test:
         $ pytest
    
    5.1 - Testes com covarege (cobertura de teste):
         $ coverage run -m pytest
    
    5.2 - Para visualizar a cobertura de teste em tela:
         $ coverage report -m

    5.3 - Para visualizar a cobertura de teste no navegador:
         $ coverage html
         $ python -m http.server 8080

    6 - Em http://127.0.0.1:5000/api/v1/docs esta o swagger, sendo possivel rodar os endpoints.


Endpoint:
  - Criar novo ToDo;
    - http://127.0.0.1:5000/api/v1/todo/
    - Metodo -> POST
    - ex: `curl -X 'POST' \
          'http://127.0.0.1:5000/api/v1/todo/' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "title": "string",
          "description": "string"
          }'`
    - ex response: `{
                     "id": 49,
                     "title": "string",
                     "description": "string",
                     "completed": false,
                     "start_date": "",
                     "end_date": ""
                   }`


 - Buscar ToDo 
    - http://127.0.0.1:5000/api/v1/todo/{id}/
    - Metodo -> GET
    - ex: `curl -X 'GET' \
      'http://127.0.0.1:5000/api/v1/todo/49/'`
    - ex response: `{
                     "id": 49,
                     "title": "string",
                     "description": "string",
                     "completed": false,
                     "start_date": "",
                     "end_date": ""
                   }`


 - Listar ToDo
   - http://127.0.0.1:5000/api/v1/todo/
   - Metodo -> GET
   - ex: `curl -X 'GET' \
     'http://127.0.0.1:5000/api/v1/todo/'`
   - ex response: `[
                        {
                            "id": 1,
                            "title": "string",
                            "description": "string",
                            "completed": true,
                            "start_date": "2024-09-18",
                            "end_date": "2024-09-18"
                        },
                        {
                            "id": 49,
                            "title": "string",
                            "description": "string",
                            "completed": false,
                            "start_date": "",
                            "end_date": ""
                        }
                   ]`


 - Atualizar parcialmente ToDo
   - http://127.0.0.1:5000/api/v1/todo/{id}/
   - Metodo -> PATCH
   - ex: `curl -X 'PATCH' \
     'http://127.0.0.1:5000/api/v1/todo/49/' \
      -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
           "completed": true
          }'`
   - ex response: `{
                     "id": 49,
                     "title": "string",
                     "description": "string",
                     "completed": true,
                     "start_date": "",
                     "end_date": ""
                   }`

 - Atualizar Full ToDo
   - http://127.0.0.1:5000/api/v1/todo/{id}/
   - Metodo -> PUT
   - ex: `curl -X 'PUT' \
      'http://127.0.0.1:5000/api/v1/todo/49/' \
   -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d '{
         "title": "string Update",
         "description": "string Update",
         "completed": true,
         "start_date": "2024-09-19",
         "end_date": "2024-09-19"
       }'`
   - ex response: `{
                 "title": "string Update",
                 "description": "string Update",
                 "completed": true,
                 "start_date": "2024-09-19",
                 "end_date": "2024-09-19"
               }`
 
 - Deletar ToDo
   - http://127.0.0.1:5000/api/v1/todo/{id}/
   - Metodo -> DELETE
   - ex: `curl -X 'DELETE' 'http://127.0.0.1:5000/api/v1/todo/49/'`