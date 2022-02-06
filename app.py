import pandas as pd
from flask import Flask, jsonify, request

from logics import get_avg, get_count
from db import collection

app = Flask(__name__)


@app.cli.command("load_db")
def load_db():
    """Loads data from the csv into the db"""
    if next(collection.find(), None):
        print("Database already has data")
        return

    print("Loading data into db...", "\n\n\n")
    data = pd.read_csv(
        'data/WA_Fn-UseC_-HR-Employee-Attrition.csv').to_dict(orient='records')
    collection.insert_many(data)
    print("inserted records to the db")


@app.route("/upload", methods=["POST"])
def add_new_record():
    """Adds a new record to the db"""
    record = request.get_json()
    result = collection.update_one(record, {"$set": record}, upsert=True)
    response = "record added" if result.upserted_id else "record updated"
    return jsonify({"message": response})


@app.route("/avg")
def get_average_endpoint():
    """Returns the average of all the records. It ignores non-numeric fields"""
    target_column = request.args.get("column")
    return get_avg(target_column)


@app.route("/count")
def get_counts_endpoint():
    """Return counts of value in a column"""
    target_column = request.args.get("column")
    return get_count(target_column)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
