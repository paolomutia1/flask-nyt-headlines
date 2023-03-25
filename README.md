# Top Technology Headlines

This Flask application displays the top 5 technology headlines from the New York Times. It also includes personalized greetings and additional features as part of the extra credit.

## Features

- Personalized greeting based on the user's name
- Top 5 technology headlines
- Headlines with clickable links (Extra Credit 1)
- Headlines with links and thumbnail images in a table (Extra Credit 2)

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/yourusername/top-tech-headlines.git

2. Change directory into the project folder:

cd top-tech-headlines

3. Install the required dependencies:

pip install -r requirements.txt

4. Replace the `api_key` value in `NYTsecrets.py` with your own New York Times API key.

## Usage

1. Run the Flask application:

python top_headlines.py

2. Open your web browser and visit `http://127.0.0.1:5000/` to view the application.

3. Use the following routes to access the different features:

- Personalized greeting: `http://127.0.0.1:5000/name/<your_name>`
- Top 5 headlines: `http://127.0.0.1:5000/headlines/<your_name>`
- Headlines with links (Extra Credit 1): `http://127.0.0.1:5000/links/<your_name>`
- Headlines with links and thumbnail images (Extra Credit 2): `http://127.0.0.1:5000/images/<your_name>`

