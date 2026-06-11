# 🚢 Titanic: Una Historia de Datos

Aplicación web interactiva construida con **Streamlit** que narra la tragedia del Titanic a través de datos. El análisis explora quiénes eran los pasajeros, la desigualdad económica a bordo y los factores que determinaron quién sobrevivió.

---

## Demo



https://github.com/user-attachments/assets/10de72f6-6e25-4b5b-84c7-e3f333e27c0f



---

## Vista previa

La app se organiza en **5 capítulos** navegables desde la barra lateral:

| Capítulo | Contenido |
|----------|-----------|
| 🏠 Introducción | Métricas globales y contexto histórico |
| 👥 I. Perfil de los Pasajeros | Distribución por clase, edad y composición demográfica |
| 💰 II. El Dinero a Bordo | Tarifas, desigualdad económica y estatus social |
| 🌊 III. La Noche del Hundimiento | Tasa de supervivencia por clase, sexo y edad |
| 🔗 IV. Patrones y Correlaciones | Heatmap de correlaciones, puertos de embarque, tamaño familiar |
| 📊 V. Dashboard Final | Resumen visual completo + conclusiones |

---

## Requisitos

- Python 3.8 o superior
- pip

Dependencias principales:

```
streamlit
pandas
numpy
plotly
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/MajoRodri/Titanic
cd Titanic
```

### 2. Crear y activar un entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install streamlit pandas numpy plotly
```

### 4. Agregar el dataset

Coloca el archivo `Titanic-Dataset.csv` en la raíz del proyecto (mismo nivel que `app.py`).  
Puedes descargarlo desde [Kaggle — Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset).

---

## Ejecución

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`.

---

## Docker

### Opción A — Usar la imagen publicada en Docker Hub

```bash
docker pull majorodri/titanic-app
docker run -p 8501:8501 majorodri/titanic-app
```

Abre `http://localhost:8501` en tu navegador.

> **Nota:** el dataset (`Titanic-Dataset.csv`) está incluido en la imagen, por lo que no necesitas montarlo manualmente.

### Opción B — Construir la imagen localmente

```bash
git clone https://github.com/MajoRodri/Titanic
cd Titanic
docker build -t titanic-app .
docker run -p 8501:8501 titanic-app
```

---

## Estructura del proyecto

```
Titanic/
├── app.py               # Aplicación Streamlit principal
├── Titanic-Dataset.csv  # Dataset (no incluido en el repositorio)
├── Titanic.ipynb        # Notebook exploratorio
├── Dockerfile           # Imagen Docker de la aplicación
├── .dockerignore        # Archivos excluidos del build
├── requirements.txt     # Dependencias Python
├── venv/                # Entorno virtual (no incluido en git)
└── README.md
```

---

## Dataset

El dataset contiene **891 registros** con las siguientes variables:

| Variable | Descripción |
|----------|-------------|
| `Survived` | 0 = Fallecido, 1 = Superviviente |
| `Pclass` | Clase del pasaje (1, 2, 3) |
| `Name` | Nombre del pasajero |
| `Sex` | Sexo |
| `Age` | Edad |
| `SibSp` | Hermanos / cónyuge a bordo |
| `Parch` | Padres / hijos a bordo |
| `Ticket` | Número de ticket |
| `Fare` | Tarifa pagada (£) |
| `Cabin` | Número de camarote |
| `Embarked` | Puerto de embarque (S / C / Q) |

---

## Hallazgos principales

- **1ª Clase: 63 %** de supervivencia vs. **3ª Clase: 24 %** — el dinero compró acceso a los botes salvavidas.
- **Mujeres de 1ª Clase: 97 %** vs. **Mujeres de 3ª Clase: 50 %** — el protocolo "mujeres y niños primero" se aplicó de forma desigual.
- **Niños menores de 12 años** tuvieron la mayor tasa de supervivencia (57 %).
- **Familias pequeñas (1–3 miembros)** sobrevivieron más (55 %) que los viajeros solos (30 %) o familias grandes (16 %).
- La **clase social es el predictor más fuerte** de supervivencia, con una correlación de −0.34 con `Pclass`.
