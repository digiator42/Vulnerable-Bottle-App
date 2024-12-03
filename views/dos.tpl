% rebase('_base.tpl', title='Main')

<h1>Simulate DOS Attack</h1>
<form method="post" action="/trigger/dos/dos">
    <label for="input">Number of Requests:</label>
    <input type="number" id="input" name="input" min="1" required>
    <button type="submit">Start Attack</button>
</form>
% if output:
<pre>{{ output }}</pre>
% end