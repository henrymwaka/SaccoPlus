from django.contrib import admin
from .models import Member, Savings, Loan, LoanRepayment, UnitTrustEarning, InterestSharing, Notification

admin.site.register(Member)
admin.site.register(Savings)
admin.site.register(Loan)
admin.site.register(LoanRepayment)
admin.site.register(UnitTrustEarning)
admin.site.register(InterestSharing)
admin.site.register(Notification)
