<?php

class User
{
  public $college = "UEC";

  public function __toString()
  {
    if($this->college !== "MIT") {
      die("try again");
    }
      return "flag{0bj3c7_1nj3c710n_vuln3r4b1l17y}";
  }
}

if(isset($_GET["data"])){
  $user_data = unserialize($_GET["data"]);
  if($user_data == null){
    die("try again");
  }else{
      echo $user_data;
  }
}else{
  echo "find a vulnerability and get a flag!";
  include("./hint.html");
}
?>
