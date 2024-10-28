import streamlit as st


def main():
    st.logo("images/screenshot.png")

    dummy1, title_col, dummy2 = st.columns(3)
    with title_col:
        st.header("PETER GACHUKI PORTFOLIO")
        st.caption("DATA SCIENTIST | DATA ANALYST | DATA ENGINEER")

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            "My name is Peter Gachuki Gichuri. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. ")

        st.write(
            "My name is Peter Gachuki Gichuri. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. ")

        st.write(
            "My name is Peter Gachuki Gichuri. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. ")

        st.write(
            "My name is Peter Gachuki Gichuri. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. ")

        st.write(
            "My name is Peter Gachuki Gichuri. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. ")

    with col2:
        d1, ac_col2, d2 = st.columns(3)
        with ac_col2:
            st.image("images/portrait.jpeg", width=420)


    st.subheader("Links : ")

    column1, column2 = st.columns(2)
    with column1:
        st.write("Github : https://github.com")
        st.write("LinkedIn : https://linkedin.com")
        st.write("Medium : https://medium.com")
    with column2:
        st.write("X : https://x.com")
        st.write("Facebook : https://facebook.com")
        st.write("Whatsapp : https://whatsapp.com")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Peter Gachuki Portfolio",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    main()
