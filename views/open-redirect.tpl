% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Open Redirect</h1>
    <form method="POST" action="/open-redirect/open_redirect">
        <label for="input">Enter URL:</label><br>
        <input type="input" id="input" name="input" placeholder="e.g., http://malicious-site.com" required>
        <br><br>
        <button type="submit">Redirect</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>