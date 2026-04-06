from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cart')
def cart_page():
    cart = [
        {"item": "Kitob",  "qty": 2, "price": 35000},
        {"item": "Qalam",  "qty": 5, "price": 3000},
        {"item": "Daftar", "qty": 3, "price": 8000},
    ]

    # umumiy summa hisoblash
    total_sum = sum(item["qty"] * item["price"] for item in cart)

    return render_template("cart.html", cart=cart, total_sum=total_sum)

if __name__ == '__main__':
    app.run(debug=True)
