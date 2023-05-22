import streamlit as st
from PIL import Image

def main():
    st.set_page_config(
        page_title="Welcome"
    )
    st.title("TediGAN: Text-Guided Diverse Face Image Generation and Manipulation")
    st.subheader("Streamlit Adaptation & Modification")
    st.markdown("***")
    st.markdown("#### Group Name : Noblesse")
    st.markdown("#### Members :")
    col1, col2, col3 = st.columns(3)
    with col1:
       st.image(Image.open('streamlit_images/member3.JPG'), caption="Jundiy Muhammad Alfatih (211511041)")
    with col2:
       st.image(Image.open('streamlit_images/member1.JPG'), caption="Muhammad Hafizh Auliansyah (211511047)")
    with col3:
       st.image(Image.open('streamlit_images/member2.JPG'), caption="Nasrulloh Fajar Muharam (211511050)")
    # st.markdown("- Jundiy Muhammad Alfatih (211511041)")
    # st.markdown("- Muhammad Hafizh Auliansyah (211511047)")
    # st.markdown("- Nasrulloh Fajar Muharam (211511050)")

if __name__ == '__main__':
  main()
