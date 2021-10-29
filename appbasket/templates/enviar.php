<?php
    if (isset($POST['enviar'])){
        if (!empty($_POST['nombre']) && !empty($_POST['email']) && !empty($_POST['mensaje'])  )) {
            $nombre = $_POST['nombre'];
            $email = $_POST['email'];
            $mensaje = $_POST['mensaje'];
            $header = 'From: ' . $mail . " \r\n";
            $header .= "X-Mailer: PHP/" . phpversion() . " \r\n";
            $header .= "Mime-Version: 1.0 \r\n";
            $header .= "Content-Type: text/plain";
            $mail = @mail(utf8_decode($mensaje), $header);

            if ($mail) {
            echo "<h4>Contactaremos lo antes posible</h4>";
            }
        }
    }
?>