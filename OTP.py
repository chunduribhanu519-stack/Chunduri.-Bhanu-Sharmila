def Saketh_Module():
    from inputimeout import inputimeout, TimeoutOccurred
    from Validation_Functions import email_validation
    import random
    import base64
    from email.message import EmailMessage
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    import os
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials.json')
    TOKEN_FILE = os.path.join(BASE_DIR, 'token.json')

    def gmail_service():
        creds = None

        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())

        return build('gmail', 'v1', credentials=creds)



    def send_otp_gmail(to_email, otp):
        service = gmail_service()

        message = EmailMessage()
        message.set_content(f"Your ERP Login OTP is: {otp}")
        message['To'] = to_email
        message['From'] = "me"
        message['Subject'] = "ERP Login OTP"

        encoded_message = base64.urlsafe_b64encode(
            message.as_bytes()).decode()

        service.users().messages().send(
            userId="me",
            body={'raw': encoded_message}
        ).execute()

    def erp_login():
        global email
        email = input("Enter your email: ")
        email_validation(email)
        otp = random.randint(100000, 999999)
        send_otp_gmail(email, otp)
        try:
            user_otp = inputimeout(prompt='Enter OTP (you have 60 seconds): ', timeout=40)
        except TimeoutOccurred:
            print("OTP expired!")
            return
        if user_otp == str(otp):
            print("Gmail Verified Successfully!")
        else:
            print("Invalid OTP")
            print("Press ' ' to Reenter Your Email and Resend OTP")
            Saketh_Pro=input("Press Y to resend OTP ")
            if Saketh_Pro.lower() == ' ':
                erp_login()
            elif Saketh_Pro.lower() == 'y':
                otp = random.randint(100000, 999999)
                send_otp_gmail(email, otp)
                user_otp = input("Enter OTP: ")
                if user_otp == str(otp):
                    print("Gmail Verified Successfully!")
    erp_login()
    return email
Saketh_Module()