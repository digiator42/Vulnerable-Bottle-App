% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>SQL Injection</h1>
    <form method="POST" action="/sqli">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" placeholder="e.g., admin' OR 1=1 --" required>
        <br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required>
        <br><br>
        <button type="submit">Login</button>
    </form>
</div>