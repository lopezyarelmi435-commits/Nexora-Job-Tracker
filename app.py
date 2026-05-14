from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Initial dummy data
jobs = [
    {"id": 1, "company": "Google", "position": "Product Manager", "status": "Applied", "date": "2024-05-12"},
    {"id": 2, "company": "Apple", "position": "UX Designer", "status": "Wishlist", "date": "2024-05-15"},
    {"id": 3, "company": "Netflix", "position": "Data Analyst", "status": "Interviewing", "date": "2024-05-16"}
]

@app.route("/")
def home():
    return render_template("index.html", jobs=jobs)

@app.route("/add", methods=["POST"])
def add_job():
    company = request.form.get("company")
    position = request.form.get("position")
    status = request.form.get("status")
    # Grab the date from the form; if empty, use today's date
    date_applied = request.form.get("date")
    if not date_applied:
        date_applied = datetime.now().strftime("%Y-%m-%d")
    
    if company and position:
        new_id = max([job['id'] for job in jobs], default=0) + 1
        jobs.append({
            "id": new_id, 
            "company": company, 
            "position": position, 
            "status": status, 
            "date": date_applied
        })
    return redirect(url_for("home"))

@app.route("/delete/<int:job_id>")
def delete_job(job_id):
    global jobs
    jobs = [job for job in jobs if job['id'] != job_id]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)