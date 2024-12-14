% rebase('_base.tpl', title='Main')

<h1>Send Email</h1>
<form action="/email_injection/email_injection" method="post">
    <label for="email">To:</label>
    <input type="email" id="email" name="email" required><br><br>

    <label for="subject">Subject:</label>
    <input type="text" id="subject" name="subject" required><br><br>

    <label for="message">Message:</label><br>
    <textarea id="message" name="message" rows="10" cols="30" required></textarea><br><br>

    <input type="submit" value="Send Email">
</form>