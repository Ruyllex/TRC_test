# TRC Project

Este es un test de TRC, consiste en una aplicación hecha en **python** con **Flask** para el backend y **Next.js 14 con Tailwind CSS** para el frontend, que se le pueden enviar PDF para que los procese y devuelva las palabras filtras del mismo. Además, está dockerizado para facilitar su despliegue y ejecución.

## 🚀 Tecnologías Utilizadas

### Backend:
- Flask

### Frontend:
- Next.js 14
- React 18
- Tailwind CSS

## 🛠️ Instalación y Configuración

### 1️⃣ Requisitos Previos
Asegúrate de tener instalados:
- **Docker** y **Docker Compose**
- **Node.js** (versión compatible con Next.js)
- **Java 17+** para el backend
- **PostgreSQL** si decides ejecutarlo sin Docker

### 2️⃣ Clonar el Repositorio
```sh
git clone https://github.com/Ruyllex/TRC_test.git
cd TRC_test
```

### 3️⃣ Levantar el Proyecto con Docker

#### 🔹 Opción 1: Usando `docker-compose`
```sh
docker-compose up --build
```
Esto construirá y ejecutará los servicios de frontend, backend y base de datos.

#### 🔹 Opción 2: Levantar los Servicios Individualmente
```sh
# Backend
cd BACK
py app.py
```
```sh
# Frontend
cd FRONT
npm install
npm run dev
```

## 🔥 Uso de la Aplicación
- El frontend estará disponible en: [`http://localhost:3000`](http://localhost:3000)
- El backend (API) estará en: [`http://localhost:5000`](http://localhost:5000)

## 🛠️ Troubleshooting
Si tienes problemas con las dependencias, ejecuta:
```sh
npm install --legacy-peer-deps  # Para resolver conflictos en Next.js
```

Si Docker está tardando mucho en construir las imágenes, intenta:
```sh
docker-compose build --no-cache
```

---
¡Listo! Ahora tienes tu Aplicación está en marcha 🚀


