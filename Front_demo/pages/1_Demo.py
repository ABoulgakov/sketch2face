import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(layout="wide")


image_element = Image.open('./photo_element.jpeg')

st.title("Sketch 2 face :pencil2: :red_haired_person:")

checkbox_crazy = st.checkbox("Crazy mode :balloon:")

tab1, tab2 = st.tabs(["My own sketch :sunglasses:","A normal sketch"])

with tab1 :
    col1, col2= st.columns([0.5,0.5], gap ="small")

    with col1:
        with st.sidebar:
                    drawing_mode = st.selectbox(
            "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform"))
                    stroke_width = st.slider("Stroke width: ", 1, 25, 3)

                    if drawing_mode == 'point':
                        point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)

                    stroke_color = st.sidebar.color_picker("Stroke color hex: ")
                    bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
                    bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
                    realtime_update = st.sidebar.checkbox("Update in realtime", True)

        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            background_image=Image.open(bg_image) if bg_image else None,
            update_streamlit=realtime_update,
            height=500,
            width = 500,
            drawing_mode=drawing_mode,
            point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
            key="canvas",
            )

    with col2 :
        image_element_place_first = st.empty()

    generate_from_drawing = st.button("Generate image", type ="primary", key="drawing")

with tab2 :
    col1, col2= st.columns([0.5,0.5], gap ="small")

    with col1:
        st.file_uploader("Import your sketch", type = ["png","jpg"])
    with col2 :
        image_element_place_second = st.empty()

    generate_from_file = st.button("Generate image", type ="primary", key ="file")


#create an image from a drawing

if generate_from_drawing:

    st.balloons()
    with image_element_place_first.container():
        st.write("blabla")
        st.image(image_element, width  = 350)

else :
    with image_element_place_first.container():
        a, b, c = st.columns([0.1,0.6,0.1])
        with b:
            st.image(image_element, width  = 350)


#create an image from a sketch

if generate_from_file :
    st.balloons()

    with image_element_place_second.container():
        st.write("blabla")
        st.image(image_element, width  = 350)

else :
    with image_element_place_second.container():
        a, b, c = st.columns([0.1,0.6,0.1])
        with b:
            st.image(image_element, width  = 350)
