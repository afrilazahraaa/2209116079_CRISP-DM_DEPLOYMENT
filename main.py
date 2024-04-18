import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.title('Pizza Sales Analysis & Prediction')

url = 'data_cleaned.csv'
df = pd.read_csv(url)

st.subheader("Dataset")
st.write(df.head(5))
# Function to calculate and display percentage
def display_percentage(column_name, counts):
    total = sum(counts)
    percentages = [(count / total) * 100 for count in counts]
    st.write(f"{column_name} Percentages:")
    for value, percentage in zip(counts.index, percentages):
        st.write(f"- {value}: {percentage:.1f}%")

st.subheader("Kuantitas")
quantity_counts = df['quantity'].value_counts()
quantity_fig = plt.figure()
quantity_hist = plt.hist(df['quantity'], bins=20, edgecolor='black')
plt.xlabel('Kuantitas')
plt.ylabel('Jumlah')
st.pyplot(quantity_fig)
display_percentage("Quantity", quantity_counts)
st.write("1. Sebagian besar pembelian pizza adalah satu pizza (98.1%), menunjukkan bahwa mayoritas pelanggan melakukan pembelian tunggal.")
st.write("2. Meskipun mayoritas pembelian adalah satu pizza, sebagian kecil pelanggan juga melakukan pembelian lebih dari satu pizza dalam satu transaksi (1.9% untuk 2 pizza).")
st.write("3. Tidak ada transaksi yang mencakup pembelian 3 atau 4 pizza, menunjukkan bahwa pembelian dalam jumlah besar tidak umum.")

st.header("Total harga per unit")
st.subheader("Total harga per unit")
unit_price_counts = pd.cut(df['unit_price'], bins=5).value_counts().sort_index()
unit_price_fig = plt.figure()
unit_price_hist = plt.hist(df['unit_price'], bins=20, edgecolor='black')
plt.xlabel('Total harga per unit')
plt.ylabel('Frequency')
st.pyplot(unit_price_fig)
display_percentage("Unit Price", unit_price_counts)
st.write("Interpretasi dan Insight:")
st.write("- Mayoritas harga unit pizza berada dalam kisaran (14.99, 20.23], dengan persentase sebesar 36.3%. Hal ini menunjukkan bahwa harga yang paling umum adalah di kisaran ini.")
st.write("- Sekitar 32.9% harga unit pizza berada dalam kisaran (9.724, 14.99], sementara 29.6% berada dalam kisaran (20.23, 25.47]. Ini menunjukkan bahwa sebagian besar harga berada di rentang menengah.")
st.write("- Harga unit pizza di atas $25 cukup jarang, dengan hanya sekitar 1.2% dari total transaksi yang berada dalam kisaran (25.47, 35.95]. Ini menunjukkan bahwa pizza dengan harga premium kurang diminati.")
st.write("- Insight actionable: Untuk meningkatkan penjualan, fokus pada pemasaran dan promosi untuk produk dengan harga unit di kisaran mayoritas (14.99-20.23), namun juga perhatikan segmen harga di bawah dan di atas kisaran ini untuk melengkapi portofolio produk Anda. Kemungkinan juga untuk mengevaluasi strategi harga untuk produk premium.")


st.header("Total Harga")
st.subheader("Total Harga")
total_price_counts = pd.cut(df['total_price'], bins=5).value_counts().sort_index()
total_price_fig = plt.figure()
total_price_hist = plt.hist(df['total_price'], bins=20, edgecolor='black')
plt.xlabel('Total Harga')
plt.ylabel('Jumlah')
st.pyplot(total_price_fig)
display_percentage("Total Price", total_price_counts)
st.write("- Mayoritas total harga transaksi (97.3%) berada dalam kisaran (9.677, 24.4], menunjukkan bahwa sebagian besar pembelian pizza memiliki nilai transaksi yang relatif rendah.")
st.write("- Meskipun sebagian besar transaksi berada dalam kisaran harga yang rendah, sekitar 2.7% transaksi memiliki total harga di atas kisaran ini, menunjukkan adanya peluang untuk meningkatkan penjualan produk dengan harga lebih tinggi.")
st.write("- Transaksi dengan total harga di atas $39 cukup jarang, dengan hanya sekitar 0.6% dari total transaksi yang berada dalam kisaran (39.05, 53.7]. Hal ini mungkin menunjukkan bahwa pizza dengan harga premium kurang diminati.")
st.write("- Insight actionable: Fokus pada strategi pemasaran dan promosi untuk produk dengan total harga di kisaran mayoritas (9.677-24.4), namun juga perhatikan segmen harga di atas kisaran ini untuk meningkatkan penjualan produk dengan harga lebih tinggi. Evaluasi strategi harga untuk produk premium juga bisa dilakukan untuk menarik lebih banyak pelanggan.")

