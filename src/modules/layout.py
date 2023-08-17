import streamlit as st

class Layout:
    
    def show_header(self, types_files):
        st.markdown(
            f"""
            <h2 style='text-align: center;'> Bate papo com  {types_files} ! 📄</h2>
            """,
            unsafe_allow_html=True,
        )

    def show_api_key_missing(self):
        st.markdown(
            """
            <div style='text-align: center;'>
                <h4>Digite sua <a href="https://platform.openai.com/account/api-keys" target="_blank">chave OpenAI API</a> para começar a conversar.</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="Pergunte-me qualquer coisa sobre o documento...",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Perguntar")
            
            is_ready = submit_button and user_input
        return is_ready, user_input
    
