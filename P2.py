import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\PROJECT\\Environmental_Effects_2020_2030.csv")


st.set_page_config(page_title=" Environmental Dashboard", layout="wide")
st.title(" Environmental Effects Dashboard (2020–2030)")


st.sidebar.header(" Filter Options")


time_range = st.sidebar.radio("Select Time Period:",
                              ["Past (2020–2024)", "Present (2025)", "Future (2026–2030)"])

if time_range == "Past (2020–2024)":
    filtered_df = df[(df["Year"] >= 2020) & (df["Year"] <= 2024)]
elif time_range == "Present (2025)":
    filtered_df = df[df["Year"] == 2025]
else:
    filtered_df = df[(df["Year"] >= 2026) & (df["Year"] <= 2030)]


sectors = [col for col in df.columns if col != "Year"]
selected_sector = st.sidebar.selectbox("Select Sector to Analyze:", sectors)


chart_type = st.sidebar.selectbox("Select Chart Type:",
                                   ["Line Chart", "Bar Chart", "Histogram", "Pie Chart"])


st.subheader(f"{chart_type} for {selected_sector} during {time_range}")


if chart_type == "Line Chart":
    st.line_chart(filtered_df.set_index("Year")[selected_sector])


elif chart_type == "Bar Chart":
    st.bar_chart(filtered_df.set_index("Year")[selected_sector])


elif chart_type == "Histogram":
    fig, ax = plt.subplots()
    ax.hist(filtered_df[selected_sector], bins=10, color='lightgreen', edgecolor='black')
    ax.set_xlabel(selected_sector)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {selected_sector}")
    st.pyplot(fig)


elif chart_type == "Pie Chart":
    pie_data = filtered_df.groupby("Year")[selected_sector].sum()
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(f"Pie Chart of {selected_sector} over {time_range}")
    st.pyplot(fig)


with st.expander(" View Raw Data"):
    st.dataframe(filtered_df)
