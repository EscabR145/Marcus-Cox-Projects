<?php //Information page with total products, order, suppliers, and number of low stock items
include 'config/db.php';
include 'config/helpers.php';

$products = sqlsrv_fetch_array(q($conn,"SELECT COUNT(*) AS total FROM PRODUCT"),SQLSRV_FETCH_ASSOC)['total']; //Gets product count
$suppliers = sqlsrv_fetch_array(q($conn,"SELECT COUNT(*) AS total FROM SUPPLIER"),SQLSRV_FETCH_ASSOC)['total']; //Gets supplier count
$orders = sqlsrv_fetch_array(q($conn,"SELECT COUNT(*) AS total FROM SALES_ORDER"),SQLSRV_FETCH_ASSOC)['total']; //Gets order count
$lowStock = sqlsrv_fetch_array(q($conn,"SELECT COUNT(*) AS total FROM PRODUCT WHERE QuantityInStock<=10"),SQLSRV_FETCH_ASSOC)['total']; //Get number of stock less than 10
?>
<h2>Dashboard</h2> <!-- Links to other pages, and display total numbers -->
<p><a href="index.php">Products</a>| <a href="add_product.php">Add Product</a>| <a href="add_supplier.php">Add Supplier</a> | 
<a href="add_order.php">Add Order</a> | <a href="view_orders.php">Orders</a></p>

<ul>
    <li>Total Products: <?php echo $products; ?></li>
    <li>Total Suppliers: <?php echo $suppliers; ?></li>
    <li>Total Orders: <?php echo $orders; ?></li>
    <li>Low Stock Items: <?php echo $lowStock; ?></li>
</ul>