% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Server-Side Request Forgery (SSRF)</h1>
    <form method="POST" action="/ssrf/ssrf">
        <label for="input">Target URL:</label>
        <br>
        <input type="input" id="input" name="input" placeholder="e.g., http://localhost/admin" required>
        <br><br>
        <button type="submit">Fetch Data</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class='output'>{{ output[:120] + '...' if len(output) > 120 else output }}</pre>
        % end
    </div>
</div>