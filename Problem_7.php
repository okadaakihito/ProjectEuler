<?php
$i=5;
$nmbr=3; 
while(true){
    $sqrts=ceil(sqrt($i));
    $flag=0;
    for($j=3;$j<=$sqrts;$j=$j+2){
            if($i%$j==0){
                $flag=1;
                break;
            }
    }
    if($flag==0){
        echo "Debug : $i is the {$nmbr}st prime number !!<br>";
        if($nmbr==10001){
            break;
        }
        $nmbr=$nmbr+1;
    }
    $i=$i+2;
}
?>