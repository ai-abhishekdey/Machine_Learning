## Housing Price Estimation using Linear Regression

**Author: Abhishek Dey**

### About:

This project is an exploration of a simple linear regression Housing Price Estimation project. The goal of this project is to demonstrate an AI application from **Notebook to Production**. I started this project with downloading the data from kaggle, Performed **automated EDA** and **feature selection**, Experimented model training with **MLflow Integration**. Then created a **Streamlit** app as front-end and **FastAPI** as backend. Then containerised the app using **Docker** and pushed the image to **Docker-hub**. Finally deployed the docker container in **AWS, AZURE and GOOGLE** cloud platforms 

### Create virtual environment

```

conda create -n ml_env python=3.10 -y

conda activate ml_env

pip install -r requirements.txt


```

### Dataset

* Download Housing price dataset from the below link

```
https://www.kaggle.com/datasets/sukhmandeepsinghbrar/housing-price-dataset

```

### Notebooks:

* [Exploratory Data Analysis (EDA)](notebooks/eda.ipynb)

* [Experiments](notebooks/experiments.ipynb)

### Model Training

```
python3 src/train.py

```

### Model Evaluation

```

python3 src/eval.py

```

### Terminal-1 : Run FastAPI backend  (Backend)

```

uvicorn src.api:app --host 0.0.0.0 --port 8000

```

### Terminal-2 : Run Streamlit app (Frontend)

```
streamlit run app.py

```

### Deployment:


* Navigate to [Deployment](Deployment/README.md)
