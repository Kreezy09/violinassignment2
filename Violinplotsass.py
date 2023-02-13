import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
data_all = pd.read_csv('gapminder_with_codes.csv')
data = data_all[data_all['year']==2007]


df = pd.DataFrame(data)

# Create a function to plot the violin plots
def plot_violin_plots(df):
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 5))

    plt.subplot(131)
    sns.violinplot(x='lifeExp', data=df)
    plt.title('Life Expectancy')
    # st.pyp
    plt.subplot(132)
    sns.violinplot(x='pop', data=df)
    plt.title('Population')
    # st.pyplot(plt)


    plt.subplot(133)
    sns.violinplot(x='gdpPercap', data=df)
    plt.title('GDP per capita')
    st.pyplot(plt)

    plt.tight_layout()
    plt.show()

# Use Streamlit to present the data
st.title("Keith Mwaniki Kareithi\nSCT211-0021/2021\nViolin Plots")
plot_violin_plots(df)