from rest_framework.views import APIView
from backend.services import initialise_wallet, view_wallet, disable_wallet, transaction_wallet
from backend.serializers import InitSerializer, TransactionRequestSerializer, DisableWalletRequestSerializer
from rest_framework.response import Response


class InitialiseWallet(APIView):

    def post(self, request):
        serializer = InitSerializer(data=request.POST)
        if serializer.is_valid():
            response = initialise_wallet(serializer.validated_data)
            if response['status'] == "success":
                status = 201
            else:
                status = 400
            return Response(response, status=status)
        else:
            return Response(serializer.errors, status=400)


class WalletView(APIView):
    def get(self, request):
        response = view_wallet(user=request.user, only_view=True)
        if response['status'] == 'success':
            status = 200
        else:
            status = 400
        return Response(response, status=status)

    def post(self, request):
        response = view_wallet(user=request.user)
        if response['status'] == 'success':
            status = 201
        else:
            status = 400
        return Response(response, status=status)

    def patch(self, request):
        serializer = DisableWalletRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            response = disable_wallet(user)
            if response['status'] == 'success':
                status = 200
            else:
                status = 400
        else:
            response, status = serializer.errors, 400
        return Response(response, status=status)


class DepositToWallet(APIView):
    def post(self, request):
        transaction_type = 'deposit'
        account = request.user.account
        serializer = TransactionRequestSerializer(
            data=request.POST, context={'trx_type': transaction_type, 'account': account})
        if serializer.is_valid():
            user = request.user
            response = transaction_wallet(serializer.validated_data, user, transaction_type)
            if response['status'] == 'success':
                status = 201
            else:
                status = 400
        else:
            response, status = serializer.errors, 400
        return Response(response, status=status)


class WithdrawalFromWallet(APIView):
    def post(self, request):
        transaction_type = 'withdrawl'
        account = request.user.account
        serializer = TransactionRequestSerializer(
            data=request.POST, context={'trx_type': transaction_type, 'account': account})
        if serializer.is_valid():
            user = request.user
            response = transaction_wallet(serializer.validated_data, user, transaction_type)
            if response['status'] == 'success':
                status = 201
            else:
                status = 400
        else:
            response, status = serializer.errors, 400
        return Response(response, status=status)