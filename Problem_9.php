<?php 
$flag=0;
for($i=1;$i<=998;$i++){
    for($j=1;$j<=998;$j++){
        $a=1000-$i-$j;
        $left1=pow($a,2)+pow($i,2)-pow($j,2);
        if($left1==0 && $a<$i && $a!=0 && $a > 0){
            echo "The factors of the answer are a=$a,b=$i,c=$j<br>";
            $answer=$a*$i*$j;
            echo "The answer is $answer";
            $flag=1;
        }
    }
}
if($flag == 0){
    echo "I couldn't found.";
}
?>