<h1>Send Email</h1>
<form action="/email/email_injection" method="post">
    <label for="to">To:</label>
    <input type="email" id="to" name="to" required><br><br>

    <label for="subject">Subject:</label>
    <input type="text" id="subject" name="subject" required><br><br>

    <label for="message">Message:</label><br>
    <textarea id="message" name="message" rows="10" cols="30" required></textarea><br><br>

    <input type="submit" value="Send Email">
</form>