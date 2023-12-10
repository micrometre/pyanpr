# flask_sse.py

from flask import Flask, Response
import time

app = Flask(__name__)

@app.route("/sse", methods=["GET"])
def sse():
    def sse_events():
        # We are using a counter here for sending some value in the response
        counter = 0

        while True:
            # In real world applications here we will fetch some data

            # Remember to yield to continue to sending data
            yield "data: message counter - {}\n\n".format(counter)

            # Increase the counter for the next message
            counter += 1
            # Put a sleep for 2 second
            time.sleep(2)

    # Send back response
    return Response(sse_events(), mimetype="text/event-stream")
