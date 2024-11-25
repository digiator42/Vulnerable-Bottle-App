% rebase('_base.tpl', title='Main')

<h1>Buffer Overflow Vulnerability</h1>
<form action="/trigger/buffer/buffer_overflow" method="post">
    <label for="input">Enter Input:</label>
    <input type="number" id="input" name="input" size="100">
    <button type="submit">Submit</button>
</form>
<div>
    % if output:
    <br>
    {{output}}
    % end