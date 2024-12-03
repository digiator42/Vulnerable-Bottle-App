% rebase('_base.tpl', title='Main')

<h1>Remote File Inclusion Vulnerability</h1>
<form action="/trigger/rfi/rfi" method="POST">
    <label for="input">Enter the file path to include:</label>
    <input type="text" id="input" name="input">
    <button type="submit">Submit</button>
</form>