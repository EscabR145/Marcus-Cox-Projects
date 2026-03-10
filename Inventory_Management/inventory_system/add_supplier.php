<?php
include 'config/db.php';
include 'config/helpers.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') { //If user wants to add supplier to db follow these steps
    q($conn, "INSERT INTO SUPPLIER (SupplierName, Email, PhoneNumber) VALUES (?, ?, ?)", [
        $_POST['SupplierName'],
        $_POST['Email'],
        $_POST['PhoneNumber']
    ]); //Get supplier information from html fields and add to db
    echo "Supplier added.";
}
?>

<h2>Add Supplier</h2> <!-- Input fields for user to enter supplier information -->
<p><a href="dashboard.php">Dashboard</a></p>

<form method="POST">
    <input name="SupplierName" placeholder="Supplier Name" required>
    <input type="email" name="Email" placeholder="Email">
    <input name="PhoneNumber" placeholder="Phone Number">
    <button type="submit">Add</button>
</form>