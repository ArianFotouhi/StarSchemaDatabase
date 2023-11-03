import requests
from input.input_data import ( lounge_data, tx_data,
                        country_data, event_data, amenity_data,
                        airport_data)
from input.input_data import data_csv_reader



#authorization
url = 'http://127.0.0.1:5000/'

# User credentials for logging in
username = 'user1'
password = 'password1'

# Login to obtain a JWT token
login_data = {
    'username': username,
    'password': password
}

login_response = requests.post(f'{url}/login', json=login_data)

if login_response.status_code == 200:
    token = login_response.json()['token']
    print('Login successful. Token obtained')
    # Set the Authorization header with the JWT token
    headers = {'Authorization': token}



    ## Read data
    response = requests.get(f'{url}/get_table/User', headers=headers)
    # Read columns
    # response = requests.get(f'{url}/get_columns/User', headers=headers)
    
    #Write data
    # user_data = data_csv_reader(file_name='input/input.xlsx')
    # for record in user_data:
    #     response = requests.post(f'{url}/upload/user', data=record, headers=headers)


    if response.status_code == 200:
        print('Successful Request:')
        for i in response.json()['data']:
            print(i)

    else:
        print('Request Failed:')
        print(response.status_code, response.text)
else:
    print('Login failed:')
    print(login_response.status_code, login_response.text)





# url= 'https://iegapp.pythonanywhere.com/geo/'

# url = 'http://127.0.0.1:5000/upload/user'
# payload = user_data

# url = 'http://127.0.0.1:5000/upload/lounge'
# payload = lounge_data

# url = 'http://127.0.0.1:5000/upload/transaction'
# payload = tx_data

# url = 'http://127.0.0.1:5000/upload/country'
# payload = country_data

# url = 'http://127.0.0.1:5000/upload/event'
# payload = event_data

# url = 'http://127.0.0.1:5000/upload/amenity'
# payload = amenity_data

# url = 'http://127.0.0.1:5000/upload/airport'
# payload = airport_data

# response = requests.post(url, data=payload)



# url = 'http://127.0.0.1:5000/get_table/User'
# response = requests.get(url)

# print(response.json())