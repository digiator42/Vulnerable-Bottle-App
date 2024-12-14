% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Insecure File Access</h1>
    <form method="POST" action="/file-read/file_read">
        <label for="input">File Path:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., /etc/passwd" required>
        <br><br>
        <button type="submit">Read File</button>
    </form>
    <div>
        % if output:
        <br>
        <pre class="output">{{output}}</pre>
        % end
    </div>
</div>