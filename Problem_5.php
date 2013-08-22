<?php
$mal=11*12*13*14*15*16*17*18*19*20;
echo "Debug  : Start is $mal<br>";
for($x=10;$x>=2;$x--){
	while(true){
		if($mal % $x==0){
			$oldmal=$mal;
			$mal=$mal/$x;
			echo "Debug  : newmal=$oldmal,mal=$mal,$x<br>";
			for($y=20;$y>=1;$y--){
				if ($mal % $y!=0){
					echo "Debug  : newmal=$oldmal,mal=$mal,$x,$y<br>";
					echo "Debug  : $mal is not Smallest multiple<br>";
					$mal=$oldmal;
					break 2;
				}
			}
			echo "Debug  : $mal is Smallest multiple now<br>";
		}else{
			echo "Error  : Couldn't complete $mal,$x,$y";
		}
	} 
}
echo "Info  : Smallest multiple is $mal";
?>