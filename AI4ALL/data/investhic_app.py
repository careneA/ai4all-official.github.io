import streamlit as st
import pandas as pd
import numpy as np

# =====================================================
#      INVESTHIC — Ethical ESG Scoring Interface
# =====================================================

st.set_page_config(page_title="INVESTHIC — Ethical ESG Analyzer", layout="centered")

# ---- Title ----
st.title("🌱 INVESTHIC — Ethical ESG Intelligence Platform")
st.write("Enter a company name to retrieve its **Ethical ESG Score (1–10)**.")

# ---- Load ESG feature table ----
@st.cache_data
def load_esg_features():
    try:
        df = pd.read_csv("df_features_ready.csv")
        df.columns = [c.lower() for c in df.columns]
        return df
    except:
        st.error("❌ df_features_ready.csv not found. Please generate ESG features first.")
        return None

df = load_esg_features()

if df is not None and "company_name" not in df.columns:
    st.error("❌ 'company_name' missing in df_features_ready.csv.")
    st.stop()

# ---- User Input ----
company_input = st.text_input("Company Name:", "")
search_btn = st.button("🔍 Evaluate Ethical Score")

# ---- Processing ----
if search_btn:
    if not company_input.strip():
        st.warning("Please enter a company name.")
    else:
        # exact match
        matches = df[df["company_name"].str.lower() == company_input.lower().strip()]

        # fallback partial match
        if matches.empty:
            matches = df[df["company_name"].str.contains(company_input, case=False, na=False)]

        if matches.empty:
            st.error(f"❌ No ESG score found for '{company_input}'.")
        else:
            # get latest entry
            result = matches.sort_values("date").iloc[-1]

            esg_score = result.get("esg_score", None)

            if esg_score is None:
                st.error("❌ ESG score column 'esg_score' missing.")
            else:
                # ---- Convert to 1–10 Ethical Score ----
                ethical_score = round(1 + 9 * float(esg_score), 1)
                ethical_score = max(1, min(10, ethical_score))  # clamp to [1,10]

                # ---- Display Score ----
                st.subheader(f"Ethical ESG Score for **{result['company_name']}**")
                st.metric("🌍 Ethical Score (1–10)", ethical_score)

                # ---- Interpretation ----
                st.write("---")

                if ethical_score >= 8.5:
                    st.success("🟩 **Highly Ethical** — strong sustainability, transparency, and governance.")
                elif ethical_score >= 6.5:
                    st.info("🟦 **Moderately Ethical** — responsible practices with some room for growth.")
                elif ethical_score >= 4.5:
                    st.warning("🟨 **Ethical Concerns** — inconsistent or weak ESG commitment.")
                else:
                    st.error("🟥 **Low Ethical Score** — significant ethical or ESG risks identified.")

                # ---- Full Data Row ----
                with st.expander("Show Full ESG Data Row"):
                    st.dataframe(result.to_frame().T, use_container_width=True)
