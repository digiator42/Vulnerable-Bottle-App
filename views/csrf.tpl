% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Cross-Site Request Forgery (CSRF)</h1>
    <form method="POST" action="/trigger/csrf/csrf">
        <label for="amount">Transfer Amount:</label><br>
        <input type="number" id="amount" name="amount" required>
        <br><br>
        <label recipient="account">Recipient Account:</label><br>
        <input type="text" id="recipient" name="recipient" placeholder="e.g., 123456789" required>
        <br><br>
        <button type="submit">Transfer</button>
    </form>
</div>

<div>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>