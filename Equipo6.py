from pathlib import Path
import streamlit as st
import plotly.express as px
import pandas as pd

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd

st.title("Análisis de Below Rating Point")

option = st.selectbox(
'Selecciona una variable',
('Familias', 'Refrigerantes', 'Compresor', 'Tecnología'))
st.write('You selected:', option)

if option == 'Familias':
    #("C:\\Users\\victo\\Desktop\\Everything\\Streamlit\\Fam Below.xlsx")
    fam = current_dir / "Fam Below.xlsx"
    df = pd.read_excel(fam)
    fig = px.bar(df, x='Familias', y='Below Rating Point', color = 'Familias', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=3, line_color='Red')
    st.write(fig)

elif option == 'Refrigerantes':
    #("C:\\Users\\victo\\Desktop\\Everything\\Streamlit\\Ref Below.xlsx")
    ref = current_dir / "Ref Below.xlsx"
    df = pd.read_excel(ref)
    fig = px.bar(df, x='Refrigerantes', y='Below Rating Point', color = 'Refrigerantes', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=3, line_color='Red')
    st.write(fig)

elif option == 'Compresor':
    #("C:\\Users\\victo\\Desktop\\Everything\\Streamlit\\Com Below.xlsx")
    com = current_dir / "Com Below.xlsx"
    df = pd.read_excel(com)
    fig = px.bar(df, x='Compresores', y='Below Rating Point', color = 'Compresores', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=3, line_color='Red')
    st.write(fig)

else:
    #("C:\\Users\\victo\\Desktop\\Everything\\Streamlit\\Tec Below.xlsx")
    tec = current_dir / "Tec Below.xlsx"
    df = pd.read_excel(tec)
    fig = px.bar(df, x='Tecnología', y='Below Rating Point', color = 'Tecnología', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=3, line_color='Red')
    st.write(fig)


st.title("Temperaturas por Familia")

#("C:\\Users\\victo\\Desktop\\Everything\\Streamlit\\WORKFILE Supsa Energy Audit Information - Marzo 2022 - Actualizada.xlsx")
supsa = current_dir / "WORKFILE Supsa Energy Audit Information - Marzo 2022 - Actualizada.xlsx"
df = pd.read_excel(supsa)

df.rename(columns = {'% Below Rating Point':'Below_Rating_Point_per',
'RC1 Temp Â°F':'RC1_Temp_F',
'RC2 Temp Â°F':'RC2_Temp_F',
'RC3 Temp Â°F':'RC3_Temp_F',
'FC Temp Average Â°F (M/M)':'FC_Temp_Avg_F_(M/M)',
'RC Temp Average Â°F (M/M)':'RC_Temp_Avg_F_(M/M)',
'FC1 Temp Â°F':'FC1_Temp_F',
'FC2 Temp Â°F':'FC2_Temp_F',
'FC3 Temp Â°F':'FC3_Temp_F',
'FC Temp Average Â°F (W/W or C/C)':'FC_Temp_Avg_F_(W/W or C/C)',
'RC Temp Average Â°F (W/W or C/C)':'RC_Temp_Average_F_(W/W or C/C)',
'Production Line':'Production_Line',
'PosiciÃ³n ':'Posicion',
'% Run Time (M/M)':'Run_Time_MM'}, inplace = True)

option = st.selectbox('Selecciona una variable', ('RC_Temp_Average - 1era Posición', 'FC_Temp_Average - 1era Posición','RC_Temp_Average - 2da Posición','FC_Temp_Average - 2da Posición' ))

st.write('You selected:', option)

if option == 'RC_Temp_Average - 1era Posición':
    fig = px.box(df, x = 'Familia', y = 'RC_Temp_Avg_F_(M/M)',color= 'Familia', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=36, line_color='Red')
    fig.add_hline(y=40, line_color='Red')
    st.write(fig)

elif option == 'RC_Temp_Average - 2da Posición':
    fig = px.box(df, x = 'Familia', y = 'RC_Temp_Average_F_(W/W or C/C)',color= 'Familia', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=36, line_color='Red')
    fig.add_hline(y=40, line_color='Red')
    st.write(fig)

elif option == 'FC_Temp_Average - 2da Posición':
    fig = px.box(df, x = 'Familia', y = 'FC_Temp_Avg_F_(W/W or C/C)',color= 'Familia', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=4, line_color='Red')
    st.write(fig)

elif option == 'FC_Temp_Average - 1era Posición':
    fig = px.box(df, x = 'Familia', y = 'FC Temp Average\nÂ°F (M/M)',color= 'Familia', color_discrete_sequence=["#eeb111", "black"])
    fig.add_hline(y=4, line_color='Red')
    st.write(fig)


