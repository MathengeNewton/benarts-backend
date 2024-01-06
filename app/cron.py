# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# import boto3
# from app import app 
# from app.models import Emails

# Initialize AWS SES client (you might need to configure it with your AWS credentials)
ses = boto3.client('ses', region_name='your_aws_region')

# Function to send emails
def send_emails():
    pass
    # with app.app_context():
    #     try:
    #         # Query your 'emails' table for unsent emails (example)
    #         # unsent_emails = Emails.query.filter_by(sent=False).all()

    #         for email in unsent_emails:
    #             # Send email using AWS SES
    #             response = ses.send_email(
    #                 Source='',
    #                 Destination={'ToAddresses': [email.recipient_email]},
    #                 Message={
    #                     'Subject': {'Data': email.subject},
    #                     'Body': {'Text': {'Data': email.body}}
    #                 }
    #             )

    #             # Update the 'sent' flag in the database if email sent successfully
    #             if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    #                 email.sent = True
    #                 email.sent_at = datetime.utcnow()
    #                 db.session.commit()

    #     except Exception as e:
    #         print(f"Error sending emails: {str(e)}")

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(send_emails, 'interval', minutes=15) 
scheduler.start()

