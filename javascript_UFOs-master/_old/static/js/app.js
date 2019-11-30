//! Using the UFO dataset provided in the form of an array of JavaScript objects,
//! write code that appends a table to your web page and then adds new rows of
//! data for each UFO sighting.



/* This locks onto the div "tbody" as a global variable called "tbody". */
var tbody = d3.select("tbody");


var submitDefault = d3.select("#submitDefault");

submitDefault.on("click", function () {
    let rowCount = ufoTable.rows.length;
    if (rowCount >= 2) {
        location.reload();
    } else {
        d3.event.preventDefault();
    }
    /* Prevent the page from refreshing. */
    //d3.event.preventDefault();

    //("tbody#id tr").remove();

    //var new_tbody = document.createElement('tbody');
    //populate_with_new_rows(new_tbody);
    //old_tbody.parentNode.replaceChild(new_tbody, old_tbody)

    //* somewhat close but still way off
    //let rowlen = ufoTable.rows.length; while (--rowlen) ufoTable.deleteRow(rowlen);

    //document.getElementById('ufoTable').deleteRow(1,);

    //("#ufoTable tbody tr").remove();

    //var rowCount = ufoTable.rows.length; while(--rowCount) ufoTable.deleteRow(rowCount);


    /* This executes a for-loop over data.js' objects; it appends a new and blank row onto
    the html's existing table for each object it iterates. */
    data.forEach((UFOsighting) => {
    //todo Is this var decleration needed?
    var row0 = tbody.append("tr")
    /* This is a nested for-loop that executes over the current object's keys and
     values; it creates and appends a new cell onto the hteml's existing table with
     a casted string for each value it iterates. */
    Object.entries(UFOsighting).forEach(([key, value]) => {
        var cell = tbody.append("td");
        cell.text(value);
    });
});
})




//! Use a date form in your HTML document and write JavaScript code that will
//! listen for events and search through the date / time column to find rows
//! that match user input.


/* Select and assign the button's submit event as a variable called "filterSubmit". */
var submit = d3.select("#submit");

/* Define what happens when that button is clicked && the user's date is submitted. */
submit.on("click", function () {
    //let rowCount = ufoTable.rows.length;
    //if (rowCount >= 2) {
    //    location.reload();
    //} else {
    //    d3.event.preventDefault();
    //}

    // 1)
    // Clear any existing declerations of the custom class.


    //* 2)
    //* Select, then assign to an alias the value of the user's submitted date element.
    //* Filter, assign to an alias, [[[and return]]] all objects matching the above.

    /* Prevent the page from refreshing. */
    //d3.event.preventDefault();

    /* Select the input element and get the raw HTML node. */
    var inputElement = d3.select("#datetime");

    /* Get the value property of the input element. */
    var rawInputValue = inputElement.property("value");

    /* Remove the leading 0s to match the dataset's datetime format */
    var inputDatetime = rawInputValue.replace(/-0+/g, '-');


    //todo:::   add a != var definition also
    var test = inputDatetime.split("-");
    //var test = inputDatetime.split(/-(?=&#?[a-zA-Z0-9]+;)/g);
    var splitTest = test.reverse();
    var joinTest = new Array(splitTest[1], splitTest[0], splitTest[2]);
    var joinTest2 = joinTest.join("/");
    //todo:::   need to make this a d3 selection not a var?
    var filteredRaw = data.filter(sighting => sighting.datetime === joinTest2);




    // 3)
    // Assign the custom class ".highlight" to each object in var filteredData.

    //var filteredData = d3.select(filteredRaw);
    //var tableobj = d3.selectAll("td");
//
    //filteredRaw.forEach((obj) => {
    //    if (obj.datetime === tableobj.Date) {
    //        //d3.select(this).classed("highlight", true);
    //        console.log("yuhh")
    //    }
    //})

    //filteredRaw.style("class", "highlight")

    //data.forEach((UFOsighting) => {
    //Object.entries(UFOsighting).forEach(([key, value]) => {
    //    if
    //});


    //* 3)
    //* In lieu of the above way...switching tactics to a more rudimentary attempt.
    //* Creating the table either from the filteredRaw or the default/all data.

    console.log(filteredRaw);

    //("tbody#id tr").remove();

    //var new_tbody = document.createElement('tbody');
    //populate_with_new_rows(new_tbody);
    //old_tbody.parentNode.replaceChild(new_tbody, old_tbody)

    //document.getElementById('tbody').innerHTML = '';

    //("tbody #tr").remove();

    //* somewhat close but still way off
    //let rowlen = ufoTable.rows.length; while (--rowlen) ufoTable.deleteRow(rowlen);



    filteredRaw.forEach((UFOsighting) => {
    //todo Is this var decleration needed?
    var row1 = tbody.append("tr")
    /* This is a nested for-loop that executes over the current object's keys and
     values; it creates and appends a new cell onto the hteml's existing table with
     a casted string for each value it iterates. */
    Object.entries(UFOsighting).forEach(([key, value]) => {
        var cell = tbody.append("td");
        cell.text(value);
    });
});


});




//! Using multiple `input` tags and/or select dropdowns, write JavaScript code
//! so the user can to set multiple filters and search for UFO sightings using
//! the following criteria based on the table columns:
//!  1. `date/time`
//!  2. `city`
//!  3. `state`
//!  4. `country`
//!  5. `shape`



    //todo:::   create in the style.css then assign a ".lowlight" custom class
    //todo:::   for the rest of the objects not matched.

        //filteredData.forEach((filteredSighting) => {
    //})








////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
//todo in the refactor~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

//todo:::   1)
//todo:::   Create a new pkg containing all of the functions that are deeply
//todo:::   stacked here as a sort of main. Modify the functions to return output
//todo:::   that needs to be fed into other functions in order to operate.


//todo:::   2)
//todo:::   Spruce up the  a e s t h e t i c s  with some bootstrapped CSS.


//todo:::   3)
//todo:::   Get rid of any/all hardcodes possible (min and max date ranges, etc)


//todo:::   4)
//todo:::   Cull or redefine any attributes/declerations that are not ES6 compliant.