/* populate_selector() receives the json output of names_dump() by hooking the "/names" route that
Flask is running. Then for each name in the json, using d3 the html is altere to turn each one into
an option for the user to choose from. */
function populate_selector() {
    var sample_selector = d3.select("#selDataset");
    d3.json("/names").then((dump_names) => {
        dump_names.forEach((name) => {
            sample_selector
                .append("option")
                .text(name)
                .property("value", name);
        });
    });
};

/* load_selection() executes both plots build commands as well as the metadata's text build
command for the user's selected saaple. */
function load_selection(sample) {
    build_pie(sample)
    build_bubbs(sample)
    build_meta(sample)
}

/* build_pie()  receives the json output of identities_dump() by hooking the "/samples" route that
Flask is running. Then the 3 objects are put into an array to be read by plotly to create a dynamic
Pie chart on the index.html */
function build_pie(sample) {
    var pie_route = "/samples/";
    var pie_selection = sample;
    var pie_query = pie_route.concat(pie_selection);
    d3.json(pie_query).then((identities) => {
        var pie_identities = [identities];
        var pie_data = [{
            values: pie_identities[0].sample_values,
            labels: pie_identities[0].otu_ids,
            type: "pie",
            title: "tbd PIE Chart Title",
            hoverinfo: pie_identities[0].otu_labels
        }];
        Plotly.newPlot("pie", pie_data, {});
    });
};

/* build_bubbs()  receives the json output of identities_dump() by hooking the "/samples" route that
Flask is running. Then the 3 objects are put into an array to be read by plotly to create a dynamic
Bubble chart on the index.html */
function build_bubbs(sample) {
    var bubbs_route = "/samples/";
    var bubbs_selection = sample;
    var bubbs_query = bubbs_route.concat(bubbs_selection);
    d3.json(bubbs_query).then((identities) => {
        var bubbs_identities = [identities];
        var bubbs_data = [{
            x: bubbs_identities[0].otu_ids,
            y: bubbs_identities[0].sample_values,
            text: bubbs_identities[0].otu_labels,
            mode: "markers",
            marker: {
                size: bubbs_identities[0].sample_values,
                color: bubbs_identities[0].otu_ids
            }
        }];
        Plotly.newPlot("bubbs", bubbs_data, {})
    });
};

/* build_meta() receives the json output of metadata_dump() by hooking the "/metadata" route that
Flask is running. If metadata exists, then it is cleared before each field of the json object is
iterated and appended as a new <p> of a new <div> within the #meta div on the index.html. */
function build_meta(sample) {
    var meta_route = "/metadata/";
    var meta_selection = sample;
    var meta_query = meta_route.concat(meta_selection);
    var testloc = d3.select("#meta");
    testloc.html("");
    d3.json(meta_query).then((metadata) => {
        var data = [metadata];
        console.log(data);
        data.forEach((field) => {
            var row = testloc.append("div");
            Object.entries(field).forEach(([key, value]) => {
                var cell = row.append("p");
                cell.text((key + ": ") + value);
            });
        });
    });
};


populate_selector();
