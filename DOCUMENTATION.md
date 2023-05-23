
# TediGAN Streamlit Adaptation

Project ini dibuat untuk menerapkan antarmuka yang lebih user-friendly dalam penerapan TediGAN Framework untuk penghasilan dan manipulasi gambar




## Authors

- [Muhammad Hafizh Auliansyah](https://github.com/HafizhAuliansyah)
- [Jundiy Muhammad Alfatih](https://github.com/jundiyfatih1)
- [Nasrulloh Fajar Muharam](https://github.com/nasrullohfajar)



## Related

Project ini adalah pengembangan dari :

[TediGAN](https://github.com/IIGROUP/TediGAN)


## Running

Untuk melakukan run aplikasi, kami sangat merekomendasikan menggunakan google colab berikut

[![Streamlit Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yNEn1M38_DEyqSAPu49GRJoPCyJ4C-Ze?usp=sharing)

#### Langkah-Langkah

- Instalasi Library Streamlit
```bash
  !pip install -q streamlit
```
- Import Streamlit and Yfinance
```python
    import streamlit as st
    import yfinance as yf
```
- Localtunnel Installtion
```
    !npm install localtunnel
```
- Cloning Repository and Model Preparation
```python
    import os
    os.chdir('/content')
    CODE_DIR = 'TediGAN'
    if not os.path.exists(CODE_DIR):
    !git clone https://github.com/HafizhAuliansyah/TediGAN-Noblesse.git $CODE_DIR
    os.chdir(f'./{CODE_DIR}')
    MODEL_DIR = os.path.join('base', 'models', 'pretrain')
    os.makedirs(MODEL_DIR, exist_ok=True)

    !pip install ftfy regex tqdm
    !pip install git+https://github.com/openai/CLIP.git

    # download pretrained stylegan and encoder
    !wget https://mycuhk-my.sharepoint.com/:u:/g/personal/1155082926_link_cuhk_edu_hk/EXqix_JIEgtLl1FXI4uCkr8B5GPaiJyiLXL6cFbdcIKqEA?e=WYesel\&download\=1 -O $MODEL_DIR/styleganinv_ffhq256_encoder.pth  --quiet
    !wget https://mycuhk-my.sharepoint.com/:u:/g/personal/1155082926_link_cuhk_edu_hk/EbuzMQ3ZLl1AqvKJzeeBq7IBoQD-C1LfMIC8USlmOMPt3Q?e=CMXn8W\&download\=1 -O $MODEL_DIR/styleganinv_ffhq256_generator.pth  --quiet
    !wget https://mycuhk-my.sharepoint.com/:u:/g/personal/1155082926_link_cuhk_edu_hk/EQJUz9DInbxEnp0aomkGGzAB5b3ZZbtsOA-TXct9E4ONqA?e=smtO0T\&download\=1 -O $MODEL_DIR/vgg16.pth  --quiet
    !nvidia-smi
```

- Change working directory
```bash
    %cd base
```
- Run streamlit and save streamlit logs.txt
```bash
    !streamlit run main.py &>/content/logs.txt &
```

- Run localtunnel to access streamlit
```bash
    !npx localtunnel --port 8501
```
- Open logs.txt and copy streamlit External URL
![image](https://drive.google.com/uc?export=view&id=1BwI60zsYdJAfzAp42sJh2kCbe9gMiHbq)
- Access the output url from the localtunnel and input the copied IP to form
As Example : https://empty-worlds-rush.loca.lt

- Open tab "Text Guided Editing" on sidebar





## Run Locally

We do not recommend running this application locally, unless you have sufficient specifications

#### _This application cannot be run directly for devices with NVIDIA GPU 4GB, it needs further settings to run it_

We recommend to use conda environment with python 3.9 to run this application

```bash
  git clone https://github.com/HafizhAuliansyah/TediGAN-Noblesse.git
```

Go to the project directory

```bash
  cd TediGAN-Noblesse
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Install pytorch with cudatoolkit via conda, check [Installation Docs](https://pytorch.org/get-started/locally/)

Example: 
```bash
  conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

Go to base directory
```bash
    cd base
```
Run streamlit
```bash
    streamlit run main.py
```


## Screenshots

- Image Manipulation
![image](https://drive.google.com/uc?export=view&id=1utK5yhG6AlwEUrbQQmCLRrqxxuHuvTs_)
Result :
![image](https://drive.google.com/uc?export=view&id=1II1EIUNw4c1m4J-4V1HZbBfPiq4ThYDn)
- Image Generation
![image](https://drive.google.com/uc?export=view&id=1dcJVs2q4P4HGYRyWkUKO-x7vn8nGD_eZ)
Result :
![image](https://drive.google.com/uc?export=view&id=1YQzi2GF1tKl36-QCRCCAXHLGIeg1aE5J)
