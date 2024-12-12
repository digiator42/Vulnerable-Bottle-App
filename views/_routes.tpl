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
            display: flex;
            flex-direction: column;
            margin: 0;
            padding: 0;
            align-items: flex-start;
        }

        h2 {
            margin-top: 10px;
        }
    </style>
    <title>Document</title>
</head>

<body>
    <h2>Routes</h2>
    <pre class="output">
    % for route, method in routes:
        % if method == 'GET':
        <span style="color: green; border: 1px solid rgb(32, 151, 47); width: 100%;">
            {{ route }} : {{ method }}
        </span>
        % else:
        <span style="color: blue; border: 1px solid rgb(145, 149, 173); width: 100%;">
            {{ route }} : {{ method }}
        </span>
        % end
    % end
    </pre>
</body>

</html>