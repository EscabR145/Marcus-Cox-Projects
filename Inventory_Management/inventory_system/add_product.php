<?php
include 'config/db.php';
include 'config/helpers.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') { //If user wants to add product follow steps
    q($conn, "INSERT INTO PRODUCT (ModelNumber, DeviceTypeID, SupplierID, StatusID, QuantityInStock, Price)
              VALUES (?, ?, ?, ?, ?, ?)", [
        $_POST['ModelNumber'],
        $_POST['DeviceTypeID'],
        $_POST['SupplierID'],
        $_POST['StatusID'],
        $_POST['QuantityInStock'],
        $_POST['Price']
    ]); //Get information from input fields and add product into database
    echo "Product added.";
}

$types = all(q($conn, "SELECT * FROM DEVICE_TYPE")); //Holds information on types, suppliers, and status from db and gets called in html for reading
$suppliers = all(q($conn, "SELECT * FROM SUPPLIER"));
$statuses = all(q($conn, "SELECT * FROM STOCK_STATUS"));
?>

<form method="POST">
    <input name="ModelNumber" placeholder="Model Number" required> <!-- Input for user -->

    <select name="DeviceTypeID" required> <!-- Display types, suppliers, and statsues to user -->
        <?php foreach ($types as $t) { ?>
            <option value="<?php echo $t['DeviceTypeID']; ?>"><?php echo e($t['TypeName']); ?></option>
        <?php } ?>
    </select>

    <select name="SupplierID" required>
        <?php foreach ($suppliers as $s) { ?>
            <option value="<?php echo $s['SupplierID']; ?>"><?php echo e($s['SupplierName']); ?></option>
        <?php } ?>
    </select>

    <select name="StatusID" required>
        <?php foreach ($statuses as $s) { ?>
            <option value="<?php echo $s['StatusID']; ?>"><?php echo e($s['StatusName']); ?></option>
        <?php } ?>
    </select>

    <input type="number" name="QuantityInStock" placeholder="Quantity" required> <!-- Input for qty, and price, with submit button to post data -->
    <input type="number" step="0.01" name="Price" placeholder="Price" required>
    <button type="submit">Add</button>
</form>