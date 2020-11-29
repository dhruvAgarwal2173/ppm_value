# Aadhar API

Here I make the assumption the the JWT auth has already been done is stored in the browser cache with
Aadhar UID in the message body of the JWT.
<br>
This API has 6 endpoints:
- is_activated
- address_details
- qualification_details
- bank_details
- personal_details
- job_exp

So I created models for the above but they can easily be replaced with any other `models.py` app from another Django app.
