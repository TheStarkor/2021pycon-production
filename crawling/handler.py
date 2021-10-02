
import requests
from bs4 import BeautifulSoup

def main(event, context):
    req = requests.get('https://2021.pycon.kr')
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    images = soup.select(
        'img'
    )
    
    for image in images:
       print(image.get('src'))

if __name__ == "__main__":
    main(None, None)