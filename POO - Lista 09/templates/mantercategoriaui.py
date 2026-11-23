import time
import pandas as pd
import streamlit as st
from service import Service


class ManterCategoriaUI:

    @staticmethod
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterCategoriaUI.listar()
        with tab2:
            ManterCategoriaUI.inserir()
        with tab3:
            ManterCategoriaUI.atualizar()
        with tab4:
            ManterCategoriaUI.excluir()

    @staticmethod
    def listar():
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            list_dic = [obj.to_json() for obj in categorias]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição da categoria", key="inserir_categoria_desc")
        if st.button("Inserir", key="inserir_categoria_btn"):
            Service.categoria_inserir(descricao)
            st.success("Categoria inserida com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de Categorias", categorias, key="atualizar_categoria_sel")
            descricao = st.text_input("Nova descrição", op.get_descricao(), key="atualizar_categoria_desc")
            if st.button("Atualizar", key="atualizar_categoria_btn"):
                id_cat = op.get_id()
                Service.categoria_atualizar(id_cat, descricao)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de Categorias", categorias, key="excluir_categoria_sel")
            if st.button("Excluir", key="excluir_categoria_btn"):
                id_cat = op.get_id()
                Service.categoria_excluir(id_cat)
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()
