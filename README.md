# desafio-paschoalotto
Projeto criado para o *desafio técnico* da Paschoalotto.

---
## Install
Para a instalação, há um script responsável por faze-la, para executa-lo:
1) Instalar o *make*:
```
    sudo apt get install make
```
2) Executar o comando abaixo no diretório raiz do projeto:
```
    make install
```

A instalação também pode ser feita manualmente, para isso:
1) Criar a *.venv*: 
```
    python3 -m venv .venv
```
2) Instalar as dependências do projeto através do *requirements.txt*:
```
    .venv/bin/pip install -r requirements.txt
```
3) Setar a variável de ambiente *FLASK_APP*:
```
    export FLASK_APP="phone:create_app()"
```
4) Rodar as migrations do projeto:
```
    .venv/bin/flask db upgrade
```

---
## Start
Para startar o projeto:
1) Se o *make* está instalado: 
```
    make run
```

Para startar o projeto caso não possuir o *make*:
1) Setar a variável de ambiente *FLASK_APP*:
```
    export FLASK_APP="phone:create_app()"
```

2) Rodar o comando:
```
    .venv/bin/flask run
```

---
## Docs
As [docs](http://localhost:5000/api/docs) podem ser acessadas pelo endpoint /docs

As docs são feitas com a estrutura [Swwager](https://swagger.io/) através da extensão [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)

---
## Links
[GitHub](https://github.com/Orbeli/desafio-paschoalotto) - GitHub do projeto  

---
## Author
Gabriel Orbeli Rodrigues Belíssimo

[E-mail](mailto:gabriel.orbeli@gmail.com)
[GitHub](https://github.com/Orbeli)
[Linkedin](https://www.linkedin.com/in/gabriel-orbeli-436815171/)
