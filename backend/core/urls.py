from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MemberViewSet, SavingsViewSet, LoanViewSet, LoanRepaymentViewSet,
    UnitTrustEarningViewSet, InterestSharingViewSet, NotificationViewSet,
    CreditHistoryViewSet, BiographicInfoViewSet, UnitTrustLedgerViewSet,
    RegisterView
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'savings', SavingsViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'loan-repayments', LoanRepaymentViewSet)
router.register(r'unit-trust-earnings', UnitTrustEarningViewSet)
router.register(r'interest-sharing', InterestSharingViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'credit-history', CreditHistoryViewSet)
router.register(r'bio-info', BiographicInfoViewSet)
router.register(r'unit-trust-ledger', UnitTrustLedgerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
]
