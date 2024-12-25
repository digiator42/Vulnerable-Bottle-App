% rebase('_base.tpl', title='Main')

<h1>Login</h1>
<form action="/brute-force/brute_force" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required><br><br>
    <button type="submit">Login</button>
</form>
% if output:
{{output}}
% end