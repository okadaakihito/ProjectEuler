<?php 
$num=600851475143; //�ő�l
$mul=1; //�f�����|�����킹����
$sqrt=ceil(sqrt($num)); //�ő�l�̕�����
echo "Debug:num=$num,sqrt=$sqrt<br>";
for ($i=2;$i<=$sqrt;$i++){
//�f����T���Ă���
	while(true){
		if($num % $i == 0){
			echo "Debug:$i is the prime factor,";
			$lpf=$i; //�f���̍ő�l��ۑ�����
			$num=$num/$i; //�f���Ŋ���
			$mul=$mul*$i; //�f���̂������킹���X�V
			echo "num=$num,mul=$mul<br>";
		}else{
			break; //������x�������Ń`�F�b�N���āA������Ȃ������ꍇ�͔�����
		}
	}
}
echo "Info:The largest prime factor is $lpf"; //���̏o��
?>
