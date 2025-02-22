% rebase('_base.tpl', title='Page Title')

<div class="form-container">
    <h1>Server-Side Template Injection (SSTI)</h1>
    <form method="POST" action="/ssti/ssti">
        <label for="input">Enter Some Text:</label><br>
        <input type="text" id="input" name="input" placeholder="e.g., &#123;&#123;7*7&#125;&#125;" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
</div>