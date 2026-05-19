#import your own test data

def get_2_numeric_option_input(prompt, options=['0', '1']):
    while True:
        response = input(prompt).strip()
        if response in options:
            return response
        else:
            print("Invalid input. Please enter '0' or '1'.")

def get_3_numeric_option_input(prompt, options=['0', '1', '2']):
    while True:
        response = input(prompt).strip()
        if response in options:
            return response
        else:
            print("Invalid input. Please enter '0', '1', or '2'.")

def get_4_numeric_option_input(prompt, options=['0', '1', '2', '3']):
    while True:
        response = input(prompt).strip()
        if response in options:
            return response
        else:
            print("Invalid input. Please enter '0', '1', '2', or '3'.")
    
print("Insert customer data to see if they will churn or not")
print("Enter the following details:")
insert_gender = get_2_numeric_option_input("Gender (1 for Male, 0 for Female): ")
insert_senior_citizen = get_2_numeric_option_input("Senior Citizen (1 for Yes, 0 for No): ")
insert_partner = get_2_numeric_option_input("Partner (1 for Yes, 0 for No): ")
insert_dependents = get_2_numeric_option_input("Dependents (1 for Yes, 0 for No): ")
insert_tenure = input("Tenure (number of months the customer has been with the company): ")
insert_phone_service = get_2_numeric_option_input("Phone Service (1 for Yes, 0 for No): ")
insert_multiple_lines = get_3_numeric_option_input("Multiple Lines (1 for No phone service, 2 for Yes, 0 for No): ")
insert_internet_service = get_4_numeric_option_input("Internet Service (1 for No, 2 for DSL, 3 for Fiber optic, 0 for No): ")
insert_online_security = get_3_numeric_option_input("Online Security (1 for No internet service, 2 for Yes, 0 for No): ")
insert_online_backup = get_3_numeric_option_input("Online Backup (1 for No internet service, 2 for Yes, 0 for No): ")
insert_device_protection = get_3_numeric_option_input("Device Protection (1 for No internet service, 2 for Yes, 0 for No): ")
insert_tech_support = get_3_numeric_option_input("Tech Support (1 for No internet service, 2 for Yes, 0 for No): ")
insert_streaming_tv = get_3_numeric_option_input("Streaming TV (1 for No internet service, 2 for Yes, 0 for No): ")
insert_streaming_movies = get_3_numeric_option_input("Streaming Movies (1 for No internet service, 2 for Yes, 0 for No): ")
insert_contract = get_3_numeric_option_input("Contract (1 for Month-to-month, 2 for One year, 3 for Two year, 0 for No): ") 
insert_pap


