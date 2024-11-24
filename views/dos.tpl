% rebase('_base.tpl', title='Main')

<h1>Simulate DOS Attack</h1>
<form method="post" action="/trigger/dos/dos">
    <label for="requests">Number of Requests:</label>
    <input type="number" id="requests" name="requests" min="1" required>
    <button type="submit">Start Attack</button>
</form>