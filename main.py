import profile
import requests
from bs4 import BeautifulSoup as bs

user = input("\nEnter Your Github Username: ")
url = 'https://github.com/'+user
r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print("\nHere's link for profile image : ")
print(profile_image,"\n")