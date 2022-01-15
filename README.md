# IUM
ML small project for studies created by Jan Piotrowski and Bartosz Kopeć. We have to classify if clients will buy something in theirs session or not. 

## Setting up the environment
1. Install `poetry`: https://python-poetry.org/docs/#installation
2. Create an environment with `poetry install`
3. Run `poetry shell`
4. To add a new package run `poetry add <package>`. Don't forget to commit the lockfile.
5. To run unit tests for your service use `poetry run pytest` or simply `pytest` within `poetry shell`.

## Jupyter Notebook
To start jupyter notebook
```shell
jupyter notebook
```

##  API
To start the server
```shell
uvicorn IUM.main:app
```

Next, you can make "get" request to check if server is running [127.0.0.1:8000](http://127.0.0.1:8000)

To call "classify" model method make request to [127.0.0.1:8000/classify](http://127.0.0.1:8000/classify)
with JSON as body
```json
{
  "session_id": int,
  "user_id": int,
  "product_id": int
}
```

You could also make request in [docs](http://127.0.0.1:8000/docs#/default/classify_classify__post). You have to click "Try it out" and change ids. This should be the easiest method to test app.

## Project Organization

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── project_name       <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── tests              <- Unit tests
    |
    ├── poetry.lock        <- Lockfile which allows complete environment reproduction
    │
    └── pyproject.toml     <- file with settings and dependencies for the environment
