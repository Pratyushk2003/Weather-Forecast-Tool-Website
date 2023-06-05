# Weather-Forecast-Tool-Website
Q. Create a command-line tool that accepts a city's name and returns the current weather forecast.
Leverage OpenWeatherMap API to fetch weather data and parse it using Python. 
Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

# Now we use GitHub Copilot for API usage

When you write the comment “Send GET request to OpenWeatherMap API endpoint” 
then GitHub Copilot will give you the suggestion of the code according to your comment requirement

# Using GitHub Copilot for data parsing and error handling

When you give the comment “Parse the JSON response” it will give you the suggestion 

	weather_data = json.loads(response.text)
	
And for error handling it will suggest you:

	except (json.JSONDecodeError, KeyError) as e:
		print("Error occurred while parsing weather data:", e)
		return 
          
	  
# HOW TO RUN THE CODE
In the terminal just run the command:

    py app.py
        OR
    python app.py 

#Result
![image](https://github.com/Pratyushk2003/Weather-Forecast-Tool-Website/assets/77561223/f958d085-6d26-42f9-8309-6e15d6ff0f60)

![image](https://github.com/Pratyushk2003/Weather-Forecast-Tool-Website/assets/77561223/45761dc4-b039-4ada-88aa-f65f309955c5)
