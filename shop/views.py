from django.shortcuts import render, get_object_or_404, redirect
from core.models import RentalProduct  # Import model RentalProduct dari core.models

def checkout(request):
    # Ambil data cart dari session
    cart = request.session.get('cart', {})
    cart_items = []

    # Hitung total harga dan siapkan data untuk template
    total_price = 0
    for product_id, details in cart.items():
        try:
            total_price += float(details['price']) * details['quantity']  # Gunakan kunci 'price'
            cart_items.append({
                'name': details['name'],
                'quantity': details['quantity'],
                'total_price': float(details['price']) * details['quantity'],
            })
        except KeyError as e:
            print(f"KeyError: {e}")  # Debugging jika ada kunci yang salah
            continue

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
def product_list(request):
    products = RentalProduct.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def add_to_cart(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(RentalProduct, id=product_id)
    
    # Ambil keranjang dari session atau buat keranjang baru
    cart = request.session.get('cart', {})

    # Tambahkan produk ke keranjang
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'quantity': 1,
            'name': product.name,
            'price': float(product.daily_rental_price),  # Harga produk
        }

    # Simpan kembali ke session
    request.session['cart'] = cart
    request.session.modified = True  # Tandai bahwa session telah berubah
    print("Cart contents:", request.session.get('cart'))
    return redirect('shop:product_list')



def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, details in cart.items():
        try:
            total_price += details['price'] * details['quantity']
            cart_items.append({
                'product_id': product_id,
                'name': details['name'],
                'quantity': details['quantity'],
                'price': details['price'],
                'total_price': details['price'] * details['quantity'],
            })
        except KeyError:
            continue  # Abaikan jika struktur data salah

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] = quantity
            request.session['cart'] = cart

    return redirect('shop:view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    # Hapus item dari keranjang jika ada
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        request.session.modified = True  # Tandai session sebagai berubah

    return redirect('shop:view_cart')

def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('shop:product_list')