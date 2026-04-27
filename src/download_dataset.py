import os
from dotenv import load_dotenv, find_dotenv


# loading token  from .env file
load_dotenv(find_dotenv())

# checking loading the API token
if not os.getenv("KAGGLE_KEY"):
    print("error: file .env or wariables not found")
    exit(1)


import kaggle

# name dataset
dataset = "syedsaqlainhussain/sql-injection-dataset"
# loading and Unpacking archive
kaggle.api.dataset_download_files(dataset=dataset, path=".", unzip=True)
