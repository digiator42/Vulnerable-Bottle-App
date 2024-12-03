<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html,
        body {
            height: 100%;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: rgb(206, 206, 204);
        }

        .output {
            background-color: white;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
            padding: 10px;
        }

        h2 {
            margin-top: 10px;
        }
    </style>
    <title>Document</title>
</head>

<body>
    % if output:
    <h2>{{ vuln }} logs</h2>
    <pre class="output">{{ output }}</pre>
    % end
</body>

</html>