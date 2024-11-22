% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Directory Traversal</h1>
    <form method="POST" action="/directory_traversal">
        <label for="path">Enter File Path:</label><br>
        <input type="text" id="path" name="path" placeholder="e.g., ../../etc/passwd" required>
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