var weatherData = [
    {"city": "Boston", "forecast":[["66°", "47°", "clouds"], ["56°", "42°", "rain"], ["56°", "41°", "clouds"], ["61°", "43°", "sun"]]},
    {"city": "Chicago", "forecast":[["46°", "35°", "clouds"], ["48°", "33°", "sun"], ["57°", "34°", "clouds"], ["70°", "43°", "sun"]]},
    {"city": "Dallas", "forecast":[["64°", "47°", "sun"], ["66°", "41°", "sun"], ["81°", "50°", "sun"], ["85°", "54°", "sun"]]},
    {"city": "San Jose", "forecast":[["75°", "65°", "rain"], ["80°", "66°", "sun"], ["69°", "61°", "clouds"], ["78°", "70°", "sun"]]},
];

function loadReport(element) {
    alert("Loading " + element.innerText + " Weather Report...");
    changeForecast(element.innerText);
    shuffleCities(element);
    reorderCitiesList();
}

function shuffleCities(element) {
    var temp = document.querySelector(".city-name").innerText;
    document.querySelector(".city-name").innerText = element.innerText;
    element.innerText=temp;
}

function reorderCitiesList() {
    var viewing = document.querySelector(".city-name").innerText;
    var alphabetical = [];
    for (var i=0; i<weatherData.length; i++)
        if (weatherData[i].city != viewing)
            alphabetical.push(weatherData[i].city);
    document.querySelector("#city-1").innerText = alphabetical[0];
    document.querySelector("#city-2").innerText = alphabetical[1];
    document.querySelector("#city-3").innerText = alphabetical[2];
}

function changeForecast(city) {
    var changer = getWeatherForecast(city);
    var hiChanged = document.querySelectorAll(".hi");
    var loChanged = document.querySelectorAll(".lo");
    var images = document.querySelectorAll(".weather-image");
    var descriptions = document.querySelectorAll(".weather-desc");
    for (var i=0; i<hiChanged.length; i++) {
        if (document.querySelector("#selector").value == "Fahrenheit") {
            hiChanged[i].innerText = changer[i][0];
            loChanged[i].innerText = changer[i][1];
        } else {
            hiChanged[i].innerText = convertToC(changer[i][0]);
            loChanged[i].innerText = convertToC(changer[i][1]);
        }
        descriptions[i].innerText = "some " + changer[i][2];
        if (changer[i][2] == "sun")
            images[i].src="assets/some_sun.png";
        else if (changer[i][2] == "clouds")
            images[i].src="assets/some_clouds.png";
        else
            images[i].src="assets/some_rain.png";
    }
}

function getWeatherForecast(city) {
    for (var i=0; i<weatherData.length; i++) {
        if (city == weatherData[i].city)
            return weatherData[i].forecast;
    }
}

function chooseUnits(element) {
    var hiTemps = document.querySelectorAll(".hi");
    var loTemps = document.querySelectorAll(".lo");
    var city = document.querySelector(".city-name").innerText;
    if (element.value == 'Celcius')
        for (var i=0; i<hiTemps.length; i++) {
            hiTemps[i].innerText = convertToC(hiTemps[i].innerText);
            loTemps[i].innerText = convertToC(loTemps[i].innerText);
        }
    else
        for (var i=0; i<hiTemps.length; i++) 
            for (var j=0; j<weatherData.length; j++)
                if (city == weatherData[j].city) {
                    hiTemps[i].innerText = weatherData[j].forecast[i][0];
                    loTemps[i].innerText = weatherData[j].forecast[i][1];
                }
}

function convertToC(value) {
    return Math.round((parseInt(value.substring(0,2))-32)*(5/9))+"°";
}

function hideCookies(id) {
    var element = document.querySelector(id);
    element.remove();
}