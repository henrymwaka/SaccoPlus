from django.db import models
from django.contrib.auth.models import User

# 1. MEMBER PROFILE
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.member_id})"

# 1b. BIOGRAPHIC INFO
class BiographicInfo(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    id_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.member} - {self.id_number}"

# 2. SAVINGS
class Savings(models.Model):
    SAVINGS_TYPE = (
        ('regular', 'Regular'),
        ('unit_trust', 'Unit Trust'),
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    savings_type = models.CharField(max_length=20, choices=SAVINGS_TYPE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.savings_type} - UGX {self.amount}"

# 3. LOANS
class Loan(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('paid', 'Paid'),
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    principal = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # % per month
    term_months = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    approved_date = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.id} for {self.member}"

# 3b. CREDIT HISTORY
class CreditHistory(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, null=True, blank=True, on_delete=models.SET_NULL)
    event = models.CharField(max_length=100)  # e.g., 'Loan Approved', 'Defaulted'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.event} on {self.timestamp.date()}"

# 4. LOAN REPAYMENTS
class LoanRepayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Repayment of UGX {self.amount} for Loan {self.loan.id}"

# 5. UNIT TRUST RETURNS (ANNUALIZED)
class UnitTrustEarning(models.Model):
    date = models.DateField()
    rate_percent = models.DecimalField(max_digits=5, decimal_places=2)
    total_income = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.rate_percent}%"

# 5b. UNIT TRUST LEDGER (MOVEMENTS IN/OUT)
class UnitTrustLedger(models.Model):
    TRANSACTION_TYPE = (
        ('deposit', 'Deposit into Unit Trust'),
        ('withdrawal', 'Withdrawal for Loans'),
        ('interest', 'Earned Interest'),
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.transaction_type} - UGX {self.amount}"

# 6. YEAR-END INTEREST SHARING
class InterestSharing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    gross_interest = models.DecimalField(max_digits=12, decimal_places=2)
    admin_fee = models.DecimalField(max_digits=12, decimal_places=2)
    net_interest = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.member} - {self.year} - UGX {self.net_interest}"

# 7. NOTIFICATIONS
class Notification(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.message[:30]}..."
