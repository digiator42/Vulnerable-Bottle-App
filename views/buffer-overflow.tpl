% rebase('_base.tpl', title='Main')

<h1>Buffer Overflow</h1>
<form action="/buffer-overflow/buffer_overflow" method="post">
    <label for="input">Enter Input:</label>
    <input type="text" id="input" name="input" size="15" maxlength="15">
    <button type="submit">Submit</button>
</form>
<div>
    % if output:
    <br>
    {{output}}
    % end