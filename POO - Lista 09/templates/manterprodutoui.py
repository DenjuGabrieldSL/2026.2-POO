import time
import pandas as pd
import streamlit as st
from service import Service


class ManterProdutoUI:

    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProdutoUI.listar()
        with tab2:
            ManterProdutoUI.inserir()
        with tab3:
            ManterProdutoUI.atualizar()
        with tab4:
            ManterProdutoUI.excluir()

    @staticmethod
    def listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            list_dic = [obj.to_json() for obj in produtos]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            st.warning("Cadastre uma categoria antes de inserir produtos.")
            return

        descricao = st.text_input("Informe a descrição do produto", key="inserir_produto_desc")
        preco = st.number_input("Informe o preço", min_value=0.0, step=0.5, format="%.2f", key="inserir_produto_preco")
        categoria = st.selectbox("Selecione a categoria", categorias, key="inserir_produto_cat")

        if st.button("Inserir", key="inserir_produto_btn"):
            Service.produto_inserir(descricao, preco, categoria.get_id())
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        produtos = Service.produto_listar()
        categorias = Service.categoria_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produtos, key="atualizar_produto_sel")
            descricao = st.text_input("Nova descrição", op.get_descricao(), key="atualizar_produto_desc")
            preco = st.number_input(
                "Novo preço",
                min_value=0.0,
                value=float(op.get_preco()),
                step=0.5,
                format="%.2f",
                key="atualizar_produto_preco"
            )
            id_cat_atual = op.get_id_categoria()
            indice_cat = 0
            for i, c in enumerate(categorias):
                if c.get_id() == id_cat_atual:
                    indice_cat = i
                    break
            categoria = st.selectbox(
                "Nova categoria",
                categorias,
                index=indice_cat if categorias else 0,
                key="atualizar_produto_cat"
            )

            if st.button("Atualizar", key="atualizar_produto_btn"):
                id_prod = op.get_id()
                id_cat = categoria.get_id() if categoria else id_cat_atual
                Service.produto_atualizar(id_prod, descricao, preco, id_cat)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produtos, key="excluir_produto_sel")
            if st.button("Excluir", key="excluir_produto_btn"):
                id_prod = op.get_id()
                Service.produto_excluir(id_prod)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()
