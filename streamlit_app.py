import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sorted_data = pd.read_csv('data/sorted_data.csv')
category_customer_count = pd.read_csv('/workspaces/blank-app/data/data/category_customer_count.csv')


# Dashboard Title
st.title("E-commerce Dashboard")

# Section 1: Cities with the Lowest Total Orders
st.header("1. Cities with the Lowest Total Orders")

# Plotting bar chart for cities with lowest sales
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 5))
colors = sns.color_palette("Blues", len(sorted_data))
bars = ax.barh(sorted_data['geolocation_city'], sorted_data['total_orders'], color=colors)

# Add labels to bars
for bar in bars:
    ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.1f}', va='center', fontsize=10)

# Titles and labels
ax.set_xlabel('Total Orders', fontsize=12)
ax.set_ylabel('Geolocation City', fontsize=12)
ax.set_title('Cities with the Lowest Total Orders', fontsize=14)

# Display the chart in Streamlit
st.pyplot(fig)

# Insight for section 1
st.markdown("""
**Insight**: Data diolah untuk menunjukkan total pesanan per lokasi, dan sepuluh lokasi dengan penjualan terendah divisualisasikan dalam bentuk diagram batang.
""")

# Section 2: Product Categories with the Lowest Number of Buyers
st.header("2. 10 Kategori Produk dengan Jumlah Pembeli Terendah")

# Plotting bar chart for product categories with lowest buyers
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='customer_id', y='product_category_name_english', data=category_customer_count.head(10), palette='coolwarm', ax=ax2)
ax2.set_title('10 Kategori Produk dengan Jumlah Pembeli Terendah', fontsize=14)
ax2.set_xlabel('Jumlah Pembeli', fontsize=12)
ax2.set_ylabel('Kategori Produk', fontsize=12)

# Display the chart in Streamlit
st.pyplot(fig2)

# Insight for section 2
st.markdown("""
**Insight**: Visualisasi menampilkan 10 kategori produk dengan jumlah pembeli terendah, menunjukkan bahwa beberapa kategori produk kurang diminati oleh konsumen.
""")

# Conclusion
st.header("Kesimpulan")

st.markdown("""
- Dari hasil visualisasi pertama, data di-group berdasarkan kota dan total pesanan dijumlahkan untuk setiap kota. Sepuluh kota dengan pesanan terendah disortir, dan divisualisasikan menggunakan diagram batang.
- Dari hasil visualisasi kedua, menampilkan 10 kategori produk dengan jumlah pembeli terendah, menunjukkan bahwa beberapa kategori produk kurang diminati oleh konsumen. Kategori produk dengan jumlah pembeli terendah adalah "security and services".
""")