st.subheader("Ukuran Pizza")
size_cols = ['pizza_size_L', 'pizza_size_M', 'pizza_size_S', 'pizza_size_XL', 'pizza_size_XXL']
size_counts = df[size_cols].sum()
size_fig = plt.figure()
size_bar = plt.bar(size_counts.index, size_counts.values)
plt.xlabel('Ukuran Pizza')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
st.pyplot(size_fig)
display_percentage("Pizza Size", size_counts)
st.write("- Pizza dengan ukuran L (Large) merupakan pilihan yang paling populer dengan persentase sebesar 38.1%, diikuti oleh ukuran M (Medium) dengan persentase 31.6%, dan ukuran S (Small) dengan persentase 29.1%. Hal ini menunjukkan bahwa mayoritas pelanggan lebih memilih ukuran pizza yang lebih besar.")
st.write("- Meskipun ukuran pizza L, M, dan S menjadi pilihan utama, ada potensi untuk meningkatkan penjualan untuk ukuran pizza dengan potensi rendah seperti XL (Extra Large) dan XXL (Extra Extra Large). Dengan hanya 1.1% dan 0.1% dari total penjualan, mungkin ada peluang untuk memperkenalkan promosi atau penawaran khusus untuk ukuran pizza yang lebih besar ini.")
st.write("- Jika pizza dengan ukuran XL dan XXL dianggap sebagai produk premium dengan harga yang lebih tinggi, perusahaan dapat mengevaluasi strategi pemasaran dan promosi khusus untuk menarik lebih banyak pelanggan ke segmen ini. Ini dapat mencakup penawaran bundel dengan produk lain, promosi diskon, atau promosi eksklusif untuk anggota setia.")
st.write("- Selain itu, evaluasi kembali aspek produksi dan biaya untuk pizza ukuran XL dan XXL juga dapat membantu memastikan keuntungan yang sehat dari penjualan produk dengan margin keuntungan yang lebih tinggi.")

st.subheader("Kategori Pizza")
category_cols = ['pizza_category_Chicken', 'pizza_category_Classic', 'pizza_category_Supreme', 'pizza_category_Veggie']
category_counts = df[category_cols].sum()
category_fig = plt.figure()
category_pie = plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
st.pyplot(category_fig)
display_percentage("Pizza Category", category_counts)
st.write("- Kategori pizza yang paling populer adalah Classic dengan persentase 30.0%, diikuti oleh Supreme dengan 24.2%, Chicken dengan 22.2%, dan Veggie dengan 23.5%. Hal ini menunjukkan bahwa variasi klasik dan premium seperti Supreme sangat diminati oleh pelanggan.")
st.write("- Meskipun kategori Classic mendominasi dalam persentase, potensi peningkatan penjualan mungkin dapat ditemukan dalam kategori lain seperti Chicken dan Veggie. Dengan hanya 22.2% dan 23.5% dari total penjualan, ada peluang untuk meningkatkan visibilitas dan popularitas produk-produk ini melalui promosi dan strategi pemasaran yang lebih agresif.")
st.write("- Untuk kategori Supreme yang memiliki persentase yang signifikan, strategi yang efektif adalah mempertahankan kualitas dan keunikan produk ini untuk mempertahankan minat pelanggan. Penawaran bundel dengan kategori lain atau penawaran spesial untuk kategori Supreme juga dapat meningkatkan penjualan produk ini.")
st.write("- Selain itu, memantau tren dan preferensi pelanggan serta menyediakan variasi menu yang inovatif dalam setiap kategori dapat membantu mempertahankan minat pelanggan dan memperluas pangsa pasar.")

st.subheader("Prediksi Kuantitas")

file_path = 'gnb_model.pkl'
clf = joblib.load(file_path)

# Define function to preprocess input data
def preprocess_input(unit_price, total_price, pizza_size, pizza_category):
    input_data = {
        'unit_price': [unit_price],
        'total_price': [total_price],
        'pizza_size_L': [pizza_size == 'Pizza Size L (Large)'],
        'pizza_size_M': [pizza_size == 'Pizza Size M (Medium)'],
        'pizza_size_S': [pizza_size == 'Pizza Size S (Small)'],
        'pizza_size_XL': [pizza_size == 'Pizza Size XL (Extra Large)'],
        'pizza_size_XXL': [pizza_size == 'Pizza Size XXL (Extra Extra Large)'],
        'pizza_category_Chicken': [pizza_category == 'Pizza Category Chicken'],
        'pizza_category_Classic': [pizza_category == 'Pizza Category Classic'],
        'pizza_category_Supreme': [pizza_category == 'Pizza Category Supreme'],
        'pizza_category_Veggie': [pizza_category == 'Pizza Category Veggie']
    }
    return pd.DataFrame(input_data)

# Input form for pizza details
unit_price = st.number_input('Unit Price', value=0)  # Default value is 0
total_price = st.number_input('Total Price', value=0)  # Default value is 0
pizza_size_options = ['Pizza Size L (Large)', 'Pizza Size M (Medium)', 'Pizza Size S (Small)', 'Pizza Size XL (Extra Large)', 'Pizza Size XXL (Extra Extra Large)']
selected_pizza_size = st.selectbox('Select Pizza Size', pizza_size_options, index=0)
pizza_category_options = ['Pizza Category Chicken', 'Pizza Category Classic', 'Pizza Category Supreme', 'Pizza Category Veggie']
selected_pizza_category = st.selectbox('Select Pizza Category', pizza_category_options, index=0)

if st.button('Predict'):
    input_data = preprocess_input(unit_price, total_price, selected_pizza_size, selected_pizza_category)

    # Perform prediction
    result = clf.predict(input_data)

    # Display prediction result
    if result.size > 0:
        st.write('Predicted number of pizzas:', result[0])
    else:
        st.write('Sorry, unable to make a prediction. Please check your inputs.')
