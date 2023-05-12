import streamlit as st

accion = st.numeralselectbox("Accion",('RESCISIÓN DE CONTRATO','AMPARO POSESORIO'))

if accion == 'RESCISIÓN DE CONTRATO':
    st.multiselect('Codigo Civil',['580', '599','603', '686', '691', '702','1457','1708','1764', '1777', '1797','1798','1800', '1806', '1807', '1828','1829','1831', '1833', '1836', '1855', '2392', '2393'])
    st.multiselect('Código Orgánico General de Procesos',['76','89','107','148','168','233','234','256','262','262 numeral 3', '284', '289', '291', '294', '295', '297'])
    st.multiselect('Constitución de la República del Ecuador',['1','75','76','76 numeral 7','76 numeral 7 literal h)','76 numeral 7 literal l)','82','167', '169', '172', '174 inciso segundo'])
    st.multiselect('Código Orgánico de la Función Judicial',['1','18','28','29','129','150','152','240'])




