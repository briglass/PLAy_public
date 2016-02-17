<?php

header("Cache-Control: no-cache, must-revalidate"); // HTTP/1.1
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT"); // Date in the past
header("Content-type: text/plain");

//SQL SERVER DETAILS
//$mysql_host = "mysql.laits.utexas.edu";
//$user="psy_turk";
//$password="Yy7m}=*VcLws2s4:z6R{";
//$database="psy_turk";

$db=mysqli_connect($mysql_host,$user,$password,$database) or die("Unable to connect to database server");

if (isset($_SERVER['HTTP_X_FORWARDED_FOR']) && !empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
	$proxy_ips = explode(",", $_SERVER['HTTP_X_FORWARDED_FOR']);
	$ip = $proxy_ips[0];
} else {
	$ip = $_SERVER['REMOTE_ADDR'];
}
//Currently set for SQL database storage, to convert to csv style, remove $db portion
$PlayID = mysqli_real_escape_string($db, $_REQUEST['data']);
$PercResp = mysqli_real_escape_string($db, $_REQUEST['data1']);
$PercReact = mysqli_real_escape_string($db, $_REQUEST['data2']);
$PercSamediff = mysqli_real_escape_string($db, $_REQUEST['data3']);
$PercFirstImg = mysqli_real_escape_string($db, $_REQUEST['data4']);
$PercSecondImg = mysqli_real_escape_string($db, $_REQUEST['data5']);
$PercRedDist = mysqli_real_escape_string($db, $_REQUEST['data6']);
$PercBlueDist = mysqli_real_escape_string($db, $_REQUEST['data7']);
$PercCorrect = mysqli_real_escape_string($db, $_REQUEST['data8']);
$PCorPrcnt =  mysqli_real_escape_string($db, $_REQUEST['data9']);
$PPc =  mysqli_real_escape_string($db, $_REQUEST['data10']);
$PMRT = mysqli_real_escape_string($db, $_REQUEST['data11']);
$PVRT =  mysqli_real_escape_string($db, $_REQUEST['data12']);
$Pv_EZ = mysqli_real_escape_string($db, $_REQUEST['data13']);
$ScreenInfo =  mysqli_real_escape_string($db, $_REQUEST['data14']);
$ExitCount = mysqli_real_escape_string($db, $_REQUEST['data15']);
$pdat = mysqli_real_escape_string($db, $_REQUEST['data16']);
	
$query = "INSERT INTO PLAyExperiment (ip, PlayID, PercResp, PercReact, PercSamediff, PercFirstImg, PercSecondImg, PercRedDist, PercBlueDist, PercCorrect, PCorPrcnt, PPc, PMRT, PVRT, Pv_EZ, ScreenInfo, ExitCount, pdat) VALUES ('{$ip}', '{$PlayID}','{$PercResp}','{$PercReact}','{$PercSamediff}','{$PercFirstImg}','{$PercSecondImg}','{$PercRedDist}','{$PercBlueDist}','{$PercCorrect}','{$PCorPrcnt}','{$PPc}','{$PMRT}','{$PVRT}','{$Pv_EZ}','{$ScreenInfo}','{$ExitCount}','{$pdat})";

if (mysqli_query($db, $query) !== TRUE) {
	echo mysqli_error($db);
}

mysqli_close($db);

	//storing as individual csv file
	//if(empty($writeType)) $writeType="a";//append if nothing is provided (least destructive)
	$Handle = fopen("XXX/". "Perc" .$PlayID . "-" . $pdat, 'a')or die("can't open file " ."XXX/". "Perc" . $PlayID . "-" . $pdat);
	//$data = implode(',',
	fwrite($Handle, $PlayID . ',' . $PCorPrcnt . ',' . $PPc . ',' . $PMRT . ',' . $PVRT . ',' . $Pv_EZ);
	fclose($Handle);
	//Storing on total csv file
	//if($includeIP=="true")  fwrite($Handle,$_SERVER['REMOTE_ADDR'] . '\n');
	$totalResults = fopen('XXXPerc.csv', 'a')or die("can't open file " . 'XXXPerc.csv');
	fwrite($totalResults, $PlayID . ',' . $PCorPrcnt . ',' . $PPc . ',' . $PMRT . ',' . $PVRT . ',' . $Pv_EZ . "\n");
	fclose($totalResults);

echo $ScreenInfo;

?>
