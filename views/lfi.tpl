% rebase('_base.tpl', title='Main')

<h1>Local File Inclusion Vulnerability</h1>
<form action="/trigger/lfi/lfi" method="POST">
    <label for="input">Enter the file path to include:</label>
    <input type="text" id="input" name="input">
    <button type="submit">Submit</button>
</form>