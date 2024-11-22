<h1>Remote File Inclusion Vulnerability</h1>
<form action="/trigger/rfi/rfi" method="POST">
    <label for="file">Enter the file path to include:</label>
    <input type="text" id="file" name="file">
    <button type="submit">Submit</button>
</form>