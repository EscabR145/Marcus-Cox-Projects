<?php
include 'config/db.php';
include 'config/helpers.php';

$orders = all(q($conn, "
    SELECT so.OrderID, p.ModelNumber, so.OrderDate, so.QuantityOrdered, so.TotalAmount
    FROM SALES_ORDER so
    JOIN PRODUCT p ON so.ProductID = p.ProductID
    ORDER BY so.OrderID
")); //Query to get all orders from db
?>

<h2>Orders</h2>
<p><a href="dashboard.php">Dashboard</a></p> <!-- Display dashboard and all order from query -->

<table border="1" cellpadding="8">
    <tr>
        <th>ID</th><th>Product</th><th>Date</th><th>Qty</th><th>Total</th>
    </tr>
    <?php foreach ($orders as $o) { ?>
    <tr>
        <td><?php echo $o['OrderID']; ?></td>
        <td><?php echo e($o['ModelNumber']); ?></td>
        <td><?php echo $o['OrderDate']->format('Y-m-d'); ?></td>
        <td><?php echo $o['QuantityOrdered']; ?></td>
        <td><?php echo $o['TotalAmount']; ?></td>
    </tr>
    <?php } ?>
</table>