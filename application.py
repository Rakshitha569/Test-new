from flask import Flask, jsonify
import requests
import pyAgrum as gum
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Simple App!"

@app.route('/data')
def get_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

@app.route('/plot')
def plot():
    # Create a simple Bayesian Network using pyAgrum
    bn = gum.BayesNet('SimpleBN')
    bn.add(gum.LabelizedVariable('A', 'A', 2))
    bn.add(gum.LabelizedVariable('B', 'B', 2))
    bn.addArc('A', 'B')
    bn.cpt('A').fillWith([0.6, 0.4])
    bn.cpt('B')[{'A': 0}] = [0.2, 0.8]
    bn.cpt('B')[{'A': 1}] = [0.75, 0.25]

    # Plot a simple graph using matplotlib
    plt.figure(figsize=(5, 5))
    gum.image(bn)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f'<img src="data:image/png;base64,{plot_url}"/>'

if __name__ == '__main__':
    app.run(debug=True)

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
 

# import requests
# from bs4 import BeautifulSoup

# def fetch_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return None

# def parse_page(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     titles = soup.find_all('h2')
#     for idx, title in enumerate(titles, start=1):
#         print(f"{idx}. {title.get_text()}")

# def main():
#     url = 'https://example.com'
#     html = fetch_page(url)
#     if html:
#         parse_page(html)

# if __name__ == "__main__":
#     main()
