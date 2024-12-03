% rebase('_base.tpl', title='Main')

<h1>Deserialization Example</h1>
<form method="post" action="/trigger/deserialization/deserialization">
    <label for="input">Enter serialized data:</label>
    <textarea id="input" name="input" rows="4" cols="50"></textarea>
    <br>
    <input type="submit" value="Deserialize">
</form>