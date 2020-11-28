from django.db import models


class AadharActivationStatus(models.Model):
    uid = models.CharField(max_length=12, blank=False, primary_key=True, unique=True, verbose_name="aadhar_uid")
    is_activated = models.BooleanField(blank=False)


class AddressDetails(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)

    # For state, city and street a choice based lists can also be made have better
    # data validation
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=6)


class QualificationData(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    yop = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=3)


class BankDetails(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=18)
    bank_name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=11)


class PersonalDetails(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(editable=False, auto_now=False, auto_created=False, auto_now_add=False)
    blood_group = models.CharField(max_length=3, help_text="Example: 'AB+', 'O-'")
    contact_number = models.CharField(max_length=10)


class JobExp(models.Model):
    uid = models.ForeignKey(AadharActivationStatus, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=120)
    job_role = models.CharField(max_length=100)
    exp_in_yrs = models.DecimalField(max_digits=3, decimal_places=1)


"""
Could've created custom model field types for YOP, IFSC, UID, Blood group(, etc.) for a better data validity
"""
