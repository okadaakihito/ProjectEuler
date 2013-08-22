<?php
/* 初期値の代入 */
$i=1;  //三角数の増分値
$tn=1; //計算途中の三角数の値
$tnm=$tn; //素因数分解途中の値
$prod=1; //約数の数

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
		$prod=2*$prod; //$limit以上の、あまりが生じた時のため(素数の場合など)
	}
	echo "Debug : $tn - $tn is $prod,$i<br>";
	if($prod >= 500){
		echo "Info : The value of the first triangle number to have over five hundred divisors is  $tn .<br>";
		break;
	}
	/* 値の更新 */
	$i=$i+1; 
	$tn=$tn+$i;
	$tnm=$tn;
	$prod=1;
}
?>