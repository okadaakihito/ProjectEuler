<?php
/* �����l�̑�� */
$i=1;  //�O�p���̑����l
$tn=1; //�v�Z�r���̎O�p���̒l
$tnm=$tn; //�f��������r���̒l
$prod=1; //�񐔂̐�

while(true){
	$limit=sqrt($tn);
	for($j=2;$j<=$limit;$j=$j+1){
		if($tnm%$j==0){
			$l=1;
			while(true){
				$tnm=$tnm/$j;
				if($tnm%$j!=0){
					$prod=($l+1)*$prod;
					break;
				}
				$l++;
			}
		}
	}
	if($tnm!=1){
		$prod=2*$prod; //$limit�ȏ�́A���܂肪���������̂���(�f���̏ꍇ�Ȃ�)
	}
	echo "Debug : $tn - $tn is $prod,$i<br>";
	if($prod >= 500){
		echo "Info : The value of the first triangle number to have over five hundred divisors is  $tn .<br>";
		break;
	}
	/* �l�̍X�V */
	$i=$i+1; 
	$tn=$tn+$i;
	$tnm=$tn;
	$prod=1;
}
?>