//* tbody holds a d3 selection of the page's first (and only) tbody html tag.
const tbody = d3.select("tbody");



//* The both listen for a click event on their buttons to then prevent the
//* default action associate with the click (a page reload in this case).
document.getElementById("submitFilter").addEventListener("click", function (event) {
    event.preventDefault()
});

document.getElementById("submitDefault").addEventListener("click", function (event) {
    event.preventDefault()
});



//* defaultClick() handles the click events for the default button. It first
//* ensures the tbody tag's html is null, then iterrates each object in data.js
//* appending a new tr tag to tbody. Lastly it goes over each attribute of the
//* object it is iterrating to append its contents into a cell td tag in the tr.
function defaultClick() {
    tbody.html("")
    data.forEach((i) => {
        tbody.append("tr");
        Object.entries(i).forEach(([key, value]) => {
            let cell = tbody.append("td");
            cell.text(value);
        });
    });
};



//* flipDatetime() recieves a datetime from filterClick() which is then split by
//* hyphens. The array's items are then reversed before being put into a new
//* array in the order of 1, 0, 2. The new array is joined with forward slashes
//* so that it will match up on the dataset before being returned back out.
function flipDatetime(OG_dt) {
    let splitHyphens = OG_dt.split("-");
    let reverseObjects = splitHyphens.reverse();
    let initArray = new Array(reverseObjects[1], reverseObjects[0], reverseObjects[2]);
    let cleanDateTime = initArray.join("/");
    return cleanDateTime
}



//* isEmpty() returns a bool of the passed-in object.
function isEmpty(obj) {
    return Object.keys(obj).length === 0;
};



//* alertNoMatch() alerts the user in a pop-up window that no matches were found
//* for their search parametres.
function alertNoMatch() {
    target = alert("[!] No matching entries for current filters.")
};



//* All of the below pivot functions check to see if any of the selectors still have
//* a default value (the user didn't want to use it). If they do, they are treated
//* as a wildcard and return all objects from the dataset. If they do have a value,
//* then that value is used to filter the dataset into a selection.
function pivotDatetime(cleanDateTime) {
    if (cleanDateTime == "//") {
        var desiredEntriesDay = data.filter(sighting => sighting.keys == 7);
    } else {
        var desiredEntriesDay = data.filter(sighting => sighting.datetime === cleanDateTime);
        if (isEmpty(desiredEntriesDay)) {
            alertNoMatch()
        } else {
        }
    }
    return desiredEntriesDay
}

function pivotCity(desiredEntriesDay, uCityInput) {
    if (uCityInput == "Select a City") {
        var desiredEntriesCity = data.filter(sighting => sighting.keys == 7);
    } else {
        var desiredEntriesCity = data.filter(sighting => sighting.city === uCityInput);
        if (isEmpty(desiredEntriesCity)) {
            alertNoMatch()
        } else {
        }
    }
    return desiredEntriesCity
}

function pivotState(desiredEntriesCity, uStateInput) {
    if (uStateInput == "Select a State") {
        var desiredEntriesState = data.filter(sighting => sighting.keys == 7);
    } else {
        var desiredEntriesState = data.filter(sighting => sighting.state === uStateInput);
        if(isEmpty(desiredEntriesState)) {
            alertNoMatch()
        } else {
        }
    }
    return desiredEntriesState
}

function pivotCountry(desiredEntriesState, uCountryInput) {
    if (uCountryInput == "Select a Country") {
        var desiredEntriesCountry = data.filter(sighting => sighting.keys == 7);
    } else {
        var desiredEntriesCountry = data.filter(sighting => sighting.country === uCountryInput);
        if(isEmpty(desiredEntriesCountry)) {
            alertNoMatch()
        } else {
        }
    }
    return desiredEntriesCountry
}

function pivotShape(desiredEntriesCountry, uShapeInput) {
    if (uShapeInput == "Select a Shape") {
        var desiredEntriesShape = data.filter(sighting => sighting.keys == 7);
    } else {
        var desiredEntriesShape = data.filter(sighting => sighting.shape === uShapeInput);
        if(isEmpty(desiredEntriesShape)) {
            alertNoMatch()
        } else {
        }
    }
    return desiredEntriesShape
}



