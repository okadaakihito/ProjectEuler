<?php
$i=5;
$sum=5; 
while(true){
    $sqrts=sqrt($i);
    $flag=0;
    for($j=3;$j<=$sqrts;$j=$j+2){
            if($i%$j==0){
                $flag=1;
                break;
            }
    }
    if($flag==0){
        if($i >= 2000000){
            echo "<br>Info : The sum of all the primes below two million is $sum !!<br>";
            break;
        }
        $sum=$sum+$i;
    }
    if(($i-1) % 100000 ==0){
        echo "Debug : Now,calculating $i,the sum is $sum .<br>";
    }
    $i=$i+2;
}
?>