st.title("Familias fuera de sus estándares")

option = st.selectbox(
'Selecciona una variable',
('RC Temp Average - 1era Posición', 'FC Temp Average - 1era Posición', 'RC Temp Average - 2da Posición', 'FC Temp Average - 2da Posición'))
st.write('You selected:', option)

famstemps = current_dir / "Familias y estandares de temperatura.xlsx"
#("C:\\Users\\victo\\Desktop\\Everything\\Streamlit\\Familias y estandares de temperatura.xlsx")
df = pd.read_excel(famstemps)

if option == 'RC Temp Average - 1era Posición':
    fig = px.pie(df, values = 'PerRC1', names = "Fam", color_discrete_sequence = px.colors.sequential.YlOrBr)
    st.write(fig)
    
    st.subheader("Las 3 familias con mejor desempeño son:")
    st.write('Fam - 4W3G80: De un total de 117 datos, 8 están fuera de sus estándares.\n' 'El 6.84 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3iG81: De un total de 23 datos, 2 están fuera de sus estándares.\n' 'El 8.70 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3n90: De un total de 39 datos, 4 están fuera de sus estándares.\n' 'El 10.26 porciento del total de sus datos están fuera de los estándares')
    
    st.subheader("Las 3 familias con peor desempeño son:")
    st.write('Fam - 6w3n80: De un total de 79 datos, 63 están fuera de sus estándares.\n' 'El 79.75 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 6w3g10: De un total de 13 datos, 8 están fuera de sus estándares.\n' 'El 61.54 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3G12: De un total de 92 datos, 45 están fuera de sus estándares.\n' 'El 48.91 porciento del total de sus datos están fuera de los estándares')

elif option == 'FC Temp Average - 1era Posición':
    fig = px.pie(df, values = 'PerFC1', names = "Fam", color_discrete_sequence = px.colors.sequential.YlOrBr)
    st.write(fig)

    st.subheader("Las 3 familias con mejor desempeño son:")
    st.write('Fam - 5w3n80: De un total de 54 datos, 21 están fuera de sus estándares.\n' 'El 38.89 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3iG81: De un total de 23 datos, 11 están fuera de sus estándares.\n' 'El 47.83 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3G80: De un total de 117 datos, 66 están fuera de sus estándares.\n' 'El 56.41 porciento del total de sus datos están fuera de los estándares')
    
    st.subheader("Las familias con peor desempeño son:")
    st.write('Fam - 6w3n80: De un total de 79 datos, 79 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 6w3g10: De un total de 13 datos, 13 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3G12: De un total de 92 datos, 92 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 0w3i10: De un total de 12 datos, 12 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3n10: De un total de 21 datos, 21 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')

elif option == 'RC Temp Average - 2da Posición':
    fig = px.pie(df, values = 'PerRC2', names = "Fam", color_discrete_sequence = px.colors.sequential.YlOrBr)
    st.write(fig)

    st.subheader("Las 3 familias con mejor desempeño son:")
    st.write('Fam - 6w3g10: De un total de 13 datos, 8 están fuera de sus estándares.\n' 'El 61.54 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 0w3i10: De un total de 12 datos, 9 están fuera de sus estándares.\n' 'El 75.00 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3G12: De un total de 92 datos, 76 están fuera de sus estándares.\n' 'El 82.61 porciento del total de sus datos están fuera de los estándares')
    
    st.subheader("Las 3 familias con peor desempeño son:")
    st.write('Fam - 4w3n10: De un total de 21 datos, 21 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3G80: De un total de 117 datos, 117 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3iG81: De un total de 23 datos, 23 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')

else:
    fig = px.pie(df, values = 'PerFC2', names = "Fam", color_discrete_sequence = px.colors.sequential.YlOrBr)
    st.write(fig)

    st.subheader("Las 3 familias con mejor desempeño son:")
    st.write('Fam - 6w3n80: De un total de 79 datos, 35 están fuera de sus estándares.\n' 'El 44.30 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3n10: De un total de 21 datos, 13 están fuera de sus estándares.\n' 'El 61.90 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3G12: De un total de 92 datos, 58 están fuera de sus estándares.\n' 'El 63.04 porciento del total de sus datos están fuera de los estándares')
    
    st.subheader("Las familias con peor desempeño son:")
    st.write('Fam - 4W3G80: De un total de 117 datos, 117 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3iG81: De un total de 23 datos, 23 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4w3n90: De un total de 39 datos, 39 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 5w3n80: De un total de 54 datos, 54 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
    st.write('Fam - 4W3N80: De un total de 43 datos, 43 están fuera de sus estándares.\n' 'El 100 porciento del total de sus datos están fuera de los estándares')
