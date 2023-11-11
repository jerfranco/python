import requests
# Weather key to access the weather api
weather_api_key = '64b99187a29f49b086f171255231011'
ip_address = requests.get('https://api64.ipify.org?format=json').json()['ip']
#Menu options
def display_menu():
    print("Menu:")
    print("1. See your ip address")
    print("2. State location")
    print("3. Display the weather information")
    print("4. Display city and state")
    print("5. Exit")

#print out the users ip address
def option1():
    print(f"Your public IP address: {ip_address}")

#prints out the usrs state location
def option2():
    
    state_location = get_state_location(ip_address, ipstack_api_key)

    if state_location:
        print(f"State location based on IP address: {state_location}")
    else:
        print("Unable to retrieve state location.")

# Based off of the usrs state location, it will gather the weather information from the weather api
def option3():
    state_location = get_state_location(ip_address, ipstack_api_key)

    if state_location:
        weather_url = 'http://api.weatherapi.com/v1/current.json'
        weather_params = {'key': weather_api_key, 'q': state_location}
        weather_response = requests.get(weather_url, params=weather_params)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()

            # Displays the location, temperature and humidity
            location = weather_data['location']['name']
            temperature_f = weather_data['current']['temp_f']
            humidity = weather_data['current']['humidity']

            print(f"Location: {location}")
            print(f"Temperature (F): {temperature_f}")
            print(f"Humidity: {humidity}")
        else:
            print(f"Weather API Error: {weather_response.status_code}, {weather_response.text}")
    else:
        print("Unable to retrieve state location.")

# Displays the users city and state
def option4():
    state_location = get_state_location(ip_address, ipstack_api_key)

    if state_location:
        weather_url = 'http://api.weatherapi.com/v1/current.json'
        weather_params = {'key': weather_api_key, 'q': state_location}
        weather_response = requests.get(weather_url, params=weather_params)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()

            # Displays the city and state
            region = weather_data['location']['region']
            location = weather_data['location']['name']

            print(f"You are located in {location}, {region}")
        else:
            print(f"Weather API Error: {weather_response.status_code}, {weather_response.text}")
    else:
        print("Unable to retrieve state location.")


# The function to get the state information based off of the ip address
def get_state_location(ip_address, api_key):
    url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        state = data.get('region_name')
        return state
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

ipstack_api_key = '4d0c3ea2ad15ab0ef71ed16113c4ed34'


# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        option4()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
