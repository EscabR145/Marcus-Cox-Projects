<?php //File to delete product from database
include 'config/db.php';
include 'config/helpers.php';

$id = $_GET['id'] ?? ''; //Search for product matching the id, if not found report missing product.
if ($id === '') die("Missing product ID.");

$count = sqlsrv_fetch_array( //Get the number of product being ordered that the user wants to delete
    q($conn, "SELECT COUNT(*) AS total FROM SALES_ORDER WHERE ProductID = ?", [$id]),
    SQLSRV_FETCH_ASSOC
)['total'];

if ($count > 0) die("Cannot delete product used in sales orders."); //If the product is being ordered do not delete

q($conn, "DELETE FROM PRODUCT WHERE ProductID = ?", [$id]); //Query to delete product from product table

header("Location: index.php");
exit;