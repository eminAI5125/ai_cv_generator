import streamlit as st
import openai
import time

# OpenAI API Anahtarını Kullan
client = openai.OpenAI(api_key="sk-proj-AYlZGwk0dprjOOrR-WPhyqbGE4wFLR3Bdi5k6lJlx82m0DS0WIznGNalb2NyNjM5_6ZJDHmtEST3BlbkFJRc6vrCi-zSQ4ZhoLGM_9v4D8ZOlBiRyU3XNmgLE98wt4-8io_a65fPOZMD5fIRpoRLptzU60sA") 

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
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen profesyonel bir CV ve motivasyon mektubu oluşturma asistanısın."},
                {"role": "user", "content": f"Bir {job_title} pozisyonuna başvuran bir aday için mükemmel bir CV ve motivasyon mektubu hazırla. Adı: {name}, Yetenekleri: {skills}, Şirket: {company}. Motivasyon mektubu kısa ve etkileyici olsun."}
            ]
        )
        
        ai_generated_text = response.choices[0].message.content
        
        st.success("✅ CV ve Motivasyon Mektubu Başarıyla Oluşturuldu!")
        st.text_area("📄 CV ve Motivasyon Mektubu", value=ai_generated_text, height=300)
