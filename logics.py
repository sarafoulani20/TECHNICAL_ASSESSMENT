from db import collection

def get_default_error_message(columns):
    """Base error message used in this application"""
    return {"error": "Please specify a valid column",
            "valid_columns": columns,
            }


def get_avg(target_column):
    """Returns the average of all the records. It ignores non-numeric fields"""

    columns = list(collection.find_one({}, {'_id': 0}).keys())

    if target_column in columns:
        records = list(collection.aggregate([
            # get average of the specified column in the db
            {'$group': {'_id': '', 'avg': {'$avg': '$' + target_column}}},
        ]))
        return {"average": records[0]['avg']}
    else:
        return get_default_error_message(columns)


def get_count(target_column):
    """Return counts of value in a column"""

    columns=list(collection.find_one({}, {'_id': 0}).keys())

    if target_column in columns:
        records=list(collection.aggregate([
            # get counts of the specified column in the db
            {'$group': {'_id': '$' + target_column, 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$project': {'_id': 0, 'count': 1, 'value': '$_id'}},
        ]))
        return {"counts": records}
    else:
        return get_default_error_message(columns)
