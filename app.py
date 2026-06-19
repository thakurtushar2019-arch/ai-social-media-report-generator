import streamlit as st
import pandas as pd

st.title("📊 AI Social Media Report Generator")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    df["Engagement Rate"] = (
        (df["Likes"] +
         df["Comments"] +
         df["Shares"])
        / df["Views"]
    ) * 100

    best_post = df.loc[
        df["Engagement Rate"].idxmax()
    ]

    worst_post = df.loc[
        df["Engagement Rate"].idxmin()
    ]

    st.subheader("🏆 Best Performing Post")

    st.write(
        best_post["Post Name"]
    )

    st.write(
        f"Engagement Rate: {best_post['Engagement Rate']:.2f}%"
    )

    st.subheader("📉 Worst Performing Post")

    st.write(
        worst_post["Post Name"]
    )

    st.write(
        f"Engagement Rate: {worst_post['Engagement Rate']:.2f}%"
    )

    st.subheader("📈 Overall Insights")

    avg_rate = df["Engagement Rate"].mean()

    st.write(
        f"Average Engagement Rate: {avg_rate:.2f}%"
    )

    st.bar_chart(
        df.set_index("Post Name")["Engagement Rate"]
    )
