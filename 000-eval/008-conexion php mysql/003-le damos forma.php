<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
</head>

<body>
    <header>
        <h1>Bryan Alejandro Avila Castro</h1>
        <h2>Blog increible</h2>
    </header>

    <main>
        <?php

        $host = "localhost";
        $user = "blogphp";
        $pass = "Blogphp123$";
        $DB = "blogphp";

        $conexion = new mysqli($host, $user, $pass, $DB);

        $sql = "SELECT * FROM blog";

        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
            echo '
        <article>
            <h3>' . $fila['titulo'] . '</h3>
            <time>' . $fila['fecha'] . '</time>
            <p>' . $fila['autor'] . '</p>
            <p>' . $fila['contenido'] . '</p>
        </article>
    ';
        }

        $conexion->close();
        ?>
    </main>

</body>

</html>