//* populateFiltered2() receives the user's filters' input from filterClick2(), then
//* looks for all objects that match the each attribute. If none are found (isEmpty()),
//* an alert is displayed to the user.
function populateFiltered2(cleanDateTime, uCityInput, uStateInput, uCountryInput, uShapeInput) {
    let desiredEntriesDay = pivotDatetime(cleanDateTime);

    let desiredEntriesCity = pivotCity(desiredEntriesDay, uCityInput);

    let desiredEntriesState = pivotState(desiredEntriesCity, uStateInput);

    let desiredEntriesCountry = pivotCountry(desiredEntriesState, uCountryInput);

    let desiredEntriesShape = pivotShape(desiredEntriesCountry, uShapeInput);

    //* If the end has been reached (valid filter results achieved), a new var is declared
    //* containing the last guantlet's remaining sighting objects.
    var matchedEntries = desiredEntriesShape;

    //* Each of the objects in the above declared array are iterrated through, and a new
    //* tr is appended to the tbody for each one. Next each attribute of the object is
    //* iterrated and appended into a new cell td within the new tr.
    matchedEntries.forEach((sighting) => {
        tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            let cell = tbody.append("td");
            cell.text(value);
        });
    });
};



//* filterClick2() handles the click events for the custom filters button. It first
//* ensures the tbody tag's html is null, then selects the id of the form. Next
//* the value is selected from the properties of each filter category. After the datetime
//* is cleaned up, all of the values are then sent into populateFiltered2().
function filterClick2() {
    tbody.html("");

    let uDatetime = d3.select("#datetime");
    let rawDatetime = uDatetime.property("value");
    let filterInput = rawDatetime.replace(/-0+/g, '-');
    cleanDateTime = flipDatetime(filterInput);

    let uCity = d3.select("#city");
    let uCityInput = uCity.property("value");

    let uState = d3.select("#state");
    let uStateInput = uState.property("value");

    let uCountry = d3.select("#country");
    let uCountryInput = uCountry.property("value");

    let uShape = d3.select("#shape");
    let uShapeInput = uShape.property("value");

    populateFiltered2(cleanDateTime, uCityInput, uStateInput, uCountryInput, uShapeInput);
};



//* titleCase() takes a string and returns it with every 1st letter capitalized.
function titleCase(str) {
  str = str.toLowerCase().split(' ');
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
  }
  return str.join(' ');
}
titleCase("I'm a little tea pot");



//* populateSelectors() gathers up all objects that contain all 7 attributes (no incompletes).
//* Next the IDs for each of the 4 selector filters are selected into variables. Empty
//* lists are declared and initialized for recieving data from an immediate for-loop run
//* on the raw entries list of objects.
//* Each entry object's attributes are iterrated, if it already exists in the new list
//* it is skipped - otherwise it is appended. Once complete, the lists are sorted into
//* Alphabetical order. They then are iterrated through a for-loop and appended to the
//* html selected IDs as new option tags. The display versions are altered to be titlecase
//* and Uppercase where appropriate.
function populateSelectors() {
    var entries = data.filter(sighting => sighting.keys = 7);

    var selectorC = d3.select("#city");
    var selectorS = d3.select("#state");
    var selectorCC = d3.select("#country");
    var selectorSS = d3.select("#shape");

    var cList = []
    var sList = []
    var ccList = []
    var ssList = []

    entries.forEach((entry) => {
        let city = entry.city;
        if (cList.includes(city)) {
        } else {
            cList.push(city);
        }

        let staat = entry.state;
        if (sList.includes(staat)) {
        } else {
            sList.push(staat);
        }

        let country = entry.country;
        if (ccList.includes(country)) {
        } else {
            ccList.push(country);
        }

        let shape = entry.shape;
        if (ssList.includes(shape)) {
        } else {
            ssList.push(shape);
        }
    });



    cList.sort();
    sList.sort();
    ccList.sort();
    ssList.sort();

    cList.forEach((city) => {
        selectorC
            .append("option")
            .text(titleCase(city))
            .property("value", city)
    });

    sList.forEach((state) => {
        selectorS
            .append("option")
            .text(state.toUpperCase())
            .property("value", state)
    });

    ccList.forEach((country) => {
        selectorCC
            .append("option")
            .text(country.toUpperCase())
            .property("value", country)
    });

    ssList.forEach((shape) => {
        selectorSS
            .append("option")
            .text(titleCase(shape))
            .property("value", shape)
    });
};

populateSelectors();