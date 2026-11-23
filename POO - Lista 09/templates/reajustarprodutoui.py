import time
import streamlit as st
from service import Service


class ReajustarProdutoUI:

    @staticmethod
    def main():
        st.header("Reajustar Preço de Produtos")
        ReajustarProdutoUI.reajustar()

    @staticmethod
    def reajustar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
            return

        percentual = st.number_input(
            "Percentual de reajuste (%)",
            value=10.0,
            step=1.0,
            format="%.2f",
            help="Use valores positivos para aumentar ou negativos para diminuir."
        )

        if st.button("Reajustar Preços", key="reajustar_produto_btn"):
            Service.produto_reajustar(percentual)
            st.success("Preços reajustados com sucesso")
            time.sleep(2)
            st.rerun()
