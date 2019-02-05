<?php

# First attempt at a page to neatly display the contents of batteries-climate-latest.csv as a webpage

$file_latest = "./batteries-climate-latest.csv";
$csv         = array_map('str_getcsv', file($file_latest));
array_walk($csv, function(&$a) use ($csv)
{
    $a = array_combine($csv[0], $a);
});
array_shift($csv);

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
echo "</body>
</html>";
?>