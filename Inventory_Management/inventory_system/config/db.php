<?php //This file makes a connection to the database
$serverName = "DESKTOP-KC06TCQ"; //Database server name
$connectOptions = [ "Database" => "ComputerHardwareInventory", "Uid" =>"", "PWD" =>""]; //String array to hold database name, uid, and password
$conn = sqlsrv_connect($serverName,$connectOptions); //sql connect command, passes info of the db into the connect
if($conn == false)
    die(print_r(sqlsrv_errors(),true)); //If we cannot connect end the command and return the error
?>
