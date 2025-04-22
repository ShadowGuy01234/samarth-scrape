from bs4 import BeautifulSoup
import requests

URL = "https://mmmut.samarth.edu.in/index.php/examstudent/data-correction/view?id="

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

metaData = soup.find('meta', {'name' : 'csrf-token'})
StudentID = metaData['content'] if metaData else None

newURL = f"https://mmmut.samarth.edu.in/index.php/examstudent/data-correction/view?id={StudentID}"

# print(StudentID)
# print(soup)