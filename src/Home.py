import streamlit as st

st.set_page_config(layout="wide", page_icon="💬", page_title="EquiBot | Chat 🔮")

st.markdown(
    """
    <h2 style='text-align: center;'>Sou EquiBot, seu assistente com reconhecimento de dados 🔮</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

st.markdown(
    """ 
    <h4 style='text-align:center;'>Sou um chatbot inteligente para interagir com linguagem natural.</h4> \n
    <h4 style='text-align:center;'>Usando o modelo de linguagem da OpenAi para fornecer interações sensíveis ao contexto dos negócios da empresa. </h4>
    <h4 style='text-align:center;'>Meu objetivo é mostrar algumas das possibilidades que a Inteligência Artificial pode trazer para o nosso negócio.\n
    <h4 style='text-align:center;'>Desde que bem estruturados e com informações confiaveis posso facilitar o entendimento de arquivos do tipo PDF, TXT, CSV. </h4>
    """    ,
    unsafe_allow_html=True)
st.markdown("---")

st.markdown(
    """<h5 style='text-align:center; color:red'> 🚨 É importante lembrar que esta aplicação é apenas um Protótipo criado com Streamlit \n 
    Uma poderosa ferramenta de análise de dados open source, 
    o que fez possível acelerar a construção desta Interface. \n</h5>"""
    ,
    unsafe_allow_html=True)
st.markdown("---")

#Robby's Pages
st.subheader("Recursos")
st.write("""
--> 📃 **Doc-Chat**: Bate-papo com os dados de aquivo do tipo (PDF, TXT, CSV) \n
--> 📈 **Visual-Doc**: Bate papo com dados tabulares e possibilidade de gerar dados visuais do tipo (CSV e XLSX(teste))
""")
st.markdown("---")


#Contributing
st.markdown("###  Contribuição")
st.markdown("""
**Aplicação foi criada com base em estudos feitos em outros cases.**
\n**Funcionalidades adaptadas para nossa realidade, a partir do interesse e pesquisa no assunto, e adaptado, para os moldes de nossa realidade e necessidade.**
""", unsafe_allow_html=True)





