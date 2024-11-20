% rebase('base.tpl', title='Page Title')

<h1>Command Injection Demo</h1>
<form method="post" action="/cmd">
    <input type="text" name="command" placeholder="Enter a command" />
    <button type="submit">Run</button>
</form>