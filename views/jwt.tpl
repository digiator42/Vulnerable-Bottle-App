% rebase('_base.tpl', title='Main')

<h1>JWT</h1>
<form action="/jwt/jwt" method="post">
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <input type="hidden" name="jwt" id="jwt" value="50cent">
    <br>
    <button type="submit">Submit</button>
</form>
<div>
    % if output:
    <br>
    <pre class="output">{{output}}</pre>
    % end
</div>

<script>
    document.onload = getAndSetJWTToken();

    async function getAndSetJWTToken() {
        await fetch('/api/get_jwt_token')
            .then(response => response.json())
            .then(data => {
                document.querySelector('#jwt').value = data.token;
            });
    }
</script>