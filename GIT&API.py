# Import library pandas dengan alias pd
import pandas as pd

# Membuat dictionary 'data' yang berisi informasi nama, usia, dan gaji karyawan
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat DataFrame 'df' dari dictionary 'data'
df = pd.DataFrame(data)

# Menampilkan DataFrame 'df' ke layar
print(df)
print('Gaji karyawan sebelum diberikan kenaikan')
print()

# Kenaikan gaji 5%
for a, row in df.iterrows():
    df.loc[a, 'Kenaikan Gaji 5%'] = (lambda gaji: int(gaji + (gaji * 0.05)))(row['Gaji'])

# Menampilkan DataFrame 'df' setelah kenaikan gaji sebesar 5%
print(df)
print('Karyawan setelah mendapatkan kenaikan gaji sebesar 5% dari gaji mereka\n')

# Kenaikan 2% untuk karyawan berusia 30 tahun
for a, row in df.iterrows():
    # Menggunakan lambda function untuk menghitung kenaikan gaji sesuai kondisi usia
    df.loc[a, 'Kenaikan Gaji 2%'] = (lambda gaji, umur: int(gaji + (gaji * 0.02)) if umur > 30 else int(gaji))(row['Kenaikan Gaji 5%'], row['Usia'])

# Membuat salinan DataFrame 'df' yang diperbarui
data_terbaru = df.copy()

# Membuat DataFrame baru 'df_terbaru' dari salinan DataFrame 'df'
df_terbaru = pd.DataFrame(data_terbaru)

# Menampilkan DataFrame 'df_terbaru' yang sudah diperbarui
print(df_terbaru)
print('Karyawan berusia 30 tahun setelah mendapatkan kenaikan 2% dari gaji mereka')
