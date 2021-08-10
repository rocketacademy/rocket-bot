from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

flask_app = Flask(__name__)
app = App(
  token=os.environ.get("SLACK_BOT_TOKEN"),
  signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
handler = SlackRequestHandler(app)

@app.event("app_mention")
def event_test(body, say, logger):
  result = body["event"]["text"].split("Post this -")
  result[1].strip()
  say("Hello!!! "+result[1].strip())

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# pip install -r requirements.txt
# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
# FLASK_APP=app.py FLASK_ENV=development flask run -p 3000
# ngrok http 3000
