import streamlit as st
import google.generativeai as genai
import time

# Google Gemini API Anahtarını Kullan
genai.configure(api_key="AIzaSyCAIK9I1yhha4Na3e9Y7EWoxJjy8axr4DM")  

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
        
        # Google Gemini API ile CV & Motivasyon Mektubu Üret
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Bir {job_title} pozisyonuna başvuran bir aday için mükemmel bir CV ve motivasyon mektubu hazırla. Adı: {name}, Yetenekleri: {skills}, Şirket: {company}. Motivasyon mektubu kısa ve etkileyici olsun.")

        ai_generated_text = response.text  # Google Gemini'nin oluşturduğu içerik
        
        st.success("✅ CV ve Motivasyon Mektubu Başarıyla Oluşturuldu!")
        st.text_area("📄 CV ve Motivasyon Mektubu", value=ai_generated_text, height=300)
