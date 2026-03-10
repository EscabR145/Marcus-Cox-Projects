<?php //Main page of file that displays all products with name, supplier, price, status, qty, and model number
include 'config/db.php';
include 'config/helpers.php';

$products = all(q($conn, "
    SELECT p.ProductID, p.ModelNumber, d.TypeName, s.SupplierName, st.StatusName, p.QuantityInStock, p.Price
    FROM PRODUCT p
    JOIN DEVICE_TYPE d ON p.DeviceTypeID = d.DeviceTypeID
    JOIN SUPPLIER s ON p.SupplierID = s.SupplierID
    JOIN STOCK_STATUS st ON p.StatusID = st.StatusID
    ORDER BY p.ProductID
")); //Query to get product information
?>

<h2>Products</h2> <!-- Header to link to other pages -->
<p><a href="dashboard.php">Dashboard</a> | <a href="add_product.php">Add Product</a> | <a href="add_supplier.php">Add Supplier</a> | <a href="add_order.php">Add Order</a> | <a href="view_orders.php">Orders</a></p>

<table border="1" cellpadding="8"> <!-- Display product information from query, allow access to edit or delete product -->
    <tr>
        <th>ID</th><th>Model</th><th>Type</th><th>Supplier</th><th>Status</th><th>Qty</th><th>Price</th><th>Actions</th>
    </tr>
    <?php foreach ($products as $p) { ?>
    <tr>
        <td><?php echo $p['ProductID']; ?></td>
        <td><?php echo e($p['ModelNumber']); ?></td>
        <td><?php echo e($p['TypeName']); ?></td>
        <td><?php echo e($p['SupplierName']); ?></td>
        <td><?php echo e($p['StatusName']); ?></td>
        <td><?php echo $p['QuantityInStock']; ?></td>
        <td><?php echo $p['Price']; ?></td>
        <td>
            <a href="edit_product.php?id=<?php echo $p['ProductID']; ?>">Edit</a>
            <a href="delete_product.php?id=<?php echo $p['ProductID']; ?>" onclick="return confirm('Delete this product?');">Delete</a>
        </td>
    </tr>
    <?php } ?>
</table>