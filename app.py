from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Data Analyst",
        'location': "Bengaluru, India",
        'salary': "Rs. 10,00,000"
    },
    {
        'id': 2,
        'title': "Data Scientist",
        'location': "Delhi, India",
        'salary': "Rs. 10,50,000"
    },
    {
        'id': 3,
        'title': "Frontend Engineer",
        'location': "Chennai, India",
        'salary': "Rs. 10,00,000"
    },
    {
        'id': 4,
        'title': "Backend Engineer",
        'location': "Kochi, India",
        'salary': "Rs. 10,00,000"
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS, Company_name="RAKHI")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
