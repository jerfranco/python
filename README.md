# Overview

For my fourth sprint, I decided to work on a networking programming app that will allow the user select and display their weather information according to their ip address. Networking is a very important aspect in programming. Everything that we use requires some kind of network. When connected to a network or a port, there are a lot of information that you can hold and store. It requires the server and the client side to communicate to allow the user to gather the correct information.

This python networking program, has four different options to choose from. The options can display the users ip address, which state they are located at, display the weather information based off of their location, and their city and state. This is my first time using apis and requests and I love it.

The software that I used is VSCode. It's one of the most common programming software where the programmer can program any language. 


[Software Demo Video](https://clipchamp.com/watch/cJzs0r2mfDX)

# Network Communication

The architecture that I used was a peer-to-peer. The program will grab the user's ip address and it will send that ip address to the apis in the program. When ran, it will then display the correct information based off of their ip address that the user sent over.

The two apis that I used is a weather api and a ipstack api that will get their location based off of their ip address. The program will get the users ip address and it will send that information to the ipstack api to get the region of the user. After it gets the region, it will send that region to the weather api and it will gather the correct information from the region and display the information to that user.

# Development Environment

One of the tools that I used was a request library. The request library allows me to get and request data from the api. I first had to install requests to my machine to make it work. I also used apis to get the correct information based off of their network ip address.


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [ipstack](https://ipstack.com/)
* [WeatherAPI](https://www.weatherapi.com/)
* [PythonAPI](https://www.dataquest.io/blog/python-api-tutorial/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* One of the things that I want to improve in my program is to allow users the option to choose what type of weather information the users want to see. 