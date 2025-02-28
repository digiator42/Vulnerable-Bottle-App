% rebase('_base.tpl', title='Main')

<h1>Buffer Overflow</h1>
<form action="/buffer-overflow/buffer_overflow" method="post">
    <label for="input">Enter First Name:</label>
    <input type="text" id="input" name="input" size="15" maxlength="15">
    % if level == 'medium':
    <label for="second_name">Enter Second Name:</label>
    <input type="text" id="second_name" name="second_name" size="15" maxlength="15">
    % end
    <button type="submit">Submit</button>
</form>
<div>
    % if output:
    <br>
    {{output}}
    % end