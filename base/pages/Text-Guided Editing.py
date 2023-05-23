import os
import numpy as np
from PIL import Image
import streamlit as st
import torch
import clip

from utils.inverter import StyleGANInverter
from utils.visualizer import resize_image

st.title("Text-Guided Editing of Images")
uploaded_file = st.file_uploader("Choose Image (If 'Man' Mode)", type="jpg")
mode_select = st.selectbox('Mode', ('Generation', 'Manipulation'))
mode = "gen"
if mode_select == 'Generation':
  mode = "gen"
else:
  mode = "man"
description = st.text_input('Description', 'she is young')
step = st.slider('Iteration :', min_value=10, max_value=1000, value=200)
n_lr = st.slider('Learning Rate (10^-n) : ',
                 min_value=1, max_value=5, value=2)
learning_rate = 10**(-n_lr)
clip_loss = st.slider('Clip loss weight :', min_value=0.1,
                      max_value=10.0, value=2.0, step=0.01)
lambda_feat = st.slider('Perceptual Lost Weight (5*10^-n) : ', min_value=1.0,
                        max_value=7.0, value=5.0, step=1.0)
loss_weight_feat = 5*10**(-lambda_feat)
loss_reconstruction = st.slider('Reconstruction loss weight :', min_value=0.1,
                        max_value=10.0, value=1.0)
loss_enc = st.slider('Encoding loss weight :', min_value=0,
                       max_value=10, value=2, step=1)

st.markdown("Summary : ")
st.write("Total iteration :", step)
st.write("Learning Rate :", learning_rate)
st.write("Clip Loss :", clip_loss)
st.write("Perceptual Lost Weight :", loss_weight_feat)
st.write("Reconstruction Lost Weight :", loss_reconstruction)
st.write("Encoding Lost Weight :", loss_enc)

model_name = 'styleganinv_ffhq256'

os.environ["CUDA_VISIBLE_DEVICES"] = '0'

def main():
  """Main function."""

  inverter = StyleGANInverter(model_name, 
      mode=mode,
      learning_rate=learning_rate,
      iteration=step,
      reconstruction_loss_weight=loss_reconstruction,
      perceptual_loss_weight=loss_weight_feat,
      regularization_loss_weight=loss_enc,
      clip_loss_weight=clip_loss,
      description=description)
  image_size = inverter.G.resolution

  text_inputs = torch.cat([clip.tokenize(description)]).cuda()

  # Invert images.
  # uploaded_file = uploaded_file.read()
  if uploaded_file is not None and mode=='man':
    image = Image.open(uploaded_file)
    if mode == "man":
      st.image(image, caption='Uploaded Image.', use_column_width=True)
      st.write("")
    st.write("Just a second...")

    image = resize_image(np.array(image), (image_size, image_size))
    _, viz_results = inverter.easy_invert(image, 5)
    final_result = np.hstack([viz_results[1], viz_results[-1]])
  elif mode=='gen':
    _, viz_results = inverter.easy_invert(None, 5)
    final_result = np.hstack([viz_results[1], viz_results[-1]])


  # return final_result
  if final_result is not None:
    with st.container():
        st.image(final_result, use_column_width=True)

if st.button("Generate Result", use_container_width=True):
  main()
  
