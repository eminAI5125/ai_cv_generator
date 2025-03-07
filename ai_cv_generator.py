import streamlit as st
import openai
import stripe
import time

# OpenAI API Anahtarını Yükle
openai.api_key = "YOUR_OPENAI_API_KEY"

# Stripe Ödeme Entegrasyonu
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

st.title("📄 AI Destekli Otomatik CV & Motivasyon Mektubu Oluşturucu")

# Kullanıcıdan Bilgileri Al
name = st.text_input("Adınız ve Soyadınız")
email = st.text_input("E-posta Adresiniz")
job_title = st.text_input("Başvurduğunuz Pozisyon")
skills = st.text_area("Yetenekleriniz ve Deneyimleriniz")
company = st.text_input("Başvurulan Şirket")
custom_message = st.text_area("Özel Mesaj veya Talepler")

if st.button("📥 CV & Motivasyon Mektubunu Oluştur"):
    with st.spinner("AI sizin için mükemmel bir CV ve motivasyon mektubu oluşturuyor..."):
        time.sleep(3)
        
        # OpenAI API ile CV & Motivasyon Mektubu Üret
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen profesyonel bir CV ve motivasyon mektubu oluşturma asistanısın."},
                {"role": "user", "content": f"Bir {job_title} pozisyonuna başvuran bir aday için mükemmel bir CV ve motivasyon mektubu hazırla. Adı: {name}, Yetenekleri: {skills}, Şirket: {company}. Motivasyon mektubu kısa ve etkileyici olsun."}
            ]
        )
        
        ai_generated_text = response["choices"][0]["message"]["content"]
        
        st.success("✅ CV ve Motivasyon Mektubu Başarıyla Oluşturuldu!")
        st.text_area("📄 CV ve Motivasyon Mektubu", value=ai_generated_text, height=300)
        
        # Ödeme Sistemi
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "AI Destekli CV & Motivasyon Mektubu"
                        },
                        "unit_amount": 990,
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="https://yourwebsite.com/success",
            cancel_url="https://yourwebsite.com/cancel",
        )
        
        st.markdown(f"[💳 Ödeme Yap ve Belgeni Al]({checkout_session.url})", unsafe_allow_html=True)
