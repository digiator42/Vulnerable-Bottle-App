% rebase('base.tpl', title='Main')

<div class="form-container">
    <h1>Cross-Site Request Forgery (CSRF)</h1>
    <form method="POST" action="/csrf">
        <label for="amount">Transfer Amount:</label><br>
        <input type="number" id="amount" name="amount" required>
        <br><br>
        <label for="account">Recipient Account:</label><br>
        <input type="text" id="account" name="account" placeholder="e.g., 123456789" required>
        <br><br>
        <button type="submit">Transfer</button>
    </form>
</div>