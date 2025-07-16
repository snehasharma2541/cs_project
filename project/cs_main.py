import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

try:
    with open('./savedModels/catboost_model.pkl', 'rb') as file:
        model = pkl.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please check the path and ensure the model is trained and saved.")
    st.stop()


st.set_page_config(page_title="Cyber Sentinel", layout="centered")
st.title("🛡️ Cyber Sentinel")
st.subheader("🔍 Predict whether a website is **Phishing or Legitimate**")

st.markdown("""
This intelligent tool uses a **CatBoost Machine Learning Model** to analyze website features and detect phishing attempts. 
""")

with st.form("input_form"):
    st.write("### 📝 Enter Website Characteristics")

    input_data = {
        "having_ip_address": st.selectbox("1. Having IP Address", [-1, 1]),
        "url_length": st.selectbox("2. URL Length", [-1, 0, 1]),
        "shortining_service": st.selectbox("3. Shortening Service", [-1, 1]),
        "having_at_symbol": st.selectbox("4. '@' Symbol Present", [-1, 1]),
        "double_slash_redirecting": st.selectbox("5. Double Slash Redirecting", [-1, 1]),
        "prefix_suffix": st.selectbox("6. Prefix/Suffix in Domain", [-1, 1]),
        "having_sub_domain": st.selectbox("7. Having Subdomain", [-1, 0, 1]),
        "sslfinal_state": st.selectbox("8. SSL Final State", [-1, 0, 1]),
        "domain_registeration_length": st.selectbox("9. Domain Registration Length", [-1, 1]),
        "favicon": st.selectbox("10. Favicon", [-1, 1]),
        "port": st.selectbox("11. Non-standard Port", [-1, 1]),
        "https_token": st.selectbox("12. HTTPS Token in URL", [-1, 1]),
        "request_url": st.selectbox("13. Request URL", [-1, 1]),
        "url_of_anchor": st.selectbox("14. URL of Anchor", [-1, 0, 1]),
        "links_in_tags": st.selectbox("15. Links in Tags", [-1, 0, 1]),
        "sfh": st.selectbox("16. Server Form Handler", [-1, 1]),
        "submitting_to_email": st.selectbox("17. Submitting to Email", [-1, 1]),
        "abnormal_url": st.selectbox("18. Abnormal URL", [-1, 1]),
        "redirect": st.selectbox("19. Redirect", [0, 1]),
        "on_mouseover": st.selectbox("20. On Mouseover", [0, 1]),
        "rightclick": st.selectbox("21. Right Click Disabled", [0, 1]),
        "popupwidnow": st.selectbox("22. Pop-up Window", [0, 1]),
        "iframe": st.selectbox("23. IFrame Redirection", [0, 1]),
        "age_of_domain": st.selectbox("24. Age of Domain", [-1, 1]),
        "dnsrecord": st.selectbox("25. DNS Record Available", [-1, 1]),
        "web_traffic": st.selectbox("26. Web Traffic", [-1, 0, 1]),
        "page_rank": st.selectbox("27. Page Rank", [-1, 0, 1]),
        "google_index": st.selectbox("28. Google Index", [-1, 1]),
        "links_pointing_to_page": st.selectbox("29. Links Pointing to Page", [0, 1]),
        "statistical_report": st.selectbox("30. Statistical Report", [-1, 1]),
    }

    submit = st.form_submit_button("🚀 Predict")


if submit:
    demo_input = pd.DataFrame([list(input_data.values())], columns=input_data.keys())
    prediction = model.predict(demo_input)[0]
    proba = model.predict_proba(demo_input)[0]

    result_text = "🟢 Legitimate Website" if prediction == 1 else "🔴 Phishing Website"
    confidence = round(max(proba) * 100, 2)

    st.markdown("### 🔍 Prediction Result:")
    st.success(result_text)
    st.markdown(f"**Confidence:** `{confidence}%`")

