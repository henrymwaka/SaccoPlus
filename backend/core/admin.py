from django.contrib import admin
from .models import (
    Member, BiographicInfo, Savings, Loan, CreditHistory,
    LoanRepayment, UnitTrustEarning, UnitTrustLedger,
    InterestSharing, Notification
)

admin.site.register(Member)
admin.site.register(BiographicInfo)
admin.site.register(Savings)
admin.site.register(Loan)
admin.site.register(CreditHistory)
admin.site.register(LoanRepayment)
admin.site.register(UnitTrustEarning)
admin.site.register(UnitTrustLedger)
admin.site.register(InterestSharing)
admin.site.register(Notification)
