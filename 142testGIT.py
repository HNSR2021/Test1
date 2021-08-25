from flask import Flask, request


app = Flask(__name__)
@app.route('https://flasktestapp-test.herokuapp.com/')
def hello():
  return 'hello world'



# @app.route('/', methods=["POST", "GET"])
# def webhook():
   # if request.method == "GET":
      #  return "Not connected to DF"
   # elif request.method == "POST":
     #   payload = request.json
     #   user_response = (payload['queryResult']['queryText'])
     #   bot_response = (payload['queryResult']['fulfillmentText'])
      #  if user_response or bot_response != "":
         #   print("user: " + user_response)
        #    print("bot: " + bot_response)
      #  return "msg received"
   # else:
      #  print("request.data")
      #  return "200"


if __name__ == '__main__':
    app.run(debug=True)