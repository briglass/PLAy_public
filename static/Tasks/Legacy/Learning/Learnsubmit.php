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
$LearnResp = mysqli_real_escape_string($db, $_REQUEST['data1']);
$LearnReact = mysqli_real_escape_string($db, $_REQUEST['data2']);
$LearnQshown = mysqli_real_escape_string($db, $_REQUEST['data3']);
$LearnAshown = mysqli_real_escape_string($db, $_REQUEST['data4']);
$LearnTone = mysqli_real_escape_string($db, $_REQUEST['data5']);
$LearnTtwo = mysqli_real_escape_string($db, $_REQUEST['data6']);
$LearnTthree = mysqli_real_escape_string($db, $_REQUEST['data7']);
$LearnTfour = mysqli_real_escape_string($db, $_REQUEST['data8']);
$LearnTfive = mysqli_real_escape_string($db, $_REQUEST['data9']);
$LearnTsix = mysqli_real_escape_string($db, $_REQUEST['data10']);
$LearnTseven = mysqli_real_escape_string($db, $_REQUEST['data11']);
$LearnTeight = mysqli_real_escape_string($db, $_REQUEST['data12']);
$LearnTnine = mysqli_real_escape_string($db, $_REQUEST['data13']);
$LearnTten = mysqli_real_escape_string($db, $_REQUEST['data14']);
$LearnCorrect = mysqli_real_escape_string($db, $_REQUEST['data15']);
$LCorPrcnt = mysqli_real_escape_string($db, $_REQUEST['data16']);
$LProCorCount = mysqli_real_escape_string($db, $_REQUEST['data17']);
$LProCorPrcnt = mysqli_real_escape_string($db, $_REQUEST['data18']);
$LNonProCorCount = mysqli_real_escape_string($db, $_REQUEST['data19']);
$LNonProCorPrcnt = mysqli_real_escape_string($db, $_REQUEST['data20']);
$LStaticCond =  mysqli_real_escape_string($db, $_REQUEST['data21']);
$ScreenInfo =  mysqli_real_escape_string($db, $_REQUEST['data22']);
$ExitCount = mysqli_real_escape_string($db, $_REQUEST['data23']);
$pdat = mysqli_real_escape_string($db, $_REQUEST['data24']);
//Will insert all above variables into the SQL database	
$query = "INSERT INTO PLAyExperiment (ip, PlayID, LearnResp, LearnReact, LearnQshown, LearnAshown, LearnTone, LearnTtwo, LearnTthree, LearnTfour, LearnTfive, LearnTsix, LearnTseven, LearnTeight, LearnTnine, LearnTten, LearnCorrect, LCorPrcnt, LProCorCount, LProCorPrcnt, LNonProCorCount, LNonProCorPrcnt, LStaticCond, ScreenInfo, ExitCount, pdat) VALUES ('{$ip}', '{$PlayID}','{$LearnResp}','{$LearnReact}','{$LearnQshown}','{$LearnAshown}','{$LearnTone}','{$LearnTtwo}','{$LearnTthree}','{$LearnTfour}','{$LearnTfive}','{$LearnTsix}','{$LearnTseven}','{$LearnTeight}','{$LearnTnine}','{$LearnTten}','{$LearnCorrect}','{$LCorPrcnt}','{$LProCorCount}','{$LProCorPrcnt}','{$LNonProCorCount}','{$LNonProCorPrcnt}','{$LStaticCond}','{$ScreenInfo}','{$ExitCount}','{$pdat})";

if (mysqli_query($db, $query) !== TRUE) {
	echo mysqli_error($db);
}

mysqli_close($db);

	//storing as individual csv file
	//if(empty($writeType)) $writeType="a";//append if nothing is provided (least destructive)
	$Handle = fopen("XXX/". "Learn" .$PlayID . "-" . $pdat, 'a')or die("can't open file " ."XXX/". "Learn" . $PlayID . "-" . $pdat);
	//$data = implode(',',
	fwrite($Handle, $PlayID . ',' . $LCorPrcnt . ',' . $LProCorCount . ',' . $LProCorPrcnt . ',' . $LNonProCorCount . ',' . $LNonProCorPrcnt);
	fclose($Handle);
	//Storing on total csv file
	//if($includeIP=="true")  fwrite($Handle,$_SERVER['REMOTE_ADDR'] . '\n');
	$totalResults = fopen('XXXLearn.csv', 'a')or die("can't open file " . 'XXXLearn.csv');
	fwrite($totalResults, $PlayID . ',' . $LCorPrcnt . ',' . $LProCorCount . ',' . $LProCorPrcnt . ',' . $LNonProCorCount . ',' . $LNonProCorPrcnt . "\n");
	fclose($totalResults);

echo $ScreenInfo;

?>
