import streamlit as st
from openai import OpenAI

# Chamando a API da OpenAI
client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# Título
st.title("Mr.Bean🎖️")

# Inicialização de estados
if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-4o-mini'

if "messages" not in st.session_state:
    st.session_state['messages'] = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Instrução do sistema

instructions_one = "Você é smurf forasteiro desconfiado, vendedor de cogumelos proibidos "

# Entrada do usuário
if prompt := st.chat_input("Pergunte alguma coisa:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Smurf está pensando..."):
            stream = client.chat.completions.create(
                model=st.session_state['openai_model'],
                messages=[
                    {"role": "system", "content": instructions_one},
                    {"role": "user", "content": prompt}
                ],
                stream=True,
            )
            response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
