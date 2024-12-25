<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
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
    <h2>{{ vuln }} source code</h2>
    <pre class="output"><code class="python">{{ output }}</code></pre>
    % end
</body>

</html>