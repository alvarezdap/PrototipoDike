import streamlit as st

accion = st.selectbox("Accion",('RESCISIÓN DE CONTRATO','AMPARO POSESORIO'))

if accion == 'RESCISIÓN DE CONTRATO':
    codigo_civil=st.multiselect('Codigo Civil',['580', '599','603', '686', '691', '702','1457','1708','1764', '1777', '1797','1798','1800', '1806', '1807', '1828','1829','1831', '1833', '1836', '1855', '2392', '2393'])
    if codigo_civil == '580':
        st.expander('Artículo 580')
        st.markdown('Las fundaciones de beneficencia que hayan de administrarse por una agrupación de individuos, se regirán por los estatutos que el fundador les hubiere dictado; y si el fundador no hubiere manifestado su voluntad a este respecto, o sólo la hubiere manifestado incompletamente, se suplirá esta falta por el Presidente de la República.')
    if codigo_civil == '599':
        st.expander('Artículo 599')
        st.markdown('El dominio, que se llama también propiedad, es el derecho real en una cosa corporal, para gozar y disponer de ella, conforme a las disposiciones de las leyes y respetando el derecho ajeno, sea individual o social. La propiedad separada del goce de la cosa, se llama mera o nuda propiedad.')
    st.multiselect('Código Orgánico General de Procesos',['76','89','107','148','168','233','234','256','262','262 numeral 3', '284', '289', '291', '294', '295', '297'])
    st.multiselect('Constitución de la República del Ecuador',['1','75','76','76 numeral 7','76 numeral 7 literal h)','76 numeral 7 literal l)','82','167', '169', '172', '174 inciso segundo'])
    st.multiselect('Código Orgánico de la Función Judicial',['1','18','28','29','129','150','152','240'])




