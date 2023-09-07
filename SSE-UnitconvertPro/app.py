import streamlit as st
import pint
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def main():
    
    st.set_page_config(page_title="SSE-UnitConvertPro", page_icon="📏", layout="wide")
    st.subheader("Welcome to :wave:-")
    st.title("📐SSE-UnitConvertPro")

    unit_format = {
        "Default": "D",
        "Short default": "~D",
        "Pretty": "P",
        "Short pretty": "~P",
        "Compact": "C",
        "Short compact": "~C" 
    }
    

    
    with st.sidebar:
        st.header("Settings")
        fmt = st.radio("Output style",unit_format.keys(), index= 2)
        prec = st.radio("Output decimals", (2, 4, 6, 8), index=0, horizontal=True)

    st.write("---")
    st.markdown("""
    ## Length/Distance & Temperature Conversion

    ##                        *Instructions*
    Enter a quantity and its unit on the left, and the desired unit on the right. 
    Example: 
    for Length/Distance "2.54 cm to m" |
    for Temperature "45 degF to degC"
    """)
    
    
    # ----- 
    
    
    left_column, right_column = st.columns((1,2))
    with left_column:
        st.subheader("Input")
        user_input = st.text_input("x", label_visibility="collapsed", value="2.54 cm to m")
        x, y = user_input.split(" to ")
        x1, x2 = x.split(" ")
        
    with right_column:
        st.subheader("Output")
        ureg = pint.UnitRegistry()
        output = ureg.Quantity(float(x1), x2).to(y)
        st.markdown(f"{output:0.{prec}f{unit_format[fmt]}}s")
    
    st.write("---")
    # -----


    st.write("##")
     
    
    
    st.write("##")
    st.write("##")
    st.markdown("This is some random text ")

    
    st.write("---")
    left_Tcolumn, right_Tcolumn = st.columns([1,3])
    with left_Tcolumn:
        st.subheader("Liked our work?🏋️" )
        st.write("[Check out our Team 👈 ](https:youtube.com)")
    
    with right_Tcolumn:
        
        st.subheader("About Us" )
        st.write("##")
        st.markdown("""We are a TEAM👌 of typical witty minded misfit developers, 
                          coming up with ways to make doing complex tasks simpler.""")
    
if __name__ == "__main__":
    main()
