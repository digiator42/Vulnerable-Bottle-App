% rebase('_base.tpl', title='Page Title')

<h1>Command Injection</h1>
<div class="form-container">
    <form method="POST" action="/cmd-injection/cmd_injection">
        <label for="input">Ping IP:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., ping 127.0.0.0 && ls" required>
        <button type="submit">Run Command</button>
    </form>
</div>
% if output:
<br>
<pre class="output">{{output}}</pre>
% end