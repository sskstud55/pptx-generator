from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form.get("message")
    # Echo the message for now
    response = f"You said: {message}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
