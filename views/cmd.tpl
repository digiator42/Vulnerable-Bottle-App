% rebase('_base.tpl', title='Page Title')

<div class="form-container">
    <h1>Command Injection</h1>
    <form method="POST" action="/trigger/cmd/subprocess_cmd">
        <label for="command">Enter a Command:</label><br>
        <input type="text" id="command" name="command" placeholder="e.g., ls" required>
        <button type="submit">Run Command</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>