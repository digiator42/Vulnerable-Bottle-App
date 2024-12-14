% rebase('_base.tpl', title='Page Title')

<h1>Trigger Crypto</h1>
<form action="/crypto/crypto" method="post">
    <label for="input">Enter Data:</label>
    <input type="text" id="input" name="input" required>
    <button type="submit">Submit</button>
</form>
% if output:
{{output}}
% end