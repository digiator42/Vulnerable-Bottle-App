% rebase('_base.tpl', title='Page Title')

<h1>Command Injection</h1>
<div class="form-container">
    <form method="POST" action="/trigger/cmd/cmd">
        <label for="input">Enter a Command:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., ls" required>
        <button type="submit">Run Command</button>
    </form>
</div>
<div class="form-container">
    <form method="POST" action="/trigger/cmd/subprocess_cmd">
        <label for="input">Ping IP:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., ls" required>
        <button type="submit">Run Command</button>
    </form>
</div>
% if output:
    <br>
    <pre class="output">{{output}}</pre>
% end