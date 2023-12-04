import json, os


def read_all_customer(file):
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, file)
        # Opening JSON file
        f = open(path)

        # check is the file is empty
        if os.path.getsize(path) == 0:
            return []

        # returns JSON object as
        # a dictionary
        customer_data = json.load(f)

        # Closing file
        f.close()
        return customer_data
    except Exception:
        print(Exception)
