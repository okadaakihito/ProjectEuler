<?php
$sum=0;
//echo "$sum";

for ($i = 1; $i <= 340; $i++) {
 $multiple3 = 3 * $i;
 if (1000 > $multiple3 && $i % 5 != 0){
  $sum = $sum + $multiple3;
 // echo "$i:"; 
 // echo "$sum,";
 }
}
for ($i = 1; $i <= 200; $i++) {
 $multiple5 = 5 * $i;
 if (1000 > $multiple5){
  $sum= $sum + $multiple5;
 }
}

echo "The sum of all the multiples of 3 or 5 below 1000 is {$sum}";

?>


