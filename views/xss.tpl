% rebase('_base.tpl', title='Page Title')

<div class="form-container">
    <h1>Cross-Site Scripting (XSS)</h1>
    <form method="POST" action="/trigger/xss/xss">
        <label for="input">Enter Some Text:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., <script>alert(1)</script>" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>