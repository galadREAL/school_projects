//? Here is the easier challenge's code:
/*
d3.csv('/data/data.csv')
  .then(rows => rows.map(row => ({
            x: [+row.poverty],
            y: [+row.healthcare],
            text: [row.abbr],
            type: 'scatter',
            mode: 'markers',
            marker: {
                size: 14,
                color: 'darkgreen',
            },
        })))
    .then(scatter_data => Plotly.newPlot('scatter', scatter_data, {}));
*/
//? Below is where I got to on attempting the bonus work - I got need to figure how to make
//? the case switcher iterate baseData's elements not just spit them out as literals.
//? Once that is conquered I'd just need to make each button do an onClick to return its
//? value into the case switcher function.

var rawCSV = 'data/data.csv';
//! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
// This inits arrays with the default values in them
function initEmpties() {
    last_y = ["row.healthcare"];
    last_x = ["row.poverty"];
    return last_y, last_x
}
//todo fix this like the "IexistJusttoCapture"
var last_y, last_x = initEmpties();

// This returns the [#] needed to get the last appended (most recent) value
function returnIndex_Y() {
    let lylen = +last_y.length;
    let lylen_i = (lylen - 1);
    return lylen_i
}

// This returns the [#] needed to get the last appended (most recent) value
function returnIndex_X() {
    let lxlen = +last_x.length;
    let lxlen_i = (lxlen - 1);
    return lylen_i, lxlen_i;
}

let lylen_i = returnIndex_Y();
let lxlen_i = returnIndex_X();

// The last (most recent) appended value is assigned into a variable
var yReturn = last_y[lylen_i];
var xReturn = last_x[lxlen_i];

// Case switches for which Dataset the user selects, returns the axes and text hover data.
//todo integrate this in with .onClicks for the buttons
function variationDelegator(variation) {
    if (variation === null) {
        console.warn("[!] Passed-in variation case was null!");
        alert("[!] Passed-in variation case was null!")
    } else {
        console.log("Passed-in variation case is valid, continuing... : ", variation);
        var txt_axis = "row.abbr";
        switch (variation) {
            case 'obese':
                //var y_axis = "row.obese";
                return ["row.obese", xReturn, txt_axis];
                break;
            case 'smokes':
                //var y_axis = "row.smokes";
                return ["row.smokes", xReturn, txt_axis];
                break;
            case 'healthcare':
                //var y_axis = "row.healthcare";
                return ["row.healthcare", xReturn, txt_axis];
                break;
            case 'poverty':
                //var x_axis = "row.poverty";
                return [yReturn, "row.poverty", txt_axis];
                break;
            case 'age':
                //var x_axis = "row.age";
                return [yReturn, "row.age", txt_axis];
                break;
            case 'income': ;
                //var x_axis = "row.income";
                return [yReturn, "row.income", txt_axis];
                break;
            default:
                return [yReturn, xReturn, txt_axis];

        };
    }
};

//*
var variation = "smokes"
//*

//variationDelegator(variation);

var IexistJusttoCapture = new Array();
IexistJusttoCapture = variationDelegator(variation);
y_axis = IexistJusttoCapture[0];
x_axis = IexistJusttoCapture[1];
txt_axis = IexistJusttoCapture[2];

// Appends the newly returned axes data to the arrays
function appendData() {
    last_y.push(y_axis);
    last_x.push(x_axis);
}

appendData();

// Storing the plotting data - hardcodes for elements that won't
// change, and vars for those that will.
var baseData = [{
    x: (("[+" + x_axis) + "]"),
    y: (("[+" + y_axis) + "]"),
    type: 'scatter',
    mode: 'markers+text',
    marker: {
        size: 22,
        color: 'lightblue'
    },
    text: (("[" + txt_axis) + "]"),
    textposition: 'center'
}];

var baseLayout = {
    xaxis: { title: x_axis },
    yaxis: { title: y_axis },
    showlegend: false
};

var baseConfig = {
    scrollZoom: true
};

//todo fix this - it isn't iterating and mapping actual data values like it should be
function iterationPlotter(baseData, baseLayout, baseConfig) {
    d3.csv(rawCSV)
        .then(rows => rows.map(row => ({
            x: baseData.x,
            y: baseData.y,
            type: baseData.type,
            mode: baseData.mode,
            marker: {
                size: baseData[0].size,
                color: baseData[0].color
            },
            text: baseData.text,
            textposition: baseData.textposition
        })))
        .then(pending_data => Plotly.newPlot(
            'scatter',
            pending_data,
            baseLayout,
            baseConfig
        ));
};


if (y_axis && x_axis != null) {
    //var last_y = y_axis;
    //var last_x = x_axis;
    iterationPlotter(baseData, baseLayout, baseConfig);
}
