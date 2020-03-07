from django.shortcuts import render
from django.http import JsonResponse
import stripe
import json
stripe_pub="pk_test_2iZBcGyFUStxvDeB0lWBEN1a00JDgO0e0X"
stripe_private="sk_test_6SDJC1aGmvUGnAo35B3TA96d00RdQhST4h"
stripe.api_key=stripe_private


#levantar el formulario de Stripe
def home(request):
    return render(request, "home.html",{'key':stripe_pub})

#Este es el primer checout que se debe mostrar para que devuelva
# todos los datos de lac arga - CHARGE 

def checkout(request):
    amount =500
    customer = stripe.Customer.create(
        email = request.POST ['stripeEmail'],
        source = request.POST ['stripeToken']
    )

    charge =stripe.Charge.create(
        customer = customer.id,
        amount = amount,
        currency = 'aud',
        description ='Venta de prueba en Ventanilla'
    )
    print("status",charge)
    # return render (request,"exito.html")
    return JsonResponse(charge)


# Create your views here.
