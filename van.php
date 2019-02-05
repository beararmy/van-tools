<?php

$file_latest   = "./batteries-climate-latest.csv";
$file_recents  = "./batteries-climate-recent-values.csv";
$csv           = array_map('str_getcsv', file($file_latest));
$csv2          = array_map('str_getcsv', file($file_recents));

array_walk($csv, function(&$a) use ($csv)
{
    $a = array_combine($csv[0], $a);
});
array_shift($csv);

 array_walk($csv2, function(&$b) use ($csv2)
 {
    $b = array_combine($csv2[0], $b);
 });
array_shift($csv2);

$timestamp   = $csv[0]['timestamp'];
$temperature = $csv[0]['temperature_in_celsius'];
$humidity    = $csv[0]['relative_humidity'];

echo "<html>
<head>
<meta http-equiv=refresh content=10 />
<title>Van Climate</title>
<link rel=stylesheet type=text/css href=van.css>
</head>
<body>";
echo "<h2>Current climate in the van:</h2>";
echo "<b>Last updated at: </b>$timestamp<br>";
echo "<b>Temperature is: </b>$temperature<br>";
echo "<b>Humidity is: </b>$humidity<br>";
echo "<br>";
echo "<b>Some Recent stats:</b><br>";
foreach ($csv2 as &$value) {
    $timestamp = $value['timestamp'];
    $temperature = $value['temperature_in_celsius'];
    $humidity = $value['relative_humidity'];
    echo "$timestamp Ago / $temperature °C / $humidity%<br>";
}
echo "</body>
</html>";
?>