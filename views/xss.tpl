% rebase('_base.tpl', title='Page Title')

<div class="form-container">
    <h1>Cross-Site Scripting (XSS)</h1>
    <form method="POST" action="/xss">
        <label for="input">Enter Some Text:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., <script>alert(1)</script>" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
    % if output:
        <p>output:{{output}}</p>
    % end
</div>