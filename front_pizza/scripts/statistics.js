/**
 * Fetchs de order detail and appends to the page
 * ****************************
 * Please change 'json/statistics.json' 
 * with your service endpoint below
 * ****************************
 */
fetch('http://127.0.0.1:8000/pizzeria/report')
    .then(response => response.json())
    .then(statistics => {
        let template = createStatisticsTemplate(statistics);
        $("#statistics").append(template);
    });

/**
 * Find the template tag and populate it with the data
 * @param statistics 
 */
function createStatisticsTemplate(statistics) {
    let template = $("#statistics-template")[0].innerHTML;
    return Mustache.render(template, statistics);
}