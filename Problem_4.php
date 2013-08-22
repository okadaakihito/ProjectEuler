<?php
$check=99999;
for($x=999;$x>=100;$x--){
	for($y=999;$y>=100;$y--){
		$mal = $x * $y;
		$strlengs=strlen($mal);
		if($strlengs==6){
			$m1 = substr($mal,0,1);
			$m2 = substr($mal,1,1);
			$m3 = substr($mal,2,1);
			$m4 = substr($mal,3,1);
			$m5 = substr($mal,4,1);
			$m6 = substr($mal,5,1);
			if($m1==$m6 && $m2==$m5 && $m3==$m4){
				echo "Debug : x=$x,y=$y,m1=$m1,m2=$m2,m3=$m3,m4=$m4,m5=$m5,m6=$m6,$mal<br>";
			    if($mal > $check){
			    	$check=$mal;
			    	echo "Debug : $mal is largest now.<br>";
			    	$maxx=$x;
			    	$maxy=$y;
			    }
			}
		}else{
			// echo "Debug:5 digits<br>";
			break;
		}
	}
}
echo "Info  : The largest palindrome made from the product of two 3-digit numbers is $check<br>Info  : max x is $maxx.max y is $maxy";
?>