<?php //File to edit details of the product such as supplier, quantity, model number, status, and price
include 'config/db.php';
include 'config/helpers.php';

$id = $_GET['id'] ?? ''; //Get id from user field

if ($id === '') die("Missing product ID."); //If cant find id then quit and send missing report

if ($_SERVER['REQUEST_METHOD'] === 'POST') { //Query to update product fields
    q($conn, "UPDATE PRODUCT
              SET ModelNumber = ?, DeviceTypeID = ?, SupplierID = ?, StatusID = ?, QuantityInStock = ?, Price = ?
              WHERE ProductID = ?", [
        $_POST['ModelNumber'],
        $_POST['DeviceTypeID'],
        $_POST['SupplierID'],
        $_POST['StatusID'],
        $_POST['QuantityInStock'],
        $_POST['Price'],
        $id
    ]);

    echo "Product updated.";
}

$product = sqlsrv_fetch_array(q($conn, "SELECT * FROM PRODUCT WHERE ProductID = ?", [$id]), SQLSRV_FETCH_ASSOC); //update table for user
$types = all(q($conn, "SELECT * FROM DEVICE_TYPE"));
$suppliers = all(q($conn, "SELECT * FROM SUPPLIER"));
$statuses = all(q($conn, "SELECT * FROM STOCK_STATUS"));
?>

<h2>Edit Product</h2>
<p><a href="index.php">Back to Products</a></p>

<form method="POST"> <!-- Input fields for product fields, selection fields for ids -->
    <input name="ModelNumber" value="<?php echo e($product['ModelNumber']); ?>" required>

    <select name="DeviceTypeID" required>
        <?php foreach ($types as $t) { ?>
            <option value="<?php echo $t['DeviceTypeID']; ?>" <?php if ($t['DeviceTypeID'] == $product['DeviceTypeID']) echo 'selected'; ?>>
                <?php echo e($t['TypeName']); ?>
            </option>
        <?php } ?>
    </select>

    <select name="SupplierID" required>
        <?php foreach ($suppliers as $s) { ?>
            <option value="<?php echo $s['SupplierID']; ?>" <?php if ($s['SupplierID'] == $product['SupplierID']) echo 'selected'; ?>>
                <?php echo e($s['SupplierName']); ?>
            </option>
        <?php } ?>
    </select>

    <select name="StatusID" required>
        <?php foreach ($statuses as $s) { ?>
            <option value="<?php echo $s['StatusID']; ?>" <?php if ($s['StatusID'] == $product['StatusID']) echo 'selected'; ?>>
                <?php echo e($s['StatusName']); ?>
            </option>
        <?php } ?>
    </select>

    <input type="number" name="QuantityInStock" value="<?php echo $product['QuantityInStock']; ?>" required>
    <input type="number" step="0.01" name="Price" value="<?php echo $product['Price']; ?>" required>
    <button type="submit">Update</button>
</form>