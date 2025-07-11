from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Utility: Get Member instance of the logged-in user
def get_member_from_user(user):
    try:
        return Member.objects.get(user=user)
    except Member.DoesNotExist:
        return None


# -------- Member Profile --------
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]


# -------- Savings --------
class SavingsViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        return Savings.objects.filter(member=member)


# -------- Loans --------
class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        return Loan.objects.filter(member=member)


# -------- Loan Repayments --------
class LoanRepaymentViewSet(viewsets.ModelViewSet):
    serializer_class = LoanRepaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        loans = Loan.objects.filter(member=member)
        return LoanRepayment.objects.filter(loan__in=loans)


# -------- Unit Trust Earnings --------
class UnitTrustEarningViewSet(viewsets.ModelViewSet):
    queryset = UnitTrustEarning.objects.all()
    serializer_class = UnitTrustEarningSerializer
    permission_classes = [IsAuthenticated]


# -------- Year-End Interest Sharing --------
class InterestSharingViewSet(viewsets.ModelViewSet):
    serializer_class = InterestSharingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        return InterestSharing.objects.filter(member=member)


# -------- Notifications --------
class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        return Notification.objects.filter(member=member)


# -------- Credit History --------
class CreditHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = CreditHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        loans = Loan.objects.filter(member=member)
        return CreditHistory.objects.filter(loan__in=loans)


# -------- Biographic Info --------
class BiographicInfoViewSet(viewsets.ModelViewSet):
    serializer_class = BiographicInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        member = get_member_from_user(self.request.user)
        return BiographicInfo.objects.filter(member=member)


# -------- Unit Trust Ledger --------
class UnitTrustLedgerViewSet(viewsets.ModelViewSet):
    queryset = UnitTrustLedger.objects.all()
    serializer_class = UnitTrustLedgerSerializer
    permission_classes = [IsAuthenticated]


# -------- User Registration --------
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
