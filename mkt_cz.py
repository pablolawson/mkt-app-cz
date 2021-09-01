import streamlit as st
import pandas as pd




facturacion = st.sidebar.number_input("¿Cuál es tu facturación mensual aproximada?", 50000)
inversion= st.sidebar.number_input("¿Cuánto estas dispuesto a invertir mensualmente en publicidad?", 5000)

tacos_obj = round(inversion / facturacion * 100, 2)

st.write("Equivale a un TACOS objetivo del (%):")
st.write(tacos_obj)


ticket = st.sidebar.number_input("¿Cuál es tu ticket promedio?", 500)

df = pd.read_csv('MELIMLA.csv')

categoria = df['root_category_id']

make_choice = st.sidebar.selectbox('¿Cuál es tu categría principal?:', categoria)

st.title("CPC")
st.write("Según tu ticket promedio y tu categoría, tu costo por click (CPC) estaría entre ($):")
cpc = df[df['root_category_id'] == make_choice]['CPC']
ticket_cat = df[df['root_category_id'] == make_choice]['TICKET']
cpc_min = round(cpc / ticket_cat * ticket * 0.8, 0)
cpc_max = round(cpc / ticket_cat * ticket * 1.2, 0)
st.write(cpc_min) 
st.write(cpc_max) 

st.title("Clicks")
st.write("Con tu presupuesto podrías comprar entre (clicks)")
clicks_max = round(inversion / cpc_max, 0)
clicks_min = round(inversion / cpc_min, 0)
st.write(clicks_max)
st.write(clicks_min) 

st.title("SIN HACER PUBLICIDAD")
st.write("SIN publicidad estos clicks te generarían entre (ventas)")
sales_org_min = clicks_min / df[df['root_category_id'] == make_choice]['VTS ORG']
sales_org_max = clicks_max / df[df['root_category_id'] == make_choice]['VTS ORG']
st.write(round(sales_org_max, 0)) 
st.write(round(sales_org_min, 0))

st.write("SIN publicidad estos clicks te generarían entre (ingresos $)")
amount_org_min = sales_org_max * ticket
amount_org_max = sales_org_min * ticket
st.write(round(amount_org_min, 0)) 
st.write(round(amount_org_max, 0))

st.title("HACIENDO PUBLICIDAD")
st.write("CON publicidad estos clicks te generarían entre (ventas)")
sales_ads_min = clicks_min / df[df['root_category_id'] == make_choice]['VTS ADS']
sales_ads_max = clicks_max / df[df['root_category_id'] == make_choice]['VTS ADS']
st.write(round(sales_ads_max, 0)) 
st.write(round(sales_ads_min, 0))

st.write("CON publicidad estos clicks te generarían entre (ingresos $)")
amount_ads_min = sales_ads_max * ticket
amount_ads_max = sales_ads_min * ticket
st.write(round(amount_ads_min, 0)) 
st.write(round(amount_ads_max, 0))

st.title("ACOS")
st.write("Tu ACOS (Inversion en publicidad / Ingresos generados por publicidad) sería del (%):")
acos_min = round(inversion / amount_ads_min * 100, 0)
acos_max = round(inversion / amount_ads_max * 100, 0)
st.write(acos_max)
st.write(acos_min) 


st.title("ROI")
st.write("El retorno sobre cada peso invertido en publicidad sería de ($):")
roi_min = 1/acos_min*100
roi_max = 1/acos_max*100
st.write(round(roi_min, 0)) 
st.write(round(roi_max, 0))




st.write("Datos de mercado")
st.write(df)