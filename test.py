import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('dataanlitica.xslx.xlsx')


df['CLASIFICACION DE RIESGO'] = df['CLASIFICACION DE RIESGO'].replace('riesgo muy alto', 'Riesgo Muy Alto')
df['CLASIFICACION DE RIESGO'] = df['CLASIFICACION DE RIESGO'].replace('riesgo bajo', 'Riesgo Bajo')
df['CLASIFICACION DE RIESGO'] = df['CLASIFICACION DE RIESGO'].replace('Alto Riesgo', 'Riesgo Alto')
df['CLASIFICACION DE RIESGO'] = df['CLASIFICACION DE RIESGO'].replace('RIESGO BAJO', 'Riesgo Bajo')
df['CLASIFICACION DE RIESGO'] = df['CLASIFICACION DE RIESGO'].replace('RISEGO BAJO', 'Riesgo Bajo')
df['CLASIFICACION DE RIESGO'] = df['CLASIFICACION DE RIESGO'].replace('Riesgo bajo', 'Riesgo Bajo')
df['HTA'] = df['HTA'].replace('hta novo', 'HTA NOVO')
df['HTA'] = df['HTA'].replace('ANTECEDENTE DE HTA', 'ANTECEDENTES')
df['HTA'] = df['HTA'].replace('SI', 'ANTECEDENTES')
df['HTA'] = df['HTA'].replace('ANTECEDNETE', 'ANTECEDENTES')
print(df)

tabla_contingencia = pd.crosstab(df['CLASIFICACION DE RIESGO'], df['HTA'])
sns.set_palette("Set2")

# Cgráfico de barras Seaborn
ax = tabla_contingencia.plot(kind='bar', stacked=True, figsize=(8, 8))

# etiquetas y título
plt.xlabel('Categoría de Riesgo')
plt.ylabel('Frecuencia')
plt.title('Relación entre Riesgo y HTA')

# Personalizar las leyendas
plt.legend(title='HTA', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()
