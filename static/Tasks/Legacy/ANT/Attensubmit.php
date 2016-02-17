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
$AttenResp = mysqli_real_escape_string($db, $_REQUEST['data1']);
$AttenReact = mysqli_real_escape_string($db, $_REQUEST['data2']);
$AttenDone = mysqli_real_escape_string($db, $_REQUEST['data3']);
$AttenTargStore = mysqli_real_escape_string($db, $_REQUEST['data4']);
$AttenCueStore = mysqli_real_escape_string($db, $_REQUEST['data5']);
$AttenCorrect = mysqli_real_escape_string($db, $_REQUEST['data6']);
$AttenTCong = mysqli_real_escape_string($db, $_REQUEST['data7']);
$AttenCuetype = mysqli_real_escape_string($db, $_REQUEST['data8']);
$ACorPrcnt = mysqli_real_escape_string($db, $_REQUEST['data9']);
$APc =  mysqli_real_escape_string($db, $_REQUEST['data10']);
$AMRT = mysqli_real_escape_string($db, $_REQUEST['data11']);
$AVRT =  mysqli_real_escape_string($db, $_REQUEST['data12']);
$Av_EZ = mysqli_real_escape_string($db, $_REQUEST['data13']);
$ScreenInfo =  mysqli_real_escape_string($db, $_REQUEST['data14']);
$ExitCount = mysqli_real_escape_string($db, $_REQUEST['data15']);
$pdat = mysqli_real_escape_string($db, $_REQUEST['data16']);
	
$query = "INSERT INTO PLAyExperiment (ip, PlayID, AttenResp, AttenReact, AttenDone, AttenTargStore, AttenCueStore, AttenCorrect, AttenTCong, AttenCuetype, ACorPrcnt, APc, AMRT, AVRT, Av_EZ, ScreenInfo, ExitCount, pdat) VALUES ('{$ip}', '{$PlayID}','{$AttenResp}','{$AttenReact}','{$AttenDone}','{$AttenTargStore}','{$AttenCueStore}','{$AttenCorrect}','{$AttenTCong}','{$AttenCuetype}','{$ACorPrcnt}','{$APc}','{$AMRT}','{$AVRT}','{$Av_EZ}','{$ScreenInfo}','{$ExitCount}','{$pdat})";

if (mysqli_query($db, $query) !== TRUE) {
	echo mysqli_error($db);
}

mysqli_close($db);


	//storing as individual csv file
	//if(empty($writeType)) $writeType="a";//append if nothing is provided (least destructive)
	$Handle = fopen("XXX/". "Atten" .$PlayID . "-" . $pdat, 'a')or die("can't open file " ."XXX/". "Atten" . $PlayID . "-" . $pdat);
	//$data = implode(',',
	fwrite($Handle, $PlayID . ',' . $ACorPrcnt . ',' . $APc . ',' . $AMRT . ',' . $AVRT . ',' . $Av_EZ);
	fclose($Handle);
	//Storing on total csv file
	//if($includeIP=="true")  fwrite($Handle,$_SERVER['REMOTE_ADDR'] . '\n');
	$totalResults = fopen('XXXAtten.csv', 'a')or die("can't open file " . 'XXXAtten.csv');
	fwrite($totalResults, $PlayID . ',' . $ACorPrcnt . ',' . $APc . ',' . $AMRT . ',' . $AVRT . ',' . $Av_EZ . "\n");
	fclose($totalResults);


echo $ScreenInfo;

?>
