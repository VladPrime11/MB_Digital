# DjangoMB Project

## Requirements
- Python 3.12+
- PostgreSQL (for production)
- Docker and Docker Compose (for running in containers)

---

## Running Locally Without Docker

### 1. Clone the Repository
```bash
git clone https://github.com/VladPrime11/MB_Digital.git
cd DjangoMB
```
### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```
### 3. Configure the `.env` File:
```bash
SECRET_KEY=b5^v!r3z@=j%k6)q*4pd7fslg

DB_NAME=mbdigital_prod_db
DB_USER=mbdigital_admin
DB_PASSWORD=MBd1g1talStr0ngP@ss
DB_HOST=db
DB_PORT=5432

DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
### 4. Apply Migrations and Run the Server
```bash
python manage.py migrate
python manage.py runserver
```
---
## Running with Docker in Development Mode
### 1. Clone the Repository
```bash
git clone https://github.com/VladPrime11/MB_Digital.git
cd DjangoMB
```
### 2. Configure the `.env` File
```bash
SECRET_KEY=b5^v!r3z@=j%k6)q*4pd7fslg

DB_NAME=mbdigital_prod_db
DB_USER=mbdigital_admin
DB_PASSWORD=MBd1g1talStr0ngP@ss
DB_HOST=db
DB_PORT=5432

DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
### 3. Run Docker Containers
```bash
docker-compose -f docker-compose.dev.yml up --build
```
The project will be available at http://localhost:8000

---
## Running with Docker in Production Mode
### 1. Clone the Repository
```bash
git clone https://github.com/VladPrime11/MB_Digital.git
cd DjangoMB
```
### 2. Configure the `.env` File
```bash
SECRET_KEY=b5^v!r3z@=j%k6)q*4pd7fslg

DB_NAME=mbdigital_prod_db
DB_USER=mbdigital_admin
DB_PASSWORD=MBd1g1talStr0ngP@ss
DB_HOST=db
DB_PORT=5432

DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
### 3. Run Docker Containers
```bash
docker-compose -f docker-compose.prod.yml up --build
```
The project will be available at http://localhost:8000