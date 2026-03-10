<?php //This file has helpers that are used commonly throughout the project
function q($conn, $sql, $params = []) { //Function to send a query to the database
    $stmt = sqlsrv_query($conn, $sql, $params);
    if (!$stmt) die("<pre>" . print_r(sqlsrv_errors(), true) . "</pre>"); //If the query fails send out an error
    return $stmt;
}

function all($stmt) { //Function to list all the rows in a query
    $rows = [];
    while ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) $rows[] = $row;
    return $rows;
}

function e($value) { //Function to return specialchars to prevent script from being ran in user input. html reads as text 
    return htmlspecialchars((string)$value);
}