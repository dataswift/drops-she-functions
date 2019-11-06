<script src="styles/prosilver/template/amcharts/amcharts.js" type="text/javascript"></script>
<script src="styles/prosilver/template//amcharts/serial.js" type="text/javascript"></script>


<h1> BusyTime </h1> <HR>

<h2> This is a demo page of a new SHE function: BusyTime.</h2> 

<p> username: testing</p>

The SHE function retrieves the Google Calendar meetings from a HAT account and produce an overall analysis and daily figures. The following chart depicts the history. </p>

<p> The account used here is a testing account which is only used for development and testing. 
The chart is not included in the SHE function. 
The SHE function is still under approval and integration process.
</p>

<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://testing.hubat.net/users/access_token",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Accept: application/json",
    "password: labai-geras-slaptazodis",
    "username: testing"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

//echo "<HR> <p>Data from HAT: sentiments </p>";

if ($err) {
//  echo "cURL Error #:" . $err;
} else {
//  echo $response;
}

$r = json_decode($response);

//var_dump($r);


$accessToken = $r->{'accessToken'};

//echo $accessToken;

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://testing.hubat.net/api/v2.6/data/calendar/google/events",
  //CURLOPT_URL => "https://testing.hubat.net/api/v2.6/data/she/insights/emotions",
  //CURLOPT_URL => "https://testing.hubat.net/api/v2/data/twitter/tweets",
  //CURLOPT_URL => "https://testing.hubat.net/api/v2/data/hat/locations",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Content-Type: application/json",
    "X-Auth-Token: $accessToken"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
//  echo $response;
//  echo "<HR>\n";
}



// connect to SHE Lambda function

$lambda_url = "https://k0vj0mk1o9.execute-api.ap-southeast-1.amazonaws.com/dev/busy-time/1.0.0";


$ch = curl_init($lambda_url);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, $response);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json',
    'Content-Length: ' . strlen($response))
);

$result = curl_exec($ch);

echo "<HR><h2> Busy Time - Analysis</h2><BR>\n";
//echo $result;


$j = json_decode($result, true);
//var_dump($j);
$j = $j[0];
$summary = $j['data'][0]['summary'];
$data = $j['data'][0]['data'];

$totalEvents = $summary['totalEvents'];
$totalEventHours = round($summary['totalEventHours'], 1);
$totalFulldayEvents = $summary['totalFulldayEvents'];
$totalDaytimeEvents = $summary['totalDaytimeEvents'];
$totalDaytimeEventHours = round($summary['totalDaytimeEventHours'], 1);
$totalEveningEvents = $summary['totalEveningEvents'];
$totalEveningEventHours = round($summary['totalEveningEventHours'], 1);
$totalShortEvents = $summary['totalShortEvents'];
$totalShortEventHours = round($summary['totalShortEventHours'], 1);
$totalMediumEvents = $summary['totalMediumEvents'];
$totalMediumEventHours = round($summary['totalMediumEventHours'], 1);
$totalLongEvents = $summary['totalLongEvents'];
$totalLongEventHours = round($summary['totalLongEventHours'], 1);
$totalWeekdayEvents = $summary['totalWeekdayEvents'];
$totalWeekdayEventHours = round($summary['totalWeekdayEventHours'], 1);
$totalWeekendEvents = $summary['totalWeekendEvents'];
$totalWeekendEventHours = round($summary['totalWeekendEventHours'], 1);
$percentBusyDays = round($summary['percentBusyDays'],1);
$percentBusyDaytime = round($summary['percentBusyDaytime'], 1);
$percentBusyEvening = round($summary['percentBusyEvening'], 1);
$startDate = $summary['startDate'];
$endDate = $summary['endDate'];
$totalDays = $summary['totalDays'];

echo "<h3> Analysis period: $startDate ~ $endDate, $totalDays days in total </h3>";
echo "<h3> Event number: $totalEvents , $totalEventHours in hours </h3>";
echo "<h4> Busy day percentage: $percentBusyDays%</h4> ";
echo "<BR>";
echo "<h4> Busy in daytime percentage: $percentBusyDaytime% </h4>";
echo "<h4> Busy in evening percentage: $percentBusyEvening%</h4> <BR>";
echo "<BR>";

echo "<h4> Daytime event number: $totalDaytimeEvents , $totalDaytimeEventHours in hours </h4>";
echo "<h4> Evening event number: $totalEveningEvents , $totalEveningEventHours in hours </h4>";
echo "<BR>";

echo "<h4> Short event number: $totalShortEvents , $totalShortEventHours in hours </h4>";
echo "<h4> Medium event number: $totalMediumEvents , $totalMediumEventHours in hours </h4>";
echo "<h4> Long event number: $totalLongEvents , $totalLongEventHours in hours </h4>";
echo "<BR>";


echo "<h4> Weekday event number: $totalWeekdayEvents , $totalWeekdayEventHours in hours </h4>";
echo "<h4> Weekend event number: $totalWeekendEvents , $totalWeekendEventHours in hours </h4>";


$figures = array();

foreach ($data as $record){
	$d = date('Y-m-d', strtotime($record['data']['date']));
        $figures[$d] = $record['data']['hours'];
}

