from django.db import models


class AadharActivationStatus(models.Model):
    uid = models.CharField(max_length=12, blank=False, primary_key=True, unique=True, verbose_name="aadhar_uid")
    is_activated = models.BooleanField(blank=False)

    def __str__(self):
        return {"Aadhar UUID": self.uid, "is_activated": self.is_activated}


class AddressDetails(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)

    # For state, city and street a choice based lists can also be made have better
    # data validation
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    postal_code = models.PositiveIntegerField()

    def __str__(self):
        response_dict = {
            "uid": self.uid,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "postal_code": self.postal_code,
        }
        return response_dict


class QualificationData(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    yop = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        response_dict = {
            "uid": self.uid,
            "name": self.name,
            "yop": self.yop,
            "percentage": self.percentage,
        }
        return response_dict


class BankDetails(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=18)
    bank_name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=11, verbose_name="IFSC")

    def __str__(self):
        response_dict = {
            "uid": self.uid,
            "account_number": self.account_number,
            "bank_name": self.bank_name,
            "ifsc": self.ifsc,
        }
        return response_dict


class PersonalDetails(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_created=False, auto_now_add=False)
    blood_group = models.CharField(max_length=3, help_text="Example: 'AB+', 'O-'")
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        response_dict = {
            "uid": self.uid,
            "full_name": self.full_name,
            "date_of_birth": self.date_of_birth,
            "blood_group": self.blood_group,
            "contact_number": self.contact_number,
        }
        return response_dict


class JobExp(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=120)
    job_role = models.CharField(max_length=100)
    exp_in_yrs = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        response_dict = {
            "uid": self.uid,
            "company_name": self.company_name,
            "job_role": self.job_role,
            "exp_in_yrs": self.exp_in_yrs,
        }
        return response_dict


"""
Could've created custom model field types for YOP, IFSC, UID, Blood group(, etc.) for a better data validity
"""
