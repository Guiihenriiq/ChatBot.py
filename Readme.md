
````markdown
# 🧠 Mr.Bean🎖️ - Chatbot Smurf Vendedor de Cogumelos Proibidos

Um chatbot divertido e interativo usando [Streamlit](https://streamlit.io/) e a API da [OpenAI](https://openai.com/). O personagem é um smurf forasteiro desconfiado que vende cogumelos proibidos — prepare-se para respostas cômicas e desconfiadas!

---

## 💡 Funcionalidades

- 🤖 Integração com a API da OpenAI (modelo GPT-4o-mini ou outro).
- 💬 Interface de chat com histórico de mensagens.
- 🎭 Personalidade customizada do assistente (smurf forasteiro).
- 🌀 Respostas com `streaming` em tempo real.
- 🗃️ Estado persistente de conversa com `st.session_state`.

---

## 🚀 Como Rodar Localmente

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/mr-bean-chatbot.git
cd mr-bean-chatbot
````

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install streamlit openai
```

### 3. Configure sua chave da OpenAI

Crie um arquivo chamado `.streamlit/secrets.toml` e adicione sua chave da API:

```toml
[OPENAI_API_KEY]
OPENAI_API_KEY = "sua-chave-aqui"
```

### 4. Rode o app

```bash
streamlit run chatbot.py
```

---

## 🧠 Estrutura do Código

```python
# chatbot.py
import streamlit as st
from openai import OpenAI

# Configuração
client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# Título e estados
st.title("Mr.Bean🎖️")
if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-4o-mini'
if "messages" not in st.session_state:
    st.session_state['messages'] = []

# Mostra mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Instruções do sistema
instructions_one = "Você é smurf forasteiro desconfiado, vendedor de cogumelos proibidos"

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
```

---

## 📁 Estrutura de Pastas Recomendada

```
mr-bean-chatbot/
│
├── chatbot.py
├── requirements.txt
└── .streamlit/
    └── secrets.toml
```

---

## 📦 requirements.txt

```txt
streamlit
openai
```

## 🛡️ Licença

Este projeto é open-source e licenciado sob a [MIT License](LICENSE).

---

## 🙋‍♂️ Autor

* Guilherme Henrique
* 🌐 [LinkedIn](https://linkedin.com/in/guilherme-henrique-ferreira-santos-9706b32b7/)
* 📧 Email: [ghcairu@gmail.com.br](mailto:ghcairu@gmail.com.br)


