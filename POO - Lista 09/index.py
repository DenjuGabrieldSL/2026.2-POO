import streamlit as st
from templates.manterclienteui import ManterClienteUI
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterprodutoui import ManterProdutoUI
from templates.reajustarprodutoui import ReajustarProdutoUI


class IndexUI:

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            ["Clientes", "Categorias", "Produtos", "Reajustar Pre\u00e7os"]
        )
        if op == "Clientes":
            ManterClienteUI.main()
        elif op == "Categorias":
            ManterCategoriaUI.main()
        elif op == "Produtos":
            ManterProdutoUI.main()
        elif op == "Reajustar Pre\u00e7os":
            ReajustarProdutoUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()


if __name__ == "__main__":
    IndexUI.main()
