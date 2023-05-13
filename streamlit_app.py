import streamlit as st

with st.form("demanda"):

    st.divider()
    st.header("TIPO DE ACCIÓN A PLANTEAR")
    accion = st.selectbox("Accion",('RESCISIÓN DE CONTRATO','AMPARO POSESORIO'))

    st.divider()
    st.header("Fundamentos de Derecho")

    if accion == 'RESCISIÓN DE CONTRATO':
        tab1, tab2, tab3, tab4 = st.tabs(["Constitución de la República del Ecuador","Código Civil", "Código Orgánico General de Procesos", "Código Orgánico de la Función Judicial"])

        with tab1:
            st.header("Constitución de la República del Ecuador")
            st.multiselect('Selecciona los artículos a usar',['1','75','76','82','167', '169', '172', '174 inciso segundo'])
            e1 = st.expander("1")
            e1.markdown("""
                        El Ecuador es un Estado constitucional de derechos y justicia, social, democrático, soberano, independiente, unitario, intercultural, plurinacional y laico. Se organiza en forma de república y se gobierna de manera descentralizada.
                        La soberanía radica en el pueblo, cuya voluntad es el fundamento de la autoridad, y se ejerce a través de los órganos del poder público y de las formas de participación directa previstas en la Constitución.
                        Los recursos naturales no renovables del territorio del Estado pertenecen a su patrimonio inalienable, irrenunciable eimprescriptible.
                        """)
            e1 = st.expander("75")
            e1.markdown("Toda persona tiene derecho al acceso gratuito a la justicia y a la tutela efectiva, imparcial y expedita de sus derechos e intereses, con sujeción a los principios de inmediación y celeridad; en ningún caso quedará en indefensión. El incumplimiento de las resoluciones judiciales será sancionado por la ley.")
            
            e2 = st.expander("76")
            e2.markdown(
                        """
                        En todo proceso en el que se determinen derechos y obligaciones de cualquier orden, se asegurará el derecho al debido proceso que incluirá las siguientes garantías básicas:

                        1. Corresponde a toda autoridad administrativa o judicial, garantizar el cumplimiento de las normas y los derechos de las partes.
                        2. Se presumirá la inocencia de toda persona, y será tratada como tal, mientras no se declare su responsabilidad mediante resolución firme o sentencia ejecutoriada.
                        3. Nadie podrá ser juzgado ni sancionado por un acto u omisión que, al momento de cometerse, no esté tipificado en la ley como infracción penal, administrativa o de otra naturaleza; ni se le aplicará una sanción no prevista por la Constitución o la ley. Solo se podrá juzgar a una persona ante un juez o autoridad competente y con observancia del trámite propio de cada procedimiento.
                        4. Las pruebas obtenidas o actuadas con violación de la Constitución o la ley no tendrán validez alguna y carecerán de eficacia probatoria.
                        5. En caso de conflicto entre dos leyes de la misma materia que contemplen sanciones diferentes para un mismo hecho, se aplicará la menos rigurosa, aún cuando su promulgación sea posterior a la infracción. En caso de duda sobre una norma que contenga sanciones, se la aplicará en el sentido más favorable a la persona infractora.
                        6. La ley establecerá la debida proporcionalidad entre las infracciones y las sanciones penales, administrativas o de otra naturaleza.
                        7. El derecho de las personas a la defensa incluirá las siguientes garantías:
                            a) Nadie podrá ser privado del derecho a la defensa en ninguna etapa o grado del procedimiento.
                            b) Contar con el tiempo y con los medios adecuados para la preparación de su defensa.
                            c) Ser escuchado en el momento oportuno y en igualdad de condiciones.
                            d) Los procedimientos serán públicos salvo las excepciones pre-vistas por la ley. Las partes podrán acceder a todos los documentos y actuaciones del procedimiento.
                            e) Nadie podrá ser interrogado, ni aún con fines de investigación, por la Fiscalía General del Estado, por una autoridad policial o por cualquier otra, sin la presencia de un abogado particular o un defensor público, ni fuera de los recintos autorizados para el efecto.
                            f) Ser asistido gratuitamente por una traductora o traductor o intérprete, si no comprende o no habla el idioma en el que se sustancia el procedimiento.
                            g) En procedimientos judiciales, ser asistido por una abogada o abogado de su elección o por defensora o defensor público; no podrá restringirse el acceso ni la comunicación libre y privada con su defensora o defensor.
                            h) Presentar de forma verbal o escrita las razones o argumentos de los que se crea asistida y replicar los argumentos de las otras partes; presentar pruebas y contradecir las que se presenten en su contra.
                            i) Nadie podrá ser juzgado más de una vez por la misma causa y materia. Los casos resueltos por la jurisdicción indígena deberán ser considerados para este efecto.
                            j) Quienes actúen como testigos o peritos estarán obligados a comparecer ante la jueza, juez o autoridad, y a responder al interrogatorio respectivo.
                            k) Ser juzgado por una jueza o juez independiente, imparcial y competente. Nadie será juzgado por tribunales de excepción o por comisiones especiales creadas para el efecto.
                            l) Las resoluciones de los poderes públicos deberán ser motivadas. No habrá motivación si en la resolución no se enuncian las normas o principios jurídicos en que se funda y no se explica la pertinencia de su aplicación a los antecedentes de hecho. Los actos administrativos, resoluciones o fallos que no se encuentren debidamente motivados se considerarán nulos. Las servidoras o servidores responsables serán sancionados.
                            m) Recurrir el fallo o resolución en todos los procedimientos en los que se decida sobre sus derechos.
                        """)

            e3 = st.expander("82")
            e3.markdown("El derecho a la seguridad jurídica se fundamenta en el respeto a la Constitución y en la existencia de normas jurídicas previas, claras, públicas y aplicadas por las autoridades competentes.")

            e4 = st.expander("167")
            e4.markdown("La potestad de administrar justicia emana del pueblo y se ejerce por los órganos de la Función Judicial y por los demás órganos y funciones establecidos en la Constitución.")

            e5 = st.expander("169")
            e5.markdown("El sistema procesal es un medio para la realización de la justicia. Las normas procesales consagrarán los principios de simplificación, uniformidad, eficacia, inmediación, celeridad y economía procesal, y harán efectivas las garantías del debido proceso. No se sacrificará la justicia por la sola omisión de formalidades.")

            e6 = st.expander("172")
            e6.markdown("""
                            Las juezas y jueces administrarán justicia con sujeción a la Constitución, a los instrumentos internacionales de derechos humanos y a la ley.

                            Las servidoras y servidores judiciales, que incluyen a juezas y jueces, y los otros operadores de justicia, aplicarán el principio de la debida diligencia en los procesos de administración de justicia.

                            Las juezas y jueces serán responsables por el perjuicio que se cause a las partes por retardo, negligencia, denegación de justicia o quebrantamiento de la ley.
                        """)
            
            e7 = st.expander("174")
            e7.markdown("""
                            Las servidoras y servidores judiciales no podrán ejercer la abogacía ni desempeñar otro empleo público o privado, excepto la docencia universitaria fuera de horario de trabajo.

                            La mala fe procesal, el litigio malicioso o temerario, la generación de obstáculos o dilación procesal, serán sancionados de acuerdo con la ley.

                            Las juezas y jueces no podrán ejercer funciones de dirección en los partidos y movimientos políticos, ni participar como candidatos en procesos de elección popular, ni realizar actividades de proselitismo político o religioso.
                        """)

        with tab2:
            st.header("580")
            st.markdown("Las fundaciones de beneficencia que hayan de administrarse por una agrupación de individuos, se regirán por los estatutos que el fundador les hubiere dictado; y si el fundador no hubiere manifestado su voluntad a este respecto, o sólo la hubiere manifestado incompletamente, se suplirá esta falta por el Presidente de la República.")
            st.header("599")
            st.markdown("El dominio, que se llama también propiedad, es el derecho real en una cosa corporal, para gozar y disponer de ella, conforme a las disposiciones de las leyes y respetando el derecho ajeno, sea individual o social. La propiedad separada del goce de la cosa, se llama mera o nuda propiedad.")
            codigo_civil=st.multiselect('Selecciona los artículos a usar',['580', '599','603', '686', '691', '702','1457','1708','1764', '1777', '1797','1798','1800', '1806', '1807', '1828','1829','1831', '1833', '1836', '1855', '2392', '2393'])

        with tab3:
            st.header("Código Orgánico General de Procesos")
            st.multiselect('Selecciona los artículos a usar',['76','89','107','148','168','233','234','256','262','262 numeral 3', '284', '289', '291', '294', '295', '297'])

        with tab4:
            st.header("Código Orgánico de la Función Judicial")
            st.multiselect('Selecciona los artículos a usar',['1','18','28','29','129','150','152','240'])
        
    st.form_submit_button("Generar demanda")
