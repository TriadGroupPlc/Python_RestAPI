import readAllCustomers
import pandas as pd


def get_customer(reference, file):
    saved_customers = readAllCustomers.read_all_customer(file)
    if saved_customers is None:
        return None
    else:
        # load data into a DataFrame object:
        df = pd.DataFrame(saved_customers)
        # find if the customer reference already exists
        # return df['Reference'].values.__contains__(customer['Reference'])
        return df.loc[df['Reference'] == reference]


def customer_exists(reference, file):
    saved_customers = readAllCustomers.read_all_customer(file)
    if saved_customers is None:
        return False
    else:
        # load data into a DataFrame object:
        df = pd.DataFrame(saved_customers)
        # find if the customer reference already exists
        return df['Reference'].values.__contains__(reference)

