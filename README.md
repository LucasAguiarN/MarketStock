<h1 align="center"; style="font-weight: bold;">Market Stock</h1>

<h3 align="center"><img  alt="Faculdade Impacta" width = "400px" src="https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png"></h3>

<p>
    <img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status = Concluído">
    <img src="https://img.shields.io/badge/Documentação-Completa-brightgreen" alt="Documentação: Completa">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
</p>

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

<br>

<h1 align="center"; style="font-weight: bold;">Market Stock</h1>

<p align="center">
    <a href="#sobre">Sobre</a> • 
    <a href="#grupo">Integrantes do Grupo</a> •
    <a href="#requisitos">Requisitos</a> •
    <a href="#arquitetura">Arquitetura</a> •
    <a href="#how-it-works">Funcionalidades</a> •
    <a href="#endpoints">Endpoints da API</a> •
    <a href="#licença">Licença</a>
</p>

<h2 id="sobre">📖 Sobre</h2>
Projeto da Disciplina de Frameworks Full Stack, ministrada pelo professor Carlos Rafael Magalhães Fernandes  na Faculdade Impacta, durante o quarto semestre do curso Análise e Desenvolvimento de Sistemas cursado no 1º Semestre de 2026.

Essa aplicação consiste num sistema para gestão de estoque e vendas de mini mercados, garantindo segurança, controle de acesso e gestão eficiente de produtos e vendas.

A interface deste projeto foi feita em React e se encontra no seguinte repositório: <a href="https://github.com/vegacode03/MarketStock-Frontend">MarketStock-Frontend.</a>

<h2 id="grupo">👥 Integrantes do Grupo</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/ivykkj.png" width="100" alt="Foto"/><br>
      <b>Cauan de Melo Silva</b><br><br>
        <a href="https://www.linkedin.com/in/cauan-de-melo-silva" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
        <a href="https://github.com/ivykkj" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/Isaacnasc.png" width="100" alt="Foto"/><br>
      <b>Isaac do Nascimento Silva</b><br><br>
        <a href="https://www.linkedin.com/in/isaac-nascimento-1925232a3/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/Isaacnasc" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/vegacode03.png" width="100"  alt="Foto"/><br>
      <b>Leonardo Borges Soares</b><br><br>
      <a href="https://www.linkedin.com/in/leonardo-borges-ab2985137/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/vegacode03" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/LucasAguiarN.png" width="100"  alt="Foto"/><br>
      <b>Lucas Aguiar Nunes</b><br><br>
      <a href="https://www.linkedin.com/in/lucas-aguiar-nunes" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/LucasAguiarN" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
  </tr>
</table>

<h2 id="requisitos">📦 Requisitos</h2>

No diretório raiz do projeto, crie um arquivo `.env` com base no arquivo 
<a href="./.env.example">`.env.example`</a>.

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.8-blue" alt="Python = 3.8"><br>

Tenha o Docker instalado caso queria rodar o projeto num container

No diretório raiz do projeto, construa e execute o container
```bash
docker-compose up --build
```
<br>

Para rodar localmente sem ser via container tenha o Python instalado e no diretório raiz do projeto crie um ambiente virtual
```bash
python -m venv .venv
```
Ative o ambiente virtual no terminal<br>
&emsp;&emsp;Sistema Windows
```bash
.venv\Scripts\activate.bat
```
&emsp;&emsp;Sistema Linux
```bash
source .venv/bin/activate
```
Execute o comando para instalar as bibliotecas<br>
```bash
pip install -r requirements.txt
```
Execute o comando para iniciar o projeto<br>
```bash
python run.py
```

<h2 id="arquitetura">🧩 Arquitetura do Sistema</h2>

```
📦 MarketStock
├─ 🐳docker-compose.yml
├─ 🐳 Dockerfile
├─ 🔑.env
├─ 🔑.env.example
├─ 📖 README.md
├─ 📦 requirements.txt
├─ 🚀 run.py
├─ 🗄️ market_management.db
├─ 🚫 .gitignore
├─ ⚖️ LICENSE
├─ 📂 src
│  ├─ 🧠 Application
│  │  ├─ 🎮 Controllers
│  │  │  ├─ 📄 product_controller.py
│  │  │  ├─ 📄 report_controller.py
│  │  │  ├─ 📄 sale_controller.py
│  │  │  ├─ 📄 seller_controller.py
│  │  │  └─ 📄 user_controller.py
│  │  └─ ⚙️ Service
│  │     ├─ 📄 product_service.py
│  │     ├─ 📄 report_service.py
│  │     ├─ 📄 sale_service.py
│  │     ├─ 📄 seller_service.py
│  │     └─ 📄 user_service.py
│  ├─ ⚙️ config
│  │  └─ 📄 data_base.py
│  ├─ 🏛️ Domain
│  │  ├─ 📄 product.py
│  │  ├─ 📄 report.py
│  │  ├─ 📄 sale.py
│  │  ├─ 📄 seller.py
│  │  └─ 📄 user.py
│  ├─ 🔌 Infrastructure
│  │  ├─ 🌐 http
│  │  │  └─ 📄 whats_app.py
│  │  └─ 🗄️ Model
│  │     ├─ 📄 product.py
│  │     ├─ 📄 report.py
│  │     ├─ 📄 sale.py
│  │     ├─ 📄 seller.py
│  │     └─ 📄 user.py
│  └─ 🔀 routes.py
└─ 📂 static
│  ├─ 📘 Swagger.yaml
│  └─ 📂 uploads
```

