from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_clickable_images import clickable_images
import webbrowser

# CONFIG

def set_config():
    st.set_page_config(page_title= "My Portfolio", page_icon=":page_facing_up:", layout="wide")
    local_css("style/style.css")

# UTILS

def load_lottie_anim(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# ASSETS
lottie_code_anim = load_lottie_anim("https://lottie.host/c1fd3860-ea0f-4ce2-975f-97f66d23a165/3Gp6qbiUIq.json")
lottie_education_anim = load_lottie_anim("https://lottie.host/9756ee76-0f5f-448a-a34c-0e2fa9ab84dd/UEXeTUTXl0.json")
lottie_skills_anim = load_lottie_anim("https://lottie.host/553da8c2-ff20-4953-9181-eba32bc06f85/wsk1zEcnTw.json")
lottie_projects_anim = load_lottie_anim("https://lottie.host/5def4371-95f7-4652-9ddf-d75ce6d2d802/BZTaxxa78B.json")
lottie_contact_anim = load_lottie_anim("https://lottie.host/e0746537-e7e9-4d07-a68a-6b83ed821dba/LpdVvXO15u.json")

img_avatar = Image.open("images/avatar.png")
img_graduation_cap = Image.open("images/graduationcap.png")

skill_logo_list = []
for s in ["android","flutter","java","python","cpp","c"]:
    skill_logo_list.append(Image.open(f"images/{s}-logo.png"))

img_puzzle_icon = Image.open("images/puzzle-icon.png")
img_keyboard_icon = Image.open("images/keyboard-icon.png")
img_portfolio_icon = Image.open("images/portfolio-icon.png")

contact_logo_list = []
for s in ["github","gmail","linkedin","x"]:
    contact_logo_list.append(f"images/{s}-logo.png")


# Markdown CSS Variables

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

hide_go_to_button = '''
<style>
a{
    visibility: hidden;}
</style>
'''

# HEADER

def set_header():
    with st.container():
        avatar, header_col = st.columns((1,4))
        with avatar:
            st.image(img_avatar,width=200)
            st.markdown(hide_img_fs, unsafe_allow_html=True)
        with header_col:
            st.header("M. Yusuf Kartal")
            st.subheader("Student & Developer")
            st.markdown(hide_go_to_button, unsafe_allow_html=True)
            st.write("TOBB ETU AI Engineering")

# BODY

# 
# def img_item_pair(img_col, item_col, img_left_or_right = "right"):
#     if img_left_or_right == "left":
#         left_column = img_col
#         right_column = item_col
#     elif img_left_or_right == "right":
#         left_column = item_col
#         right_column = img_col
    
def set_body():
    with st.container():
        st.write("---")
        # ----- ABOUT PART -----
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("About me")
            st.write("##")
            st.write("""
                        Hi, I am Yusuf :wave:\nI am an Artifical Intelligence Engineering student at TOBB ETU. I have started programming at the age of 15. since then I have dabbled with various stuff 
                        related to programming such as game development, mobile app development, cyber security, 
                        robotics, IoT, and Artificial Intelligence. Currently, I am trying to learn artificial intelligence,
                        and improve my skills by working on projects. Besides, I am developing mobile apps for personal
                        usage. 
                    """)
        with right_column:
            st_lottie(lottie_code_anim, height=300, key="code")
        st.write("---")

        # ----- EDUCATION PART -----
        left_column, right_column = st.columns((1,2))
        with right_column:
            st.header("Education")
            i1, divider1, i2, divider2, i3 = st.columns((2,1,2,1,2))
            with i1:
                st.subheader("TOBB ETU AI Engineering")
                st.write("Expected to graduate in 2027")
            with divider1:
                st.write("---")
            with i2:
                st.subheader("High School")
                st.write("Graduated in 2023")
                
            with divider2:
                st.write("---")
            with i3:
                st.subheader("Secondary School")
                st.write("Graduated in 2018")
        with left_column:
            st_lottie(lottie_education_anim, height=300, key="education")
        st.write("---")

        # ----- SKILLS PART -----
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("Skills")
            st.write("##")
            for i, s in enumerate(st.columns(6)):
                s.image(skill_logo_list[i],width=100)
        with right_column:
            st_lottie(lottie_skills_anim, height=300, key="skills")
        st.write("---")
        
        # ----- PROJECTS PART -----
        left_column, right_column = st.columns((1,2))
        with right_column:
            st.header("Projects")
            i1, divider1, i2, divider2, i3 = st.columns((2,1,2,1,2))
            with i1:
                st.image(img_portfolio_icon)
                st.subheader("Basic Mobile Portfolio")
                st.write("A basic portfolio app template.")
                st.write("2023")
                if st.button("Github",type="secondary"):
                    webbrowser.open("https://github.com/yAquila/Basic-Mobile-Portfolio")
            with divider1:
                st.write("|")
            with i2:
                st.image(img_puzzle_icon)
                st.subheader("Mind Plateau")
                st.write("A comprehensive platform for mind games.")
                st.write("2021-2022")
                
            with divider2:
                st.write("|")
            with i3:
                st.image(img_keyboard_icon)
                st.subheader("Type Against")
                st.write("A multiplayer mobile fast-typing game.")
                st.write("2020")
        with left_column:
            st_lottie(lottie_projects_anim, height=300, key="projects")
        
        # ----- CONTACT PART -----
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("Contact Me")
            st.write("##")
            clicked = clickable_images(
                ["https://cdn-icons-png.flaticon.com/512/25/25231.png",
                 "https://cdn-icons-png.flaticon.com/512/732/732200.png",
                 "https://cdn-icons-png.flaticon.com/512/3536/3536505.png",
                 "https://cdn-icons-png.flaticon.com/512/5968/5968830.png",
                 ],
                titles=["Github","Mail","LinkedIn","X"],
                div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#fafafa"},
                img_style={"margin": "15px", "height": "100px"},
            )

            # st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
            if clicked > -1 and clicked!= 2:
                webbrowser.open(["https://github.com/yAquila/", "mailto://yusufkartal2004@gmail.com", "", "https://twitter.com/yusufkartal2004"][clicked])
            elif clicked == 2:
                st.toast(":grey[Coming soon...]")
            # for i, s in enumerate(st.columns(5)):
            #     s.image(contact_logo_list[i],width=100)
        with right_column:
            st_lottie(lottie_contact_anim, height=300, key="contact")

        

def main_page():
    set_config()
    set_header()
    set_body()

main_page()