
def trigger_email_injection(email, user_input):
    email_body = f"To: {email}\n{user_input}\n\nBody Content"
    # send_email(email_body)