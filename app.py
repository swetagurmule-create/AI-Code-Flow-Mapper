from flask import Flask, render_template, request

app = Flask(__name__)


def analyze_code(code):
    code = code.lower()

    if "flask" in code:
        return {
            "architecture": "Flask Web Application",
            "components": [
                "User",
                "Flask Application",
                "Routes",
                "Business Logic"
            ],
            "summary": "This is a Flask-based web application. A user sends a request, Flask processes it, executes the business logic, and returns a response."
        }

    elif "class" in code:
        return {
            "architecture": "Object-Oriented Program",
            "components": [
                "Class",
                "Objects",
                "Methods"
            ],
            "summary": "This program follows Object-Oriented Programming principles using classes and objects."
        }

    else:
        return {
            "architecture": "General Python Program",
            "components": [
                "Input",
                "Processing",
                "Output"
            ],
            "summary": "This appears to be a general Python program."
        }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        code = request.form.get("code", "")
        result = analyze_code(code)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
