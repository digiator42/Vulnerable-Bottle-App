% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Cross-Site Request Forgery (CSRF)</h1>
    <form method="POST" action="/csrf/csrf">
        <!-- only for medium and strong levels -->
        <input type="hidden" name="csrf_token" value="">
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
<script>

    document.onload = getCsrfToken();

    async function getCsrfToken() {
        await fetch(`/api/generate_csrf_token`)
            .then(response => response.json())
            .then(data => {
                document.querySelector('input[name="csrf_token"]').value = data.csrf_token;
            })
            .catch(error => console.error('Error fetching CSRF token:', error));
    }
</script>