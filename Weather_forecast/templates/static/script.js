const form = document.getElementById('weather-form');
    const locationElement = document.querySelector('.location');
    const temperatureElement = document.querySelector('.temperature');
    const humidityValueElement = document.querySelector('.humidity-value');
    const windspeedValueElement = document.querySelector('.windspeed-value');
    const descriptionElement = document.querySelector('.description');
    const iconElement = document.querySelector('.icon');
    const humidityIconElement = document.querySelector('.humidity-icon');
    const windIconElement = document.querySelector('.wind-icon');
    const weatherCard = document.querySelector('.weather-card');

    // Get the current time in hours
    const currentTime = new Date().getHours();
    const containerElement = document.querySelector('.container');
    const headingElement = document.querySelector('h1');
    // Check if it's daytime or nighttime based on the current time
    if (currentTime >= 6 && currentTime < 18) {
    // It's daytime, so set the background image to a day image
    containerElement.style.backgroundImage = "url('static/day.jpeg')"; // Example: URL of a day image
    headingElement.style.color = "black";
    } else {
    // It's nighttime, so set the background image to a night image
    containerElement.style.backgroundImage = "url('static/night.jpg')"; // Example: URL of a night image
    headingElement.style.color = "white";
    }
containerElement.style.backgroundSize = "cover";
containerElement.style.backgroundRepeat = "no-repeat";
containerElement.style.backgroundPosition = "center";
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const cityInput = document.getElementById('city-input').value;

      fetch(`/weather?city=${cityInput}`)
        .then(response => response.json())
        .then(data => {
          locationElement.textContent = data.location;
          const temperatureInCelsius = Math.round(data.temperature - 273.15);
          temperatureElement.textContent = temperatureInCelsius + '°C';
          humidityValueElement.textContent = data.humidity;
          windspeedValueElement.textContent = data.windspeed;
          descriptionElement.textContent = data.description;
          iconElement.src = data.icon;
          weatherCard.classList.add('animate-fade-in');
          weatherCard.style.display = 'block';
          const wind = parseInt(data.windspeed);
          windIconElement.src = "/static/wind.jpg";
          // Set humidity icon based on the humidity value
          const humidity = parseInt(data.humidity);
          if (humidity <= 30) {
            humidityIconElement.src = "/static/low.jpeg";
          } else if (humidity > 30 && humidity <= 70) {
            humidityIconElement.src = "/static/humidity.jpeg";
          } else {
            humidityIconElement.src = "/static/high.jpeg";
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });