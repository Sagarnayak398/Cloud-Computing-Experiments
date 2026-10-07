# salesforce-DC-mail-service

Salesforce Apex Email Service — Cloud Computing Lab

Overview
This lab experiment demonstrates how to send an email using Apex code through the Salesforce Developer Console. The goal was to understand how Salesforce's `Messaging` class can be used to programmatically send emails, and to verify successful delivery using debug logs.

Objective
Learn how to write and execute anonymous Apex code in the Developer Console.
Use the `Messaging.SingleEmailMessage` class to send an email.
Verify email delivery using `System.debug()` logs.
Tools Used
Salesforce Developer Console (Execute Anonymous Window)
Apex Programming Language
Apex Code
```apex
// 1. Create a new single email message object
Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

// 2. Specify the recipient email addresses (Replace with your email)
String[] toAddresses = new String[] {'your-email@example.com'};
mail.setToAddresses(toAddresses);

// 3. Set the email details
mail.setSubject('Test Email from Salesforce Developer Console');
mail.setPlainTextBody('Hello! This email was successfully generated and sent using Apex code via the Developer Console.');

// 4. Send the email
Messaging.SendEmailResult[] results = Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

// 5. Verify if the email was sent successfully
if (results[0].isSuccess()) {
    System.debug('Email sent successfully!');
} else {
    System.debug('Email delivery failed: ' + results[0].getErrors()[0]);
}
```
Steps Followed
Opened the Developer Console in Salesforce.
gone to Debug → Open Execute Anonymous Window.
Wrote the Apex code above to construct and send an email using `Messaging.SingleEmailMessage`.
Checked Open Log and clicked Execute to run the script.
Verified the debug log, which showed `Email sent successfully!`, confirming the email was sent without errors.
Checked the recipient inbox and found the test email delivered (it landed in the Spam folder, which is expected for test emails from developer orgs).
Output
1. Debug Log Confirmation
The execution log in the Developer Console showed:
```
USER_DEBUG | Email sent successfully!
```
2. Email Received
The recipient inbox received the email with:
Subject: Test Email from Salesforce Developer Console
Body: "Hello! This email was successfully generated and sent using Apex code via the Developer Console."
(See screenshots folder for the Developer Console execution log and the received email.)

Screenshots

<img width="1362" height="857" alt="developer-console-log" src="https://github.com/user-attachments/assets/a4f99170-9023-4709-8fda-10ffdd14dc21" />
Apex code and successful execution log in the Developer Console
<img width="540" height="1206" alt="test mail" src="https://github.com/user-attachments/assets/92ac784c-112f-458f-9d9e-d37baa175b9d" />

 Test email received in the inbox (Gmail)
