import time
import pandas as pd
import streamlit as st
from service import Service


class ManterClienteUI:

    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            list_dic = [obj.to_json() for obj in clientes]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome", key="inserir_cliente_nome")
        email = st.text_input("Informe o e-mail", key="inserir_cliente_email")
        fone = st.text_input("Informe o fone", key="inserir_cliente_fone")
        if st.button("Inserir", key="inserir_cliente_btn"):
            Service.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes, key="atualizar_cliente_sel")
            nome = st.text_input("Novo nome", op.get_nome(), key="atualizar_cliente_nome")
            email = st.text_input("Novo e-mail", op.get_email(), key="atualizar_cliente_email")
            fone = st.text_input("Novo fone", op.get_fone(), key="atualizar_cliente_fone")
            if st.button("Atualizar", key="atualizar_cliente_btn"):
                id_cli = op.get_id()
                Service.cliente_atualizar(id_cli, nome, email, fone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes, key="excluir_cliente_sel")
            if st.button("Excluir", key="excluir_cliente_btn"):
                id_cli = op.get_id()
                Service.cliente_excluir(id_cli)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
