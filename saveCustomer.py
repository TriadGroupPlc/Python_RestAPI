import readAllCustomers
import validateCustomer, json


def save_customer(customer, file):
    val = validateCustomer.find_ref_customer(customer['Reference'], file)
    if val == 1:
        return 'customer already exists'
    else:
        write_into_file(customer, file)
        return 'customer added successfully'


def write_into_file(customer, file):
    saved_customers = readAllCustomers.read_all_customer(file)
    if saved_customers is None:
        saved_customers = customer
    else:
        saved_customers.append(customer)
    with open(file, "w") as outfile:
        json.dump(saved_customers, outfile)
