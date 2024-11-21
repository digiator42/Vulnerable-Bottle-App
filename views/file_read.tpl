% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>Insecure File Access</h1>
    <form method="POST" action="/file_read">
        <label for="filepath">File Path:</label><br>
        <input type="text" id="filepath" name="filepath" placeholder="e.g., /etc/passwd" required>
        <br><br>
        <button type="submit">Read File</button>
    </form>
</div>