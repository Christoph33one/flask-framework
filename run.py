import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# This is template rendering. This inherits code from the base template
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # taking file path value and passing it as json_data.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

    # python is opening the Json file using "r"
    # (read only) then assigning it the new varible
    # we created called json_data


# route to give h1 titles in about.html and link and show a h1 text.
@app.route("/about/<member_name>")
# angle brakets will pass the url path into the view below.
def about_memeber(member_name):
    member = {}
    # taking file path value and passing it as json_data.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:  # to iritate through data array.
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)

    return render_template("about.html", page_title="about", company=data)
    # passing data with a new Variable (page_title) as an
    # expression {{url_for}}
    # this data is sent to the base.html file and then to separate html files
    # to meet the required data for each file.

    # company=data is assinging a new varible called 'company'
    # that is sent throught to the html template, which is equal to
    # list of data that is loading.


@app.route("/contact",  methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
        # this is a way of requesting the key, this is how we access
        # a forms data from the back end!
    return render_template("contact.html", page_title="history")


@app.route("/history")
def history():
    return render_template("history.html", page_title="history")


# the ip and its value / porth and its value. these are used when deploying in
# heruko. In the config vars section, you need to enter both ports and values
# to the get app running, important!!!
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
