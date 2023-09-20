import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

data_training = pd.read_csv('data_sintetis_akhir.csv', sep=';')

st.title("Dashboard Tracer Study Unsoed")
st.header("Tracer Study")
st.write(
    """
Tracer study ini bertujuan untuk mengetahui profil mahasiswa setelah lulus dari UNSOED. Tracer study ini dilaksanakan untuk menjaring informasi dan masukan dari alumni sebagai salah satu dasar yang sangat penting bagi evaluasi dan pengembangan UNSOED, dalam bidang kurikulum, proses pembelajaran, sarana prasarana, dan pelayanan.
"""
)

st.write(
    """
    ### **Pertanyaan Nomor 1**
#### **F8 - Jelaskan status Anda saat ini?**

F8 adalah kolom yang menggambarkan status saat ini dari responden. Responden diminta untuk menjelaskan status mereka saat ini berdasarkan pilihan jawaban yang disediakan:

- **1: Bekerja (Full Time / Part Time)**: Responden sedang bekerja baik secara full time maupun part time.
- **2: Belum Memungkinkan Bekerja**: Responden tidak memungkinkan untuk bekerja saat ini.
- **3: Wiraswasta**: Responden adalah seorang wiraswasta atau memiliki usaha sendiri.
- **4: Melanjutkan Pendidikan**: Responden sedang melanjutkan pendidikan mereka.
- **5: Tidak Bekerja Tetapi Sedang Mencari Kerja**: Responden tidak sedang bekerja, namun aktif mencari pekerjaan.")
"""
)

f8ket_counts = data_training['f8ket'].value_counts()

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=f8ket_counts.values, y=f8ket_counts.index,
                 orient='h', palette='viridis')
plt.title('Grafik Kategori Alumni')
plt.xlabel('Jumlah')
plt.ylabel('Kategori')
plt.xticks(rotation=0, ha='center')

total_data_awal = len(data_training['f8'])
for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width} ({width/total_data_awal:.2%})',
                (width - 80, p.get_y() + p.get_height() / 2.),
                va='center', ha='left', color='white')

maxt = f8ket_counts.idxmax()
mint = f8ket_counts.idxmin()
max_color_index = np.where(f8ket_counts.index == maxt)[0][0]
min_color_index = np.where(f8ket_counts.index == mint)[0][0]

legend_elements = [
    Patch(facecolor=sns.color_palette('viridis')[
          max_color_index], edgecolor='black', label=f'Frekuensi Tingkat Kesesuaian Pendidikan Paling Banyak: {maxt}'),
    Patch(facecolor=sns.color_palette('viridis')[
          min_color_index], edgecolor='black', label=f'Frekuensi Tingkat Kesesuaian Pendidikan Paling Sedikit: {mint}'),
]

plt.legend(handles=legend_elements, title="Statistik Tingkat Pendidikan",
           loc='upper center', bbox_to_anchor=(0.5, -0.15))

keterangan = f'Data yang Digunakan {total_data_awal} dari {total_data_awal} Data'
plt.text(0.19, -0.12, keterangan, ha='center', va='center',
         transform=plt.gca().transAxes, fontsize=10)


st.pyplot(plt)
