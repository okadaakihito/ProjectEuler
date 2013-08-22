<?php
$check=99999;
for($x=999;$x>=100;$x--){
	for($y=999;$y>=100;$y--){
		$mal = $x * $y;
		$strlengs=strlen($mal);
		if($strlengs==6){
			$malstr=(string) $mal;
			$malrev=strrev($malstr);
			if($malstr==$malrev){
				//echo "Debug : $mal is palindrome<br>";
			    if($mal > $check){
			    	$check=$mal;
			    	echo "Debug : $mal is largest palindrome now.<br>";
			    	$maxx=$x;
			    	$maxy=$y;
			    }
			}
		}else{
			//echo "Debug:5digits<br>";
			break;
		}
	}
}
echo "Info  : The largest palindrome made from the product of two 3-digit numbers is $check<br>Info  : max x is $maxx.max y is $maxy";
?>