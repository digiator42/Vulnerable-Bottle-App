% rebase('_base.tpl', title='Main')

<div class="form-container">
    <h1>SQL Injection</h1>
    <form method="POST" action="/trigger/sqli/sqli">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" placeholder="e.g., admin' OR 1=1" required>
        <br><br>
        <label for="role">Role:</label><br>
        <input type="role" id="role" name="role" required>
        <br><br>
        <button type="submit">Search</button>
    </form>
    <div>
        % if isinstance(output, list):
        <br>
        <pre class="output" style="display: flex; flex-direction: column;">
            % for output in output:
            <span>{{output}}</span>
            % end
        % else:
            {{output}}
        % end
        </pre>
    </div>
</div>