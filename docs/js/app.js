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
        let data = {
            instructions:["Go fast", "Turn left"],
        }
        data.instructions.forEach(function(instruction) {
            var li = document.createElement("li");
            var h = document.createElement("h5");
            h.append(instruction);
            li.append(h);
            //li.append(instruction)
            document.getElementById("overviewList").append(li);
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
    
    if(document.title == "SWARM"){
        //Set up location
        setInterval(function(){
            console.log("Hello")
            updateLocation(42.3461949, 83.4919403);
        }, 5000);
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
    let data = fakeData();
    console.log(data);
    updateInstruction(data.text, data.icon);
}
/*
Generates fake data for app to use
@return Returns a data object reflective of potential server responses
*/
function fakeData(){
    let ran = Math.random();
    let data;
    if (ran < .2){
        data = { exists: false, text: "Wait please", icon: "left"};
    }else if (ran < .4){
        data = { exists: true, text: "Turn right after the green sedan", icon: "right" };
    }else if (ran < .6){
        data = { exists: true, text: "Turn left after the blue convertible", icon: "right" };
    }else if (ran < .8){
        data = { exists: true, text: "Turn right at the end of the lane", icon: "right" };
    }else{
        data = { exists: true, text: "Turn left after the red SUV", icon: "left" };
    }
    return data;
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
        responsiveVoice.speak("");
        document.getElementById("voiceToggle").classList.remove("lighten-3");
        document.getElementById("voiceToggle").classList.add("accent-2");
    }
    else {
        updateSetting(null, "spokenFeedBackOn", false);
        document.getElementById("voiceToggle").classList.remove("accent-2");
        document.getElementById("voiceToggle").classList.add("lighten-3");
    }
}
