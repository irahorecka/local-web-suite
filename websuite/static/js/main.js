function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'static/settings.json', false);
    xobj.onreadystatechange = function() {
        if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
        }
    };
    xobj.send(null);
}

function loadSunCalcTimes(city_JSON) {
    return SunCalc.getTimes(new Date, city_JSON["lat"], city_JSON["lon"]);
}

function init() {
    loadJSON(function(response) {
        // Parse JSON string into object
        actualJSON = JSON.parse(response);
    });
    var toronto = actualJSON["location"]["toronto"];
    var torontoSunCalcTimes = loadSunCalcTimes(toronto);
    
    var currentDateTime = new Date();
    isDayTime = false;
    if (currentDateTime > torontoSunCalcTimes["sunrise"] && currentDateTime < torontoSunCalcTimes["sunset"]) {
        isDayTime = true;
    }
}

init();
