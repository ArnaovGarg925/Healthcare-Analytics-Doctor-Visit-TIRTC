import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Healthcare Analytics – Doctor Visits", page_icon="🏥", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/doctor_visits.csv")
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    df["age_years"] = df["age"] * 100
    df["age_group"] = pd.cut(
        df["age_years"], bins=[0,18,30,45,60,80,100],
        labels=["0-18","19-30","31-45","46-60","61-80","81+"],
        include_lowest=True
    )
    df["insurance_status"] = np.select(
        [df["private"].eq("yes"), df["freepoor"].eq("yes"), df["freerepat"].eq("yes")],
        ["Private","Free/poor","Free/repat"], default="None"
    )
    return df

df = load_data()
st.title("🏥 Healthcare Analytics for Doctor Visits")
st.caption("TIRTC DIY Project | Data-driven exploration of doctor-visit patterns")

# Sidebar filters
st.sidebar.header("Filters")
gender = st.sidebar.multiselect("Gender", sorted(df.gender.unique()), default=sorted(df.gender.unique()))
health = st.sidebar.multiselect("Health score", sorted(df.health.unique()), default=sorted(df.health.unique()))
insurance = st.sidebar.multiselect("Coverage", sorted(df.insurance_status.unique()), default=sorted(df.insurance_status.unique()))

f = df[df.gender.isin(gender) & df.health.isin(health) & df.insurance_status.isin(insurance)]

c1,c2,c3,c4 = st.columns(4)
c1.metric("Records", f"{len(f):,}")
c2.metric("Total visits", f"{int(f.visits.sum()):,}")
c3.metric("Average visits / record", f"{f.visits.mean():.2f}" if len(f) else "0")
c4.metric("Records with ≥2 visits", f"{(f.visits.ge(2).mean()*100):.1f}%" if len(f) else "0%")

st.divider()
left,right = st.columns(2)

with left:
    g = f.groupby("gender", as_index=False)["visits"].sum()
    st.plotly_chart(px.bar(g, x="gender", y="visits", title="Total Visits by Gender", text_auto=True), use_container_width=True)

with right:
    a = f.groupby("age_group", observed=True, as_index=False)["visits"].sum()
    st.plotly_chart(px.bar(a, x="age_group", y="visits", title="Total Visits by Age Group", text_auto=True), use_container_width=True)

left,right = st.columns(2)
with left:
    i = f.groupby("illness", as_index=False)["visits"].mean()
    st.plotly_chart(px.line(i, x="illness", y="visits", markers=True, title="Average Visits vs Illness Count"), use_container_width=True)

with right:
    h = f.groupby("health", as_index=False)["visits"].mean()
    st.plotly_chart(px.line(h, x="health", y="visits", markers=True, title="Average Visits vs Health Score"), use_container_width=True)

st.subheader("Coverage distribution")
cov = f["insurance_status"].value_counts().reset_index()
cov.columns = ["coverage","records"]
st.plotly_chart(px.pie(cov, names="coverage", values="records", hole=.35), use_container_width=True)

st.subheader("Filtered data")
st.dataframe(f, use_container_width=True, height=320)

st.info("This project is for analytics and educational use. It identifies patterns in the supplied dataset; it does not diagnose patients or recommend medical treatment.")
