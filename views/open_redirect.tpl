% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Open Redirect</h1>
    <form method="POST" action="/open_redirect">
        <label for="url">Enter URL:</label><br>
        <input type="url" id="url" name="url" placeholder="e.g., https://example.com" required>
        <br><br>
        <button type="submit">Redirect</button>
    </form>
</div>