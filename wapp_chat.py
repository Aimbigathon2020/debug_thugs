'''To send the message in private chat'''

from twilio.rest import Client 
 
account_sid = 'AC197ed718789b33abc746e34a2dcb77d0' 
auth_token = '4b156a237520c90afe104bceea5e93b8' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body="TN 31 BC 5123 \n red colour \n toyato etios \n stolen vehicle!",      
                              to='whatsapp:+917010874364' 
                          ) 
 
print(message.sid)
