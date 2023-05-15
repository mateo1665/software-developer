<!DOCTYPE html>
<html>
<body>
<?php
$nummer1 = rand(1, 10);
$nummer2 = rand(1, 10);

echo("het eerste getal: ". $nummer1 . "<br>");
echo("het tweede getal: ". $nummer2 . "<br>");

echo("plus som " . "<br>");
echo($nummer1 + $nummer2 . "<br>");
echo("min som " . "<br>");
echo($nummer1 - $nummer2 . "<br>");
echo("deel som " . "<br>");
echo($nummer1 / $nummer2 . "<br>");
echo("keer som " . "<br>");
echo($nummer1 * $nummer2 . "<br>");
?>

<?php
$nummer = rand(1,10);

for ($x = 1; $x <= 10; $x++) {
  $som = $nummer * $x;
  echo $nummer . "x" . $x . "=" . $som . "<br>";
}
?>

<body>
<html: