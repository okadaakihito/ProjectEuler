<?php 
$num=600851475143; //Å‘å’l
$mul=1; //‘f”‚ðŠ|‚¯‚ ‚í‚¹‚½”
$sqrt=ceil(sqrt($num)); //Å‘å’l‚Ì•½•ûª
echo "Debug:num=$num,sqrt=$sqrt<br>";
for ($i=2;$i<=$sqrt;$i++){
//‘f”‚ð’T‚µ‚Ä‚¢‚­
	while(true){
		if($num % $i == 0){
			echo "Debug:$i is the prime factor,";
			$lpf=$i; //‘f”‚ÌÅ‘å’l‚ð•Û‘¶‚·‚é
			$num=$num/$i; //‘f”‚ÅŠ„‚é
			$mul=$mul*$i; //‘f”‚Ì‚©‚¯‡‚í‚¹‚ðXV
			echo "num=$num,mul=$mul<br>";
		}else{
			break; //‚à‚¤ˆê“x“¯‚¶”‚Åƒ`ƒFƒbƒN‚µ‚ÄA‚©‚©‚ç‚È‚©‚Á‚½ê‡‚Í”²‚¯‚é
		}
	}
}
echo "Info:The largest prime factor is $lpf"; //‰ð‚Ìo—Í
?>
