/*
SWARM Code version 1.0
*/

//Code to run on Startup
//Register Service Worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker
        .register('./service-worker.js').then(function() {
            console.log('Service Worker registered');
        });
}

/*//Set up location
if ("geolocation" in navigator) {
    navigator.geolocation.watchPosition(function(position) {
        updateLocation(position.coords.latitude, position.coords.longitude);
    }, function() {}, geo_options);
}
else {
    alert("Please update your browser to one that supports geolocation, such as Google Chrome or Mozilla Firefox.");
}
var geo_options = {
    enableHighAccuracy: false,
    maximumAge: 10,
};*/

setInterval(getLocation, 1000)
function getLocation(){
    navigator.geolocation.getCurrentPosition(function(position){
        updateLocation(position.coords.latitude, position.coords.longitude);
    });
}

//Make document.cookie readable as an object
if (document.cookie === "") {
    document.cookie = JSON.stringify({
        spokenFeedBackOn: true
    });
}
var cookie = JSON.parse(document.cookie);

//Code to run once content is loaded
document.addEventListener("DOMContentLoaded", function() {
    if (document.title == "Overview" && !(cookie.orientation && cookie.color && cookie.type)) {
        history.pushState({}, document.title, document.location.pathname.substring(1));
        document.location = "../settings.html";
    }

    //if overview page, make get request
    if (document.title == "Overview") {
        $.getJSON('https://cap-swarm.herokuapp.com', {
            carColor: cookie.color,
            carType: cookie.type,
            carOrientation: cookie.orientation
        }, function(data) {
            console.log(data);
            updateSetting(null, "id", data.id);
            //Fake data
            data.instructions = ["Back up and go left", "Go forward"];
            data.instructions.forEach(function(instruction) {
                var li = document.createElement("li");
                li.append(instruction);
                document.getElementById("overviewList").append(li);
            });
        });
    }

    //If on a page with dropdowns, dynamically load saved responses
    if (document.getElementsByClassName("dropdown-button")) {
        //Create an array with all dropdown buttons
        var array = document.getElementsByClassName("dropdown-button");
        //Loop through elements and change their innerHTMLS
        Array.from(array).forEach(function(element) {
            if (cookie[element.dataset.activates]) {
                updateDropdown(element, cookie[element.dataset.activates]);
            }
        });
    }
    
    //If main page, set up volume toggle button state
    if (document.getElementById("voiceToggle") && !cookie.spokenFeedBackOn){
        cookie.spokenFeedBackOn = true;
        toggleSpokenFeedback();
    }
});
/*---------------------------------------Functions---------------------------------------*/
/*
Update onscreen instructions using data from the server
@param text - the String to be displayed at the top of the UI
@param icon - a String with the id of the instruction icon. Accepts arrow_back, arrow_forward, arrow_downward, and arrow_upward.
*/
function updateInstruction(text, icon) {
    responsiveVoice.cancel();
    document.getElementById("spinner").style.display = "none";
    document.getElementById("instructionText").innerHTML = text;
    document.getElementById("instructionIcon").setAttribute("src", "img/" + icon + ".png");
    if (cookie.spokenFeedBackOn) {
        responsiveVoice.speak(text);
    }
}

/*
Update onscreen display of the user's current location
@param lat - device latitude
@param long - device longitude
*/
function updateLocation(lat, long) {
    document.getElementById("locationOutput").innerHTML = JSON.stringify(lat) + ", " + JSON.stringify(long);
    console.log(JSON.stringify(lat) + ", " + JSON.stringify(long));
    $.getJSON('https://cap-swarm.herokuapp.com', {
            id: cookie.id,
            lat: lat,
            long: long
        },
        function(data) {
            //fake data
            data = fakeData();
            console.log(data);
            if(data.exists){
                console.log(data);
                updateInstruction(data.text, data.icon);
            }
        });
}
/*
Generates fake data for app to use
@return Returns a data object reflective of potential server responses
*/
function fakeData(){
    let ran = Math.random()
    if (ran < .90){
        data = { exists: false, text: "Turn left", icon: "left"}
    }else if (ran < .95){
        data = { exists: true, text: "Turn right", icon: "right" }
    }else{
        data = { exists: true, text: "Turn left", icon: "left" }
    }
    return data
}

/*
Change user setting
@param elem - the element being clicked
@param setting - the setting being updated
@param value   - the value being assigned to the setting
*/
function updateSetting(elem, setting, value) {
    cookie[setting] = value;
    document.cookie = JSON.stringify(cookie);
    //Go up three levels in the DOM to the card, then go to the second element (the dropdown) and change the innerHTML to reflect that
    if (elem) {
        updateDropdown(elem.parentElement.parentElement.parentElement.children[1], value);
    }
    console.log(setting + " has been set to " + value);
}

/*
Change dopdown label to reflect save state
@param elem - the element to update
@param value - the new value for the element
*/
function updateDropdown(elem, value) {
    elem.innerHTML = value + '<i class="material-icons right">arrow_drop_down</i>';
}

/*
Toggle spoken feedback
*/
function toggleSpokenFeedback() {
    let val = cookie.spokenFeedBackOn ? (!cookie.spokenFeedBackOn

    ) : true;
    if (cookie.spokenFeedBackOn === false) {
        updateSetting(null, "spokenFeedBackOn", true);
        document.getElementById("voiceToggle").classList.remove("lighten-3");
        document.getElementById("voiceToggle").classList.add("accent-2");
    }
    else {
        updateSetting(null, "spokenFeedBackOn", false);
        document.getElementById("voiceToggle").classList.remove("accent-2");
        document.getElementById("voiceToggle").classList.add("lighten-3");
    }
}