<?php 
$num=600851475143; //最大値
$mul=1; //素数を掛けあわせた数
$sqrt=ceil(sqrt($num)); //最大値の平方根
echo "Debug:num=$num,sqrt=$sqrt<br>";
for ($i=2;$i<=$sqrt;$i++){
//素数を探していく
	while(true){
		if($num % $i == 0){
			echo "Debug:$i is the prime factor,";
			$lpf=$i; //素数の最大値を保存する
			$num=$num/$i; //素数で割る
			$mul=$mul*$i; //素数のかけ合わせを更新
			echo "num=$num,mul=$mul<br>";
		}else{
			break; //もう一度同じ数でチェックして、かからなかった場合は抜ける
		}
	}
}
echo "Info:The largest prime factor is $lpf"; //解の出力
?>
