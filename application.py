import flask

print "hello"
# from flask import Flask

# from flask import Flask

# application=Flask(__name__)

# @application.route("/")
# def hello_world():
#  return 'Hello World'

# ''' from flask import jsonify
# app = Flask(__name__)
# @app.route('/numbers/')

# def print_list():
#     #a=jsonify(list(range(5)))
#     return jsonify(list(range(5))) '''
# #if __name__=='__main__':
 

import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h2')
    for idx, title in enumerate(titles, start=1):
        print(f"{idx}. {title.get_text()}")

def main():
    url = 'https://example.com'
    html = fetch_page(url)
    if html:
        parse_page(html)

if __name__ == "__main__":
    main()
