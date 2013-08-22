<?php
$term1=1;
$term2=2;
$sum=2;

while (true) {
	$term3=$term1+$term2;
	if($term3 > 4000000){
    	echo "The sum of the even-valued terms is {$sum}";
		break;
	}
        echo "Debug:$term1,$term2,$term3<br>";
	if($term3 % 2 == 0){
		$sum=$term3+$sum;
		echo "Debug:$sum<br>";
	}
	$term1=$term2;
	$term2=$term3;

}
?>


