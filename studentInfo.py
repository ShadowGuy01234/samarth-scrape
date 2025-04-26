from bs4 import BeautifulSoup
import requests
import traceback

username = "Enter_Your_username"
password = "Enter_your_password"

try:
    session = requests.Session()
    login_url = 'https://mmmut.samarth.edu.in/index.php/site/login'
    
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.content, 'html.parser')
    csrf_token = soup.find('input', {'name': '_csrf'}).get('value')
    
    # doing login
    login_data = {
        'LoginForm[username]': username,
        'LoginForm[password]': password,
        '_csrf': csrf_token
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    response = session.post(login_url, data=login_data, headers=headers)

    # Profile details page
    details_url = "https://mmmut.samarth.edu.in/index.php/examstudent/data-correction/view"
    response = session.get(details_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    student_data = {}

    table = soup.find('table', class_='table-bordered')

    if table:
        rows = table.find_all('tr')

        for row in rows:
            data = row.find_all('td')
            # print(data)
            key1 = data[0].get_text(strip=True)
            value1 = data[1].get_text(strip=True)
            student_data[key1] = value1
            key2 = data[2].get_text(strip=True)
            value2 = data[3].get_text(strip=True)
            student_data[key2] = value2

    else:
        print("No table found!")

    print(student_data)

except Exception as e:
    print("An error occurred:")
    traceback.print_exc()
