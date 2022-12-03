import os
from dotenv import load_dotenv
from manage import main

main()
load_dotenv()

hola = os.environ['HOLA']

print(hola)