import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Streamlit app
st.title("CyberPal Email Scenario")

# Input fields
receiver_email = st.text_input("Recipient Email Address", placeholder="Enter your newly created temporary email")
send_email = st.button("Send Email")

if send_email:
    if not receiver_email:
        st.error("Please enter your newly created temporary email")
    else:
        # Email configuration
        sender_email = "secadvisor9@gmail.com"
        password = "vmov qeot zehk mpdj"
        subject = "Important Postal Service Delivery Update"
        body = """
Hello,
You have a package waiting for delivery. However, we were unable to process the delivery fee of $5.99 due to a payment error. Your package will be returned to the sender unless the fee is paid within 48 hours.
        
Please reply to this email with the following payment details to resolve the issue:

- Full Name
- Address
- Credit Card Number
- Expiration Date
- CVV
We apologize for any inconvenience this may have caused. Thank you for your cooperation.

Best regards,
Postal Office Customer Service"""

        # Create the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Send the email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            st.success("Email sent successfully! "
                       "You can close this tab.")
            # st.success("You can close this tab.")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
