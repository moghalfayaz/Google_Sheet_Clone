from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sheets.db"
db = SQLAlchemy(app)

# Database Model
class Spreadsheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.Text, nullable=False)

# Initialize Database
with app.app_context():
    db.create_all()

# Home Route
@app.route("/")
def index():
    return render_template("index.html")

# Save Spreadsheet Data
@app.route("/save", methods=["POST"])
def save_sheet():
    data = request.json
    sheet_name = data.get("name")
    sheet_data = data.get("data")

    existing_sheet = Spreadsheet.query.filter_by(name=sheet_name).first()
    if existing_sheet:
        existing_sheet.data = str(sheet_data)
    else:
        new_sheet = Spreadsheet(name=sheet_name, data=str(sheet_data))
        db.session.add(new_sheet)

    db.session.commit()
    return jsonify({"message": "Sheet saved successfully!"})

# Load Spreadsheet Data
@app.route("/load/<name>", methods=["GET"])
def load_sheet(name):
    sheet = Spreadsheet.query.filter_by(name=name).first()
    if sheet:
        return jsonify({"name": sheet.name, "data": eval(sheet.data)})
    return jsonify({"error": "Sheet not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
