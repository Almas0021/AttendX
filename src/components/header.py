import streamlit as st
from textwrap import dedent


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        dedent(
            f"""
            <div style="
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin-top: 30px;
                margin-bottom: 30px;
            ">
                <img
                    src="{logo_url}"
                    alt="AttendX Logo"
                    style="
                        height: 100px;
                        width: auto;
                    "
                >
                <h1 style="
                    text-align: center;
                    color: #E0E3FF;
                    margin: 10px 0 0 0;
                    padding: 0;
                    white-space: nowrap;
                ">ATTEND X</h1>
            </div>
            """
        ),
        unsafe_allow_html=True
    )


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        dedent(
            f"""
            <div style="
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: flex-start;
                flex-wrap: nowrap;
                gap: 12px;
                width: 100%;
            ">
                <img
                    src="{logo_url}"
                    alt="AttendX Logo"
                    style="
                        height: 70px;
                        width: auto;
                        flex-shrink: 0;
                    "
                >
                <h2 style="
                    color: #5865F2;
                    font-size: 2rem;
                    line-height: 1;
                    margin: 0;
                    padding: 0;
                    white-space: nowrap;
                ">ATTENDX</h2>
            </div>
            """
        ),
        unsafe_allow_html=True
    )