import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def landingPageUser(request):
    return render(request, 'landingPageUser.html')

def shopBooks(request):
    book = Book.objects.all()

    context = {
        'book': book,
    }
    return render(request, 'shopBooks.html', context)

def login_homepage(request):
    num = random.randrange(1000, 9999)
    # global str_num
    # str_num = str(num)
    request.session['str_num'] = str(num)
    # print('inside login_homepage')
    return render(request, 'index.html', {"captcha": str(num)})

def login(request):
    context = {}
    context['captcha'] = request.session.get('str_num')
    # disp = context['captcha']
    if request.method == 'POST':
        captcha = request.POST.get('captcha')
        str_num = request.session.get('str_num')
        if str_num == str(captcha):
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None and user.is_staff:
                auth.login(request, user)
                return render(request, 'dashboardAdmin.html')
            elif user is not None:
                auth.login(request, user)
                return redirect('landingPageUser')
            else:
                messages.error(request, 'Credentials are incorrect. Please enter them correctly!')
                return render(request, 'index.html', context)
        else:
            messages.error(request, "Enter the captcha Correctly!")
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, "You have been successfully logged off!")
        return redirect('login_homepage')

def cart(request):
    context = {}
    items = Cart.objects.filter(user__id = request.user.id, status = False)
    context['items'] = items
    if request.method == 'POST':
        bid = request.POST['bid']
        qty = request.POST['qty']
        is_exist = Cart.objects.filter(product__id=bid, user__id=request.user.id, status=False)
        if len(is_exist)>0:
            messages.info(request, 'Item Already exist in cart')
        else:
            product = get_object_or_404(Book, id=bid)
            usr = get_object_or_404(User, id = request.user.id)
            c = Cart(user = usr, product = product, quantity = qty)
            c.save()
            messages.info(request, '{} Added in your cart.'.format(product.name))

    return render(request, 'cart.html', context)

def change_quantity(request):
    cid = request.GET['cid']
    qty = request.GET['quantity']
    cart_obj = get_object_or_404(Cart, id=cid)
    cart_obj.quantity = qty
    cart_obj.save()

    return HttpResponse(1)

# def increase_cart_data(request):
#     if request.method == 'POST':
#         items = Cart.objects.filter(user__id=request.user.id, status=False)
#         total = 0
#         for i in items:
#             total += i.product.amount
        
#         # quantity = request.POST['qty-plus']
#         cid = request.POST['cid']
#         c = Cart.objects.get(id=cid)
#         c.quantity= c.quantity+1
#         c.save()
    
#         context = {
#             'total': total,
#         }
#         return render(request, 'cart.html', context)

# def decrease_cart_data(request):
#     if request.method == 'POST':
#         items = Cart.objects.filter(user__id=request.user.id, status=False)
#         total = 0
#         quantity = 0
#         for i in items:
#             total -= i.product.amount
#             quantity -= i.quantity

#         context = {
#             'total': total,
#             'quan': quantity
#         }
#         return render(request, 'cart.html', context)

    
def remove(request, id):
    c = Cart.objects.get(id=id)
    c.delete()
    messages.info(request, '{} has been removed from your cart.'.format(c.product.name))
    return redirect('shopBooks')


def checkout(request):
    context = {}
    cart = Cart.objects.filter(user=request.user)
    total = 0
    for i in cart:
        if i.status == False:
            total += i.quantity*i.product.amount
    
    context['total'] = total
    
    context['cart'] = cart

    return render(request, 'checkout.html', context) 

def order(request):
    items = Cart.objects.filter(user_id__id=request.user.id, status=False)
    products=""
    amt=0
    cart_ids = ""
    p_ids =""

    for j in items:
        products += str(j.product.name)+"\n"
        p_ids += str(j.product.id)+","
        amt += float(j.product.amount)
        cart_ids += str(j.id)+","

    if request.method == 'POST':
        address = request.POST['address']
        contactNo = request.POST['contactNo']
        total = request.POST.get('total')
       
        # print(request.POST)

        usr = User.objects.get(id=request.user.id)
        print(usr)
        newOrder = Order(user_id=usr.id,cart_ids=cart_ids, product_ids=p_ids ,address=address, total=total, contact_number=contactNo)
        newOrder.save()

        # changing the status of order
        ord_obj = get_object_or_404(Order, id=newOrder.id)
        ord_obj.status = True
        ord_obj.save()

        # changing the status of Cart
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_obj = Cart.objects.get(id=i)
            cart_obj.status = True
            cart_obj.save()
        return render(request, 'orderBook.html')


def reportUser(request):
    context = {}
    if request.method == 'POST':
        user = request.user.id
        name = request.POST['name']
        organization = request.POST['organization']
        description = request.POST['description']

        if 'incidentPhoto' in request.FILES:
            image = request.FILES['incidentPhoto']
        else:
            image = None

        newReport = IncidentReport(user_id=user, name=name, description=description, organization=organization, upload_photo=image)
        newReport.save()
        messages.info(request, 'Incident has been successfully reported.')
    return render(request, 'reportUser.html', context)

def statusUser(request):
    context = {}

    obj = IncidentReport.objects.filter(user_id=request.user.id)
    # print(obj)
    context['incident'] = obj
    return render(request, 'statusUser.html', context)

def viewDescriptionUser(request):
    context = {}
    # incident = IncidentReport.objects.all()
    if request.method == 'POST':
        incident_id = request.POST.get('incident-id')
        # print(incident_id)
        incident = IncidentReport.objects.get(id=incident_id)
        context['incident'] = incident

    return render(request, 'viewDescriptionUser.html', context)


def contactUs(request):
    if request.method =='POST':
        name = request.POST['name']
        contact = request.POST['contact']
        message = request.POST['message']
        newContact = ContactUs(user_id=request.user.id,name=name, contactNo=contact, message=message)
        newContact.save()
        messages.info(request, 'Thank you for contacting us.')

    return render(request, 'contactUs.html')


def userProfile(request):
    context = {}    
    check = UserProfile.objects.filter(user__id=request.user.id)
    # print(check)
    if len(check)>0:
        data = UserProfile.objects.get(user__id=request.user.id)
        context['data'] = data
        # print(data)

    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']
        
        if len(check) == 0:
            createUserProfile = UserProfile.objects.create(user_id=request.user.id, name=name, contactNo=contact, address=address)
        
        dataUserProfile = UserProfile.objects.get(user__id=request.user.id)
        dataUserProfile.name = name
        dataUserProfile.contactNo = contact
        dataUserProfile.address = address
        dataUserProfile.save()
        # print(dataUserProfile)
        messages.info(request, "Changes Saved Successfully !")
        # return render(request, 'userProfile.html', context)
    return render(request, 'userProfile.html', context)

def orderStatus(request):
    context= {}
    orders = Order.objects.filter(user__id=request.user.id)
    all_orders = []

    for order in orders:
        products = []
        carts = []
        # print(order.product_ids.split(",")[:-1])
        for id in order.product_ids.split(",")[:-1]:
            try:
                product = Book.objects.get(id=id)
            except:
                product = None
            products.append(product)

        for id in order.cart_ids.split(",")[:-1]:
            quantity = Cart.objects.filter(id=id)
            carts.append(quantity)

        ord = {
            "order_id": order.id,
            "products": products,
            "status": order.status,
            "date": order.ordered_on,
            "total": order.total,
            "quantity": carts,
        }

        all_orders.append(ord)
        
        context["order_status"] = all_orders
    return render(request, 'orderStatusUser.html', context)
