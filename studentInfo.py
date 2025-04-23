from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")

URL = "https://mmmut.samarth.edu.in/index.php/examstudent/data-correction/view?id="

# Login to samarth
session = requests.Session()
login_url = "https://mmmut.samarth.edu.in/index.php/site/login"

login_page = session.get(login_url)

new_soup = BeautifulSoup(login_page.content, 'html.parser')
csrf_token = new_soup.find('input', {'name': '_csrf'}).get('value')

login_data = {
            'LoginForm[username]': username,
            'LoginForm[password]': password,
            '_csrf': csrf_token
        }

headers = {'User-Agent': 'Mozilla/5.0'}

login_response = session.post(login_url, data=login_data, headers=headers)
print(f"Status code: {login_response.status_code}")



