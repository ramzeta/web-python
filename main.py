import os
from dotenv import load_dotenv

load_dotenv()
hola = os.environ['HOLA']

print(hola)