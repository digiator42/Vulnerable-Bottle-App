<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/lgoin.css">
    <title>Document</title>
</head>

<body>
    <h1>Welcome admin, login</h1>
    <form class="form-container" action="/login" method="post">
        Username: <input name="username" type="text" /><br>
        Password: <input name="password" type="password" /><br>
        <input value="Login" type="submit" />
        % if output:
        <p>{{ output }}</p>
        % end
    </form>
</body>

</html>