//var_dump($figures);


ksort($figures);

?>
<script type="text/javascript" language="JavaScript">
var chartData = [

<?php
foreach ($figures as $day=>$v) {
	echo "{\"date\":\"" . $day . "\" ";

	echo ",\"hours\":" . $v;

	echo "}, ";
}
?>

];



// use ISO 8601 date format
//var chartData = [{"date":"2018-07-16","value":10000,"TAIEX":10817},{"date":"2018-07-17","TAIEX":10779},{"date":"2018-07-28","value":9744,"TAIEX":10842}];


AmCharts.ready(function () {
              // SERIAL CHART
               chart = new AmCharts.AmSerialChart();

               chart.dataProvider = chartData;
               chart.categoryField = "date";

               // listen for "dataUpdated" event (fired when chart is inited) and call zoomChart method when it happens
               chart.addListener("dataUpdated", zoomChart);

               chart.synchronizeGrid = true; // this makes all axes grid to be at the same intervals
               chart.mouseWheelZoomEnabled = true;

               // AXES
               // category
               var categoryAxis = chart.categoryAxis;
               categoryAxis.parseDates = true; // as our data is date-based, we set parseDates to true
               categoryAxis.minPeriod = "DD"; // our data is daily, so we set minPeriod to DD
               categoryAxis.minorGridEnabled = true;
               categoryAxis.axisColor = "#DADADA";
               categoryAxis.twoLineMode = true;
               categoryAxis.dateFormats = [{
                    period: 'fff',
                    format: 'JJ:NN:SS'
                }, {
                    period: 'ss',
                    format: 'JJ:NN:SS'
                }, {
                    period: 'mm',
                    format: 'JJ:NN'
                }, {
                    period: 'hh',
                    format: 'JJ:NN'
                }, {
                    period: 'DD',
                    format: 'DD'
                }, {
                    period: 'WW',
                    format: 'DD'
                }, {
                    period: 'MM',
                    format: 'MM'
                }, {
                    period: 'YYYY',
                    format: 'YYYY'
                }];

               // first value axis (on the left)
               var valueAxis1 = new AmCharts.ValueAxis();
               valueAxis1.axisColor = "#3498db";
               valueAxis1.axisThickness = 2;
               chart.addValueAxis(valueAxis1);

               // second value axis (on the right)
               //var valueAxis2 = new AmCharts.ValueAxis();
               //valueAxis2.position = "right"; // this line makes the axis to appear on the right
               //valueAxis2.axisColor = "#888888";
               //valueAxis2.gridAlpha = 0;
               //valueAxis2.axisThickness = 2;
               //chart.addValueAxis(valueAxis2);

               // GRAPHS
               // first graph
               var graph1 = new AmCharts.AmGraph();
               graph1.valueAxis = valueAxis1; // we have to indicate which value axis should be used
               graph1.title = "Meeting Hours"; 
               graph1.valueField = "hours";
               graph1.bullet = "round";
               graph1.hideBulletsCount = 30;
               graph1.bulletBorderThickness = 1;
               graph1.lineColor = "#3498db";
               graph1.lineThickness = 2;
               chart.addGraph(graph1);

/*
               // second graph
               var graph2 = new AmCharts.AmGraph();
               graph2.valueAxis = valueAxis1; // we have to indicate which value axis should be used
               //graph2.valueAxis = valueAxis2; // we have to indicate which value axis should be used
               graph2.title = "Facebook"; 
               graph2.valueField = "fb";
               graph2.bullet = "square";
               graph2.hideBulletsCount = 30;
               graph2.bulletBorderThickness = 1;
               graph2.lineColor = "#888888";
               graph2.lineThickness = 2;
               chart.addGraph(graph2);

               // second graph
               var graph3 = new AmCharts.AmGraph();
               graph3.valueAxis = valueAxis1; // we have to indicate which value axis should be used
               graph3.title = "Notables"; 
               graph3.valueField = "notables";
               graph3.bullet = "triangle";
               graph3.hideBulletsCount = 30;
               graph3.bulletBorderThickness = 1;
               graph3.lineColor = "#A88888";
               graph3.lineThickness = 2;
               //chart.addGraph(graph3);
*/
               // CURSOR
               var chartCursor = new AmCharts.ChartCursor();
               chartCursor.cursorAlpha = 0.1;
               chartCursor.fullWidth = true;
               chartCursor.valueLineBalloonEnabled = true;
               chart.addChartCursor(chartCursor);

               // SCROLLBAR
               var chartScrollbar = new AmCharts.ChartScrollbar();
               chart.addChartScrollbar(chartScrollbar);

               // LEGEND
               var legend = new AmCharts.AmLegend();
               legend.marginLeft = 110;
               legend.useGraphSettings = true;
               chart.addLegend(legend);

               // WRITE
               chart.write("chartdiv");
           });

           // this method is called when chart is first inited as we listen for "dataUpdated" event
           function zoomChart() {
               // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
               if (chartData.length > 200)
                   chart.zoomToIndexes(Math.round(chartData.length * 0.4), chartData.length - 1);
           }

</script>

 <div id="chartdiv" style="width: 100%; height: 400px;"></div>


