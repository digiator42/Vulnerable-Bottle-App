% rebase('_base.tpl', title='Page Title')

<h1>Crypto</h1>
<form action="/crypto/crypto" method="post">
    <label for="password">Verify Password:</label>
    <input type="password" id="password" name="password" required>
    <button type="submit">Submit</button>
</form>
% if output:
{{output}}
% end