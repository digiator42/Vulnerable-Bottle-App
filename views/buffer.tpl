% rebase('_base.tpl', title='Main')

<h1>Buffer Overflow Vulnerability</h1>
<form action="/buffer/buffer_overflow" method="post">
    <label for="input">Enter Input:</label>
    <input type="text" id="input" name="input" size="15" maxlength="15">
    <button type="submit">Submit</button>
</form>
<div>
    % if output:
    <br>
    {{output}}
    % end