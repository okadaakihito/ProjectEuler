<?php
$powsum=0;
$sum=0;
for($x=1;$x<=100;$x++){
	$powsum=pow($x,2)+$powsum;
	$sum=$sum+$x;
}
$sumpow=pow($sum,2);
$result=$sumpow-$powsum;
echo "Info  : Sum square difference is $result";
?>