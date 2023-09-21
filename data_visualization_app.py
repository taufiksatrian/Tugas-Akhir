import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import tableauserverclient as TSC
from matplotlib.patches import Patch
import streamlit.components.v1 as components

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


tableau_html = """
<div class="centered" style="text-align: center;">
    <div class='tableauPlaceholder' id='viz1695328600249' style='display:inline-block;'>
        <noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tr&#47;TracerStudyUnsoed1-2&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript>
        <object class='tableauViz' style='display:none; width: 100%;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='TracerStudyUnsoed1-2&#47;Dashboard1' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tr&#47;TracerStudyUnsoed1-2&#47;Dashboard1&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1695328600249');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 1200 ) {
        vizElement.style.width='1200px';
        vizElement.style.height='827px';
    } else if ( divElement.offsetWidth > 800 ) {
        vizElement.style.width='1000px';
        vizElement.style.height='827px';
    } else {
        vizElement.style.width='100%';
        vizElement.style.height='1277px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

st.markdown("""
<style>
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
""", unsafe_allow_html=True)

st.write(
    """
    ### Dashboard 
Dashboard menggunakan Tools Tableau:
"""
)

components.html(tableau_html, height=1000, width=1200)
