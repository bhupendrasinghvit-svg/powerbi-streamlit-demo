import streamlit as st

st.set_page_config(page_title="Power BI Context")

st.title("Power BI Context Parameters")

# Read URL parameters
params = st.query_params

brand = params.get("Brand", "")
pharmacy = params.get("Pharmacy", "")
kpi = params.get("KPI", "")

st.write("Brand:", brand)
st.write("Pharmacy:", pharmacy)
st.write("KPI:", kpi)

if brand:
    st.success(f"Selected Brand: {brand}")

if pharmacy:
    st.success(f"Selected Pharmacy: {pharmacy}")

if kpi:
    st.success(f"Selected KPI: {kpi}")