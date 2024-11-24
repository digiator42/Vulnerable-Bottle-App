% rebase('_base.tpl', title='Main')

<h1>Local File Inclusion Vulnerability</h1>
<form action="/trigger/lfi/lfi" method="POST">
    <label for="file">Enter the file path to include:</label>
    <input type="text" id="file" name="file">
    <button type="submit">Submit</button>
</form>