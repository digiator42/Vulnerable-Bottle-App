% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Directory Traversal</h1>
    <form method="POST" action="/trigger/directory-traversal/directory_traversal">
        <label for="input">Enter File Path:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., ../../etc/passwd" required>
        <br><br>
        <button type="submit">Access File</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>