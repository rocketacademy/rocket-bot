# Install dependencies

All the dependencies are mentioned in the requirements.txt file. To install, run

pip install -r requirements.txt

# Run the Flask server

FLASK_APP=app.py FLASK_ENV=development flask run -p 3000

You can use Ngrok to expose your local server to the Internet.

ngrok http 3000

https://www.activestate.com/blog/how-to-build-a-twitter-bot-for-slack-with-python/