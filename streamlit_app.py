import streamlit as st
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=1000, key="daterefresh")
st.set_page_config(page_title="Nuestra Historia ❤️", page_icon="❤️")

# 1. CAMBIA TU FECHA AQUÍ (Año, Mes, Día, Hora, Minuto, Segundo)
FECHA_ANIVERSARIO = datetime(2026, 6, 1, 2, 7, 30) 

# 2. CAMBIA O AGREGA TUS FRASES AQUÍ
MENSAJITOS = [
     "Eres mi persona favorita en todo el universo.",
       "Gracias por hacerme sonreír incluso en los días difíciles.",
       "Solo piensoen ti.",
       "¿Ya te dije hoy que eres lo mejor que me ha pasado?",
       "Eres mi hogar y mi lugar seguro.",
       "Cada segundo a tu lado vale la pena por completo.",
       "Un recordatorio de que te amo más que ayer, pero menos que mañana.",
       "Contigo quiero todo.",
       "Me encantas completita, de la cabeza a los pies.",
       "Soy la mas afortunada de tenerte.",
       "Mis mamis.",
       "Eres mi primer pensamiento al despertar.",
       "Estoy muy enamorada de ti.",
       "Gracias por nunca rendirte conmigo.",
       "Quiero que siempre estes en mi vida.",
       "Gracias por amarme.",
       "Tu forma de ser me vuelve loca.",
       "Eres la mas hermosa.",
       "solterita?",
       "Me gusta todo de ti.",
       "Gracias por ser mi novia, mi confidente y mi mejor amiga."
   ]
if "nota_actual" not in st.session_state:
    st.session_state.nota_actual = "Haz clic abajo para leer..."

st.markdown("<h2 style='text-align: center; color: #6d4c41; font-family: sans-serif;'>El tiempo que llevo siendo la más feliz a tu lado: ✨</h2>", unsafe_allow_html=True)

ahora = datetime.now()
diferencia = ahora - FECHA_ANIVERSARIO
dias = diferencia.days
horas, resto = divmod(diferencia.seconds, 3600)
minutos, segundos = divmod(resto, 60)

texto_reloj = f"{dias} días, {horas}h, {minutos}m y {segundos}s"
st.markdown(f"<h1 style='text-align: center; color: #d81b60; font-family: sans-serif; font-size: 32px;'>{texto_reloj} ❤️</h1>", unsafe_allow_html=True)

st.write("")
st.write("¿Me extrañas o necesitas una sonrisa? Presiona aquí abajo: ⬇️")

if st.button("Abrir una nota de amor 💌", use_container_width=True):
    st.session_state.nota_actual = random.choice(MENSAJITOS)
    st.balloons()

st.success(st.session_state.nota_actual)
