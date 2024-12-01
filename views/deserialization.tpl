% rebase('_base.tpl', title='Main')

<h1>Deserialization Example</h1>
<form method="post" action="/trigger/deserialization/deserialization">
    <label for="data">Enter serialized data:</label>
    <textarea id="data" name="data" rows="4" cols="50"></textarea>
    <br>
    <input type="submit" value="Deserialize">
</form>