<?php
include 'config/db.php';
include 'config/helpers.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') { //If we want to add order to database, perform steps
    $productId = $_POST['ProductID']; //Variables to hold information about the order
    $qty = (int) $_POST['QuantityOrdered'];
    $date = $_POST['OrderDate'];

    $product = sqlsrv_fetch_array( // Array that holds price and quantity from product
        q($conn, "SELECT Price, QuantityInStock FROM PRODUCT WHERE ProductID = ?", [$productId]),
        SQLSRV_FETCH_ASSOC
    );

    if (!$product) { //Check if product is on the product table
        echo "Product not found.";
    } elseif ($qty > $product['QuantityInStock']) { //If the qty is more than qty retrieved from product query tell user there is no stock
        echo "Not enough stock.";
    } else {
        $total = $product['Price'] * $qty; //Total price of this product to buy in order

        q($conn, "INSERT INTO SALES_ORDER (ProductID, OrderDate, QuantityOrdered, TotalAmount) 
                  VALUES (?, ?, ?, ?)", [$productId, $date, $qty, $total]); //Enter order into the db

        q($conn, "UPDATE PRODUCT
                  SET QuantityInStock = QuantityInStock - ?
                  WHERE ProductID = ?", [$qty, $productId]); //Update the qty on the product table from what was just ordered

        echo "Order added.";
    }
}

$products = all(q($conn, "SELECT ProductID, ModelNumber FROM PRODUCT ORDER BY ModelNumber")); //Update list of products for user
?>

<h2>Add Order</h2> <!-- Html format for product information from user and button to request order -->
<p><a href="dashboard.php">Dashboard</a></p>

<form method="POST">
    <select name="ProductID" required>
        <option value="">Select Product</option>
        <?php foreach ($products as $p) { ?>
            <option value="<?php echo $p['ProductID']; ?>"><?php echo e($p['ModelNumber']); ?></option>
        <?php } ?>
    </select>

    <input type="date" name="OrderDate" required>
    <input type="number" name="QuantityOrdered" min="1" placeholder="Quantity" required>
    <button type="submit">Add</button>
</form>