<h2 id="how-it-works">⚙️ Funcionalidades</h2>

### 1️⃣ Cadastro de Mini Mercado (Seller)
Os mini mercados devem se cadastrar informando os seguintes campos:
- **Nome**
- **CNPJ**
- **E-mail**
- **Celular**
- **Senha**
- **Status** (Padrão: Inativo)

#### 🔹 Fluxo de Ativação do Seller:
1. Após o cadastro, um código de 4 dígitos é enviado via **WhatsApp (Twilio)** para o seller.
2. O seller deve inserir o código recebido para ativar sua conta.
3. Somente sellers ativados podem fazer login e gerenciar produtos.

---

### 2️⃣ Autenticação do Seller
- O sistema deve utilizar **JWT** ou **OAuth** para autenticação.
- Sellers inativados não podem fazer login.

---

### 3️⃣ Gerenciamento de Produtos
Um seller autenticado pode:
- **Cadastrar produtos** com os seguintes campos:
  - Nome
  - Preço
  - Quantidade
  - Status (Ativo/Inativo)
  - Imagem
- **Listar produtos** cadastrados
- **Editar produto**
- **Ver detalhes de um produto**
- **Inativar produtos**

**Regras:**
- O seller só pode visualizar e gerenciar seus próprios produtos.

---

### 4️⃣ Venda de Produtos
- O seller pode realizar uma venda informando:
  - Produto
  - Quantidade
- As vendas devem ser armazenadas na tabela `Vendas`, contendo:
  - ID do Produto
  - Quantidade vendida
  - Preço do produto no momento da venda

**Regras:**
- Não é possível vender mais do que a quantidade disponível em estoque.
- Produtos inativados não podem ser vendidos.
- Sellers inativos não podem realizar vendas.


## 🛠️ Tecnologias Utilizadas
- **Back-end:** Python + Flask
- **Front-end:** React.js
- **Banco de Dados:** SQLite
- **Autenticação:** JWT ou OAuth
- **Mensageria:** Twilio (para envio do código de ativação no WhatsApp)

## 📊 Dashboard e Relatórios
- Implementação de um painel para exibição de relatórios e análise de vendas.
- Monitoramento de estoque em tempo real.

<h2 id="endpoints">🛠️ Endpoints da API</h2>

Cadastro de Seller
```bash
  curl -X POST "http://localhost:5000/api/sellers" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Mini Mercado X", "cnpj": "00.000.000/0001-00", "email": "mercado@email.com", "celular": "559999999999", "senha": "123456"}'
```
Ativação de Seller via WhatsApp
```bash
  curl -X POST "http://localhost:5000/api/sellers/activate" \
       -H "Content-Type: application/json" \
       -d '{"celular": "559999999999", "codigo": "1234"}'
```
Autentificação
```bash
  curl -X POST "http://localhost:5000/api/sellers/login" \
       -H "Content-Type: application/json" \
       -d '{"email": "mercado@email.com", "senha": "123456"}'
```
Atualização de Seller
```bash
  curl -X PUT "http://localhost:5000/api/sellers/me" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Mini Mercado X", "email": "mercado@email.com", "celular": "559999999999"}'
```
### 3️⃣ Gerenciamento de Produtos
Cadastro de Produto
```bash
  curl -X POST "http://localhost:5000/api/products" \
       -H "Authorization: Bearer SEU_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Arroz", "preco": 10.50, "quantidade": 100, "imagem": "url_da_imagem"}'
```
Listar Produtos
```bash
  curl -X GET "http://localhost:5000/api/products" \
       -H "Authorization: Bearer SEU_TOKEN"
```
Editar Produto
```bash
  curl -X PUT "http://localhost:5000/api/products/<int:produto_id>" \
       -H "Authorization: Bearer SEU_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Arroz Integral", "preco": 12.00, "quantidade": 50}'
```
Ver Detalhes Produto
```bash
  curl -X GET "http://localhost:5000/api/products/<int:produto_id>" \
       -H "Authorization: Bearer SEU_TOKEN"
```
Inativar Produto
```bash
  curl -X PATCH "http://localhost:5000/api/products/<int:produto_id>/inactivate" \
       -H "Authorization: Bearer SEU_TOKEN"
```
### 4️⃣ Realizar Venda
Criar Venda
```bash
  curl -X POST "http://localhost:5000/api/sales" \
       -H "Authorization: Bearer SEU_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"produtoId": 1, "quantidade": 2}'
```

<h2 id="licença">📜 Licença</h2>
Este projeto é para fins educacionais e está disponível sob a <a href="./LICENSE">Licença MIT.</a>