from flask import Flask, render_template
import requests
from NYTsecrets import api_key

app = Flask(__name__)

def get_top_articles():
    """
    Retrieve the top 5 articles from the New York Times Technology section.

    Returns:
        list: A list of dictionaries containing the 'title' and 'url' of the top 5 technology articles.
    """
    url = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={api_key}'
    response = requests.get(url)
    data = response.json()
    top_articles = data['results'][:5]
    return top_articles

@app.route('/')
def home():
    """Render the default home page."""
    return '<h1>Welcome!</h1>'

@app.route('/name/<name>')
def hello(name):
    """
    Render a personalized greeting.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A rendered HTML template with the personalized greeting.
    """
    return render_template('name.html', name=name)

@app.route('/headlines/<name>')
def headlines(name):
    """
    Render the top 5 technology headlines for the given name.

    Args:
        name (str): The name of the person for the personalized headline display.

    Returns:
        str: A rendered HTML template with the top 5 technology headlines.
    """
    top_articles = get_top_articles()
    headlines_with_links = [{'title': article['title'], 'url': article['url']} for article in top_articles]
    return render_template('headlines.html', name=name, headlines_with_links=headlines_with_links)

@app.route('/links/<name>')
def links(name):
    """
    Render the top 5 technology headlines with links for the given name (Extra Credit 1).

    Args:
        name (str): The name of the person for the personalized headline display with links.

    Returns:
        str: A rendered HTML template with the top 5 technology headlines and links.
    """
    top_articles = get_top_articles()
    headlines_with_links = [{'title': article['title'], 'url': article['url']} for article in top_articles]
    return render_template('links.html', name=name, headlines_with_links=headlines_with_links)

@app.route('/images/<name>')
def images(name):
    """
    Render the top 5 technology headlines with links and thumbnails in a table for the given name (Extra Credit 2).

    Args:
        name (str): The name of the person for the personalized headline display with links and thumbnails.

    Returns:
        str: A rendered HTML template with the top 5 technology headlines, links, and thumbnails in a table.
    """
    top_articles = get_top_articles()
    headlines_with_links_and_thumbnails = [{'title': article['title'], 'url': article['url'], 'thumbnail': article['multimedia'][0]['url']} for article in top_articles if article['multimedia']]
    return render_template('images.html', name=name, headlines_with_links_and_thumbnails=headlines_with_links_and_thumbnails)

if __name__ == '__main__':
    app.run(debug=True)
