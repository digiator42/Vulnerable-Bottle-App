
def trigger_email_injection(data):
    email_body = f"To: {data['email']}\n{data['message']}\n\nBody Content {data['subject']}"
    # send_email(email_body)