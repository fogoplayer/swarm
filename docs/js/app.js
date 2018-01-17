/*
SWARM Code version 1.0
*/

//Code to run on Startup
//Register Service Worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker
        .register('./service-worker.js').then(function() { console.log('Service Worker registered'); });
}

//Set up location
if ("geolocation" in navigator) {
    navigator.geolocation.watchPosition(function(position) {
        updateLocation(position.coords.latitude, position.coords.longitude);
    });
}
else {
    alert("Please update your browser to one that supports geolocation, such as Google Chrome or Mozilla Firefox.")
}

//Make document.cookie readable as an object
if (document.cookie === "") {
    document.cookie = {};
}
else {
    var cookie = JSON.parse(document.cookie);
}

/*
Update onscreen instructions using data from the server
@param text - the String to be displayed at the top of the UI
@param icon - a String with the id of the instruction icon. Accepts arrow_back, arrow_forward, arrow_downward, and arrow_upward.
*/
function updateInstruction(text, icon) {
    document.getElementById("instructionText").innerHTML = text;
    document.getElementById("instructionIcon").innerHTML = icon;
}

/*
Update onscreen display of the user's current location
@param lat - device latitude
@param long - device longitude
*/
function updateLocation(lat, long) {
    document.getElementById("locationOutput").innerHTML = JSON.stringify(lat) + ", " + JSON.stringify(long);
    console.log(JSON.stringify(lat) + ", " + JSON.stringify(long));
}

/*
Change user settings
@param setting - the setting being updated
@param value   - the value being assigned to the setting
*/
function updateSettings(setting, value) {
    cookie[setting] = value;
    document.cookie = JSON.stringify(cookie);
}