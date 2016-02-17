<?php

// Need to set permissions for overall results file and individual results folder to 777 (read, write, etc all ticked) once files are put onto server through filezilla


if (isset($_SERVER['HTTP_X_FORWARDED_FOR']) && !empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
	$proxy_ips = explode(",", $_SERVER['HTTP_X_FORWARDED_FOR']);
	$ip = $proxy_ips[0];
} else {
	$ip = $_SERVER['REMOTE_ADDR'];
}

$sscode = $_REQUEST['data'];
$gender = $_REQUEST['data1'];
$age = $_REQUEST['data2'];
$country = $_REQUEST['data3'];
$pgame = $_REQUEST['data4'];
$pgametype = $_REQUEST['data5'];
$pgameexp = $_REQUEST['data6'];
$pgamehrs = $_REQUEST['data7'];
$pgameprof = $_REQUEST['data8'];
$sgame = $_REQUEST['data9'];
$sgametype = $_REQUEST['data10'];
$sgameexp = $_REQUEST['data11'];
$sgamehrs = $_REQUEST['data12'];
$sgameprof = $_REQUEST['data13'];
$tgame = $_REQUEST['data14'];
$tgametype = $_REQUEST['data15'];
$tgameexp = $_REQUEST['data16'];
$tgamehrs = $_REQUEST['data17'];
$tgameprof = $_REQUEST['data18'];
$TaskOrder = $_REQUEST['data19'];
$LearnResp = $_REQUEST['data21'];
$LearnReact = $_REQUEST['data22'];
$LearnQshown = $_REQUEST['data23'];
$LearnAshown = $_REQUEST['data24'];
$LearnTone = $_REQUEST['data25'];
$LearnTtwo = $_REQUEST['data26'];
$LearnTthree = $_REQUEST['data27'];
$LearnTfour = $_REQUEST['data28'];
$LearnTfive = $_REQUEST['data29'];
$LearnTsix = $_REQUEST['data30'];
$LearnTseven = $_REQUEST['data31'];
$LearnTeight = $_REQUEST['data32'];
$LearnTnine = $_REQUEST['data33'];
$LearnTten = $_REQUEST['data34'];
$LearnCorrect = $_REQUEST['data35'];
$LCorPrcnt = $_REQUEST['data36'];
$AttenResp = $_REQUEST['data37'];
$AttenReact = $_REQUEST['data38'];
$AttenDone = $_REQUEST['data39'];
$AttenTargStore = $_REQUEST['data40'];
$AttenCueStore = $_REQUEST['data41'];
$AttenCorrect = $_REQUEST['data42'];
$AttenTCong = $_REQUEST['data43'];
$AttenCuetype = $_REQUEST['data44'];
$ACorPrcnt = $_REQUEST['data45'];
$PercResp = $_REQUEST['data46'];
$PercReact = $_REQUEST['data47'];
$PercSamediff = $_REQUEST['data48'];
$PercFirstImg = $_REQUEST['data49'];
$PercSecondImg = $_REQUEST['data50'];
$PercRedDist = $_REQUEST['data51'];
$PercBlueDist = $_REQUEST['data52'];
$PercCorrect = $_REQUEST['data53'];
$PCorPrcnt =  $_REQUEST['data54'];
$LStaticCond =  $_REQUEST['data55'];
$ScreenInfo =  $_REQUEST['data56'];
$LProCorPrcnt =  $_REQUEST['data57'];
$LPCCount =  $_REQUEST['data58'];
$LNonProCorPrcnt =  $_REQUEST['data59'];
$LNPCCount =  $_REQUEST['data60'];
$ExitCount = $_REQUEST['data20'];
$funnelAvar = $_REQUEST['data70'];
$funnelBvar = $_REQUEST['data71'];
$funnelDvar = $_REQUEST['data72'];
	
	$Handle = fopen("ALLresults/".$sscode . "-" . $pdat, 'a')or die("can't open file " ."ALLresults/". $sscode . "-" . $pdat);
	//$data = implode(',',
	fwrite($Handle, $sscode . ',' . $gender . ',' . $age . ',' . $country . ',' . $pgame . ',' . $pgametype . ',' . $pgameexp . ',' . $pgamehrs . ',' . $pgameprof . ',' . $sgame . ',' . $sgametype . ',' . $sgameexp . ',' . $sgamehrs . ',' . $sgameprof . ',' . $tgame . ',' . $tgametype . ',' . $tgameexp . ',' . $tgamehrs . ',' . $tgameprof . ',' . $TaskOrder . ',' . $LearnResp . ',' . $LearnReact . ',' . $LearnQshown . ',' . $LearnAshown . ',' . $LearnTone . ',' . $LearnTtwo . ',' . $LearnTthree . ',' . $LearnTfour . ',' . $LearnTfive . ',' . $LearnTsix . ',' . $LearnTseven . ',' . $LearnTeight . ',' . $LearnTnine . ',' . $LearnTten . ',' . $LearnCorrect . ',' . $LCorPrcnt . ',' . $LProCorPrcnt . ',' . $LPCCount . ',' . $LNonProCorPrcnt . ',' . $LNPCCount . ',' . $LStaticCond . ',' . $AttenResp . ',' . $AttenReact . ',' . $AttenDone . ','  . $AttenTargStore . ','  . $AttenCueStore . ',' . $AttenCorrect . ',' . $AttenTCong . ',' . $AttenCuetype . ',' . $ACorPrcnt . ',' . $PercResp . ',' . $PercReact . ',' . $PercSamediff . ',' . $PercFirstImg . ',' . $PercSecondImg . ',' . $PercRedDist . ',' . $PercBlueDist . ',' . $PercCorrect . ',' . $PCorPrcnt . ',' . $ScreenInfo . ',' . $ExitCount);//instead of comma separation, it might be more suitable to use an unusual symbol combination as the separator, e.g. %£ although this is likely unnecessary
	fclose($Handle);

	//if($includeIP=="true")  fwrite($Handle,$_SERVER['REMOTE_ADDR'] . '\n');
	$totalResults = fopen('allXResults.csv', 'a')or die("can't open file " . 'allXResults.csv');
	fwrite($totalResults, $sscode . ',' . $gender . ',' . $age . ',' . $country . ',' . $pgame . ',' . $pgametype . ',' . $pgameexp . ',' . $pgamehrs . ',' . $pgameprof . ',' . $sgame . ',' . $sgametype . ',' . $sgameexp . ',' . $sgamehrs . ',' . $sgameprof . ',' . $tgame . ',' . $tgametype . ',' . $tgameexp . ',' . $tgamehrs . ',' . $tgameprof . ',' . $TaskOrder . ',' . $LearnResp . ',' . $LearnReact . ',' . $LearnQshown . ',' . $LearnAshown . ',' . $LearnTone . ',' . $LearnTtwo . ',' . $LearnTthree . ',' . $LearnTfour . ',' . $LearnTfive . ',' . $LearnTsix . ',' . $LearnTseven . ',' . $LearnTeight . ',' . $LearnTnine . ',' . $LearnTten . ',' . $LearnCorrect . ',' . $LCorPrcnt . ',' . $LProCorPrcnt . ',' . $LPCCount . ',' . $LNonProCorPrcnt . ',' . $LNPCCount . ',' . $LStaticCond . ',' . $AttenResp . ',' . $AttenReact . ',' . $AttenDone . ','  . $AttenTargStore . ','  . $AttenCueStore . ',' . $AttenCorrect . ',' . $AttenTCong . ',' . $AttenCuetype . ',' . $ACorPrcnt . ',' . $PercResp . ',' . $PercReact . ',' . $PercSamediff . ',' . $PercFirstImg . ',' . $PercSecondImg . ',' . $PercRedDist . ',' . $PercBlueDist . ',' . $PercCorrect . ',' . $PCorPrcnt . ',' . $ScreenInfo . ',' . $ExitCount);//instead of comma separation, it might be more suitable to use an unusual symbol combination as the separator, e.g. %£
	fclose($totalResults);
	
	$textResults = fopen('txtResults.csv', 'a')or die("can't open file " . 'txtResults.csv');
	fwrite($textResults, $sscode . ',' . $funnelAvar . ',' . $funnelBvar . ',' . $funnelDvar ."\n");
	fclose($textResults);
	
	
	
	echo "result=success";  //needed for FLASH

?>
