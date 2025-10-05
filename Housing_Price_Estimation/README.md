## Housing Price Estimation using Linear Regression

**Author: Abhishek Dey**


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

* [Exploratory Data Analysis (EDA)]('notebooks/eda.ipynb')

* [Experiments]('notebooks/experiments.ipynb')

### Model Training

```
python3 src/train.py

```

### Model Evaluation

```

python3 src/eval.py

```

### Terminal-1 : Run FastAPI backend 

```

uvicorn src.api:app --host 0.0.0.0 --port 8000

```

### Terminal-2 : Run Streamlit app 

```
streamlit run app.py

```