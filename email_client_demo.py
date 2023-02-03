import smtplib
from email.mime.text import MIMEText
# Berkay Gülen -- 20170613017 -- Section 2

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
username = 'dummy1999mail@gmail.com'
password = 'test_password'
sender = 'dummy1999mail@gmail.com'
targets = ['ieu.cseng@gmail.com']

msg = MIMEText("""
Hello, my TCP packet response includes this information:

 Source Port: 465 
 Source Address: 142.250.110.108
 Destination Port: 25877
 Destination Address: 192.168.1.10
 Sequence Number: 0 (relative sequence number)
 Sequence Number (raw): 1958527725
 Acknowledgment Number: 1 (relative ack number)
 Acknowledgment number (raw): 2246795693
 0110 .... = Header Length: 24 bytes (6)
 Flags: 0x012 (SYN, ACK)
 window: 65535
 Checksum: 0x52f2 [unverified]
 [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 42]
        [The RTT to ACK the segment was: 0.067568000 seconds]
 [Timestamps]
        [Time since first frame in this TCP stream: 0.067568000 seconds]
        [Time since previous frame in this TCP stream: 0.067568000 seconds]
    
Thank you""")

msg['Subject'] = 'CE306 – Section 2 - Lab Assignment #3'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
