#from django.shortcuts import render
from .models import Category,Product,Cart,CartItem,Order,OrderItem
from .serializers import RegisterSerializer,CategorySerializer,ProductSerializer,ProductCreateSerializer,CartItemSerializer,CartItemCreateSerializer,OrderSerializer,OrderItemSerializer,CartSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated


# Create your views here.
#Register user
@api_view(['POST'])
def register_user(request):
    serializers = RegisterSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)

    return Response(serializers.errors)

#GET ALL PRODUCTS
@api_view(['GET'])
def get_products(request):
    products = product.objects.all()

    search = request.GET.get('search')

    if search:
        products = products.filter(name_icontains=search)

    serializers = ProductSerializers(products,many=True)
    return Response(serializers.data)

#GET SINGLE PRODUCT
@api_view(['GET'])

def get_product(request,pk):
    product = product.objects.get(id=pk)
    serializers = ProductSerializers(product)
    return Response(serializers.data)

#CREATE PRODUCT
@api_view(['POST'])
@permission_classes([IsAdminUser])


def create_product(request):
 serializer = ProductCreateSerializer(data=request.data)

 if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)

 return Response(serializer.errors)


#update products
@api_view(['PUT'])
@permission_classes([IsAdminUser])

def update_product(request,pk):
    product = product.object.get(id=pk)
    serializer = ProductCreateSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


#DELETS PRODUCTS
@api_view(['DELETE'])
@permission_classes([IsAdminUser])

def delete_product(request,pk):
    product = product.objects.get(id=pk)
    product.delete()

    return Response('Product Deleted')


#GET CATEGORIES\
@api_view(['GET'])
def get_category (request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

#creat category
@api_view(['POST'])
@permission_classes([IsAdminUser])

def create_category(request):
    serializer = CategorySerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors) 


#update category
@api_view(['PUT','PATCH'])
@permission_classes([IsAdminUser])

def update_category(request,pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


#DELETS category
@api_view(['DELETE'])
@permission_classes([IsAdminUser])

def delete_category(request,pk):
    category = Category.objects.get(id=pk)
    category.delete()

    return Response('Category Deleted')



#CREATE CART
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def create_cart(request):
    cart= cart.objects.create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

#ADD TO CART
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def add_to_cart(request):
    serializer = CartItemCreateSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save(Cart=Cart)
        return Response(serializer.data)

    return Response(serializer.errors)

#GET CART ITEM
@api_view(['GET'])
@permission_classes([IsAuthenticated])

def get_cart_items(request):
    items = CartItem.objects.filter(cart_user = request)
    serializer = CartItemSerializer(items, many=True)
    return Response (serializer.data)

#Create order
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def create_order(request):
    cart_item = cartItem.objects.filter(cart_user = request.user)

    total = 0

    for item in cart_item:
        total += item.product.price*item.quantity

        for item in cart_item:
            OrderItem.objects.create(
                order = Order,
                product = item.product,
                quantity = item.quantity
            )

        cart_item.delete()

        serializer = OrderSerializers(Order)
        return Response(serializer.data)


#GET ORDER
@api_view(['GET'])
@permission_classes([IsAuthenticated])

def get_orders(request):
    orders = Order.objects.filter(user = request.user)
    serializer = OrderSerializers(orders, many=True)
    return Response(serializer.data)