% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Server-Side Request Forgery (SSRF)</h1>
    <form method="POST" action="/ssrf">
        <label for="url">Target URL:</label><br>
        <input type="url" id="url" name="url" placeholder="e.g., http://localhost/admin" required>
        <br><br>
        <button type="submit">Fetch Data</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>