import streamlit as st
import pandas as pd

st.title("📊 AI Social Media Report Generator")

uploaded_file = st.file_uploader(
    "Upload Instagram CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file, header=1)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Convert metrics to numeric
    df["Likes"] = pd.to_numeric(df["Likes"], errors="coerce")
    df["Comments"] = pd.to_numeric(df["Comments"], errors="coerce")
    df["Shares"] = pd.to_numeric(df["Shares"], errors="coerce")

    # Engagement Score
    df["Engagement Score"] = (
        df["Likes"].fillna(0)
        + df["Comments"].fillna(0)
        + df["Shares"].fillna(0)
    )

    best_post = df.loc[df["Engagement Score"].idxmax()]
    worst_post = df.loc[df["Engagement Score"].idxmin()]

    st.subheader("🏆 Best Performing Post")

    st.write("Date:", best_post["Date"])
    st.write("Content Type:", best_post["Type of Content"])
    st.write("Engagement Score:", int(best_post["Engagement Score"]))

    st.subheader("📉 Lowest Performing Post")

    st.write("Date:", worst_post["Date"])
    st.write("Content Type:", worst_post["Type of Content"])
    st.write("Engagement Score:", int(worst_post["Engagement Score"]))

    st.subheader("📈 Content Performance")

    content_summary = (
        df.groupby("Type of Content")["Engagement Score"]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(content_summary)

    st.subheader("🤖 AI Insight")

    top_content = content_summary.index[0]

    st.success(
        f"The best performing content category is '{top_content}'. "
        f"Focus more on this content type to improve engagement."
    )
