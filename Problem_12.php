<?php
/* ‰Šú’l‚Ì‘ã“ü */
$i=1;  //ŽOŠp”‚Ì‘•ª’l
$tn=1; //ŒvŽZ“r’†‚ÌŽOŠp”‚Ì’l
$tnm=$tn; //‘fˆö”•ª‰ð“r’†‚Ì’l
$prod=1; //–ñ”‚Ì”

while(true){
	$limit=sqrt($tn);
	for($j=2;$j<=$limit;$j=$j+1){
		if($tnm%$j==0){
			$l=1;
			while(true){
				$tnm=$tnm/$j;
				if($tnm%$j!=0){
					$prod=($l+1)*$prod;
					break;
				}
				$l++;
			}
		}
	}
	if($tnm!=1){
		$prod=2*$prod; //$limitˆÈã‚ÌA‚ ‚Ü‚è‚ª¶‚¶‚½Žž‚Ì‚½‚ß(‘f”‚Ìê‡‚È‚Ç)
	}
	echo "Debug : $tn - $tn is $prod,$i<br>";
	if($prod >= 500){
		echo "Info : The value of the first triangle number to have over five hundred divisors is  $tn .<br>";
		break;
	}
	/* ’l‚ÌXV */
	$i=$i+1; 
	$tn=$tn+$i;
	$tnm=$tn;
	$prod=1;
}
?>