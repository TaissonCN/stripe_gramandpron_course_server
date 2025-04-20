from flask import Flask, redirect
import stripe
import datetime

app = Flask(__name__)

# 🔑 SUA CHAVE DO STRIPE
stripe.api_key = "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"

# 📌 CONFIGURAÇÃO DO PLANO
PRICE_ID = "price_1REWEPGOJw1fpAx2Zpe4Ld1n"  # ID do preço semanal de 40 AUD criado no Stripe
START_DATE = datetime.datetime(2025, 5, 6)

@app.route("/")
def create_checkout():
    # Calcular a data de término após 12 semanas
    end_date = START_DATE + datetime.timedelta(weeks=12)

    # Criar uma nova sessão de pagamento
    session = stripe.checkout.Session.create(
        mode="subscription",
        success_url="https://sites.google.com/view/pronunciation-and-grammar/home",  # depois você pode mudar para sua página real
        cancel_url="https://sites.google.com/view/pronunciation-and-grammar-fail/home",
        line_items=[{
            "price": PRICE_ID,
            "quantity": 1
        }],
        subscription_data={
            "trial_end": int(START_DATE.timestamp())
        }
    )

    # Redirecionar o cliente para o link do Stripe
    return redirect(session.url, code=303)

if __name__ == "__main__":
    app.run(debug=True)
