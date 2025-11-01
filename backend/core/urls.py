from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MemberViewSet, SavingsViewSet, LoanViewSet, LoanRepaymentViewSet,
    UnitTrustEarningViewSet, InterestSharingViewSet, NotificationViewSet,
    CreditHistoryViewSet, BiographicInfoViewSet, UnitTrustLedgerViewSet,
    RegisterView
)

router = DefaultRouter()

# ViewSets with static queryset
router.register(r'members', MemberViewSet)
router.register(r'unit-trust-earnings', UnitTrustEarningViewSet)
router.register(r'unit-trust-ledger', UnitTrustLedgerViewSet)

# ViewSets that use get_queryset() — require basename
router.register(r'savings', SavingsViewSet, basename='savings')
router.register(r'loans', LoanViewSet, basename='loans')
router.register(r'loan-repayments', LoanRepaymentViewSet, basename='loan-repayments')
router.register(r'interest-sharing', InterestSharingViewSet, basename='interest-sharing')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'credit-history', CreditHistoryViewSet, basename='credit-history')
router.register(r'bio-info', BiographicInfoViewSet, basename='bio-info')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
]
