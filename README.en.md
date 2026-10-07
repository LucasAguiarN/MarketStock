<h1 align="center"; style="font-weight: bold;">Market Stock</h1>

<h3 align="center"><img  alt="Impacta College" width = "400px" src="https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png"></h3>

<p>
    <img src="https://img.shields.io/badge/Status-Completed-brightgreen" alt="Status = Completed">
    <img src="https://img.shields.io/badge/Documentation-Complete-brightgreen" alt="Documentation: Complete">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
    <a href="./README.md" target="_blank"><img title="PT-BR" src="https://img.shields.io/badge/docs-pt--BR-blue" alt="README PT-BR"></a>
    <a href="./README.en.md" target="_blank"><img title="EN-US" src="https://img.shields.io/badge/docs-en--US-blue" alt="README EN-US"></a>
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
    <a href="#about">About</a> • 
    <a href="#team">Team Members</a> •
    <a href="#requirements">Requirements</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#how-it-works">Features</a> •
    <a href="#endpoints">API Endpoints</a> •
    <a href="#license">License</a>
</p>

<h2 id="about">📖 About</h2>
Project for the Full Stack Frameworks course, taught by professor Carlos Rafael Magalhães Fernandes at Impacta College, during the fourth semester of the Systems Analysis and Development program, taken in the 1st semester of 2026.

This application is a system for managing the stock and sales of mini markets, ensuring security, access control, and efficient management of products and sales.

This project's interface was built with React and is located in the following repository: <a href="https://github.com/vegacode03/MarketStock-Frontend">MarketStock-Frontend.</a>

<h2 id="team">👥 Team Members</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/ivykkj.png" width="100" alt="Photo"/><br>
      <b>Cauan de Melo Silva</b><br><br>
        <a href="https://www.linkedin.com/in/cauan-de-melo-silva" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
        <a href="https://github.com/ivykkj" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/Isaacnasc.png" width="100" alt="Photo"/><br>
      <b>Isaac do Nascimento Silva</b><br><br>
        <a href="https://www.linkedin.com/in/isaac-nasc" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
      <a href="https://github.com/Isaacnasc" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/vegacode03.png" width="100"  alt="Photo"/><br>
      <b>Leonardo Borges Soares</b><br><br>
      <a href="https://www.linkedin.com/in/leonardo-borges-ab2985137/" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
      <a href="https://github.com/vegacode03" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/LucasAguiarN.png" width="100"  alt="Photo"/><br>
      <b>Lucas Aguiar Nunes</b><br><br>
      <a href="https://www.linkedin.com/in/lucas-aguiar-nunes" target="_blank"><img title="Connect" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
      <a href="https://github.com/LucasAguiarN" target="_blank"><img title="Follow me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/></a>
    </td>
  </tr>
</table>

<h2 id="requirements">📦 Requirements</h2>

In the project's root directory, create a `.env` file based on the 
<a href="./.env.example">`.env.example`</a> file.

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.8-blue" alt="Python = 3.8"><br>

Make sure Docker is installed if you want to run the project in a container

In the project's root directory, build and run the container
```bash
docker-compose up --build
```
<br>

To run locally without a container, make sure Python is installed, and in the project's root directory create a virtual environment
```bash
python -m venv .venv
```
Activate the virtual environment in the terminal<br>
&emsp;&emsp;Windows
```bash
.venv\Scripts\activate.bat
```
&emsp;&emsp;Linux
```bash
source .venv/bin/activate
```
Run the command to install the libraries<br>
```bash
pip install -r requirements.txt
```
Run the command to start the project<br>
```bash
python run.py
```

<h2 id="architecture">🧩 System Architecture</h2>

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

<h2 id="how-it-works">⚙️ Features</h2>

### 1️⃣ Mini Market Registration (Seller)
Mini markets must register by providing the following fields:
- **Name**
- **Tax ID (CNPJ)**
- **Email**
- **Phone number**
- **Password**
- **Status** (Default: Inactive)

#### 🔹 Seller Activation Flow:
1. After registration, a 4-digit code is sent via **WhatsApp (Twilio)** to the seller.
2. The seller must enter the code received to activate their account.
3. Only activated sellers can log in and manage products.

---

### 2️⃣ Seller Authentication
- The system must use **JWT** or **OAuth** for authentication.
- Deactivated sellers cannot log in.

---

### 3️⃣ Product Management
An authenticated seller can:
- **Register products** with the following fields:
  - Name
  - Price
  - Quantity
  - Status (Active/Inactive)
  - Image
- **List registered products**
- **Edit a product**
- **View product details**
- **Deactivate products**

**Rules:**
- A seller can only view and manage their own products.

---

### 4️⃣ Selling Products
- The seller can make a sale by providing:
  - Product
  - Quantity
- Sales must be stored in the `Sales` table, containing:
  - Product ID
  - Quantity sold
  - Product price at the time of sale

**Rules:**
- It is not possible to sell more than the quantity available in stock.
- Deactivated products cannot be sold.
- Inactive sellers cannot make sales.


## 🛠️ Technologies Used
- **Back-end:** Python + Flask
- **Front-end:** React.js
- **Database:** SQLite
- **Authentication:** JWT or OAuth
- **Messaging:** Twilio (for sending the WhatsApp activation code)

## 📊 Dashboard and Reports
- Implementation of a panel for displaying reports and sales analysis.
- Real-time stock monitoring.

<h2 id="endpoints">🛠️ API Endpoints</h2>

Seller Registration
```bash
  curl -X POST "http://localhost:5000/api/sellers" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Mini Mercado X", "cnpj": "00.000.000/0001-00", "email": "mercado@email.com", "celular": "559999999999", "senha": "123456"}'
```
Seller Activation via WhatsApp
```bash
  curl -X POST "http://localhost:5000/api/sellers/activate" \
       -H "Content-Type: application/json" \
       -d '{"celular": "559999999999", "codigo": "1234"}'
```
Authentication
```bash
  curl -X POST "http://localhost:5000/api/sellers/login" \
       -H "Content-Type: application/json" \
       -d '{"email": "mercado@email.com", "senha": "123456"}'
```
Update Seller
```bash
  curl -X PUT "http://localhost:5000/api/sellers/me" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Mini Mercado X", "email": "mercado@email.com", "celular": "559999999999"}'
```
### 3️⃣ Product Management
Register Product
```bash
  curl -X POST "http://localhost:5000/api/products" \
       -H "Authorization: Bearer YOUR_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Arroz", "preco": 10.50, "quantidade": 100, "imagem": "url_da_imagem"}'
```
List Products
```bash
  curl -X GET "http://localhost:5000/api/products" \
       -H "Authorization: Bearer YOUR_TOKEN"
```
Edit Product
```bash
  curl -X PUT "http://localhost:5000/api/products/<int:produto_id>" \
       -H "Authorization: Bearer YOUR_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Arroz Integral", "preco": 12.00, "quantidade": 50}'
```
View Product Details
```bash
  curl -X GET "http://localhost:5000/api/products/<int:produto_id>" \
       -H "Authorization: Bearer YOUR_TOKEN"
```
Deactivate Product
```bash
  curl -X PATCH "http://localhost:5000/api/products/<int:produto_id>/inactivate" \
       -H "Authorization: Bearer YOUR_TOKEN"
```
### 4️⃣ Make a Sale
Create Sale
```bash
  curl -X POST "http://localhost:5000/api/sales" \
       -H "Authorization: Bearer YOUR_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"produtoId": 1, "quantidade": 2}'
```

<h2 id="license">📜 License</h2>
This project is for educational purposes and is available under the <a href="./LICENSE">MIT License.</a>