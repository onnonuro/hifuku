# Hifuku: Morphometric Analysis of Sural Nerve Biopsies
Hifuku, meaning 'sural' or 'saphenous' in Japanese, is an open-source machine learning-based software designed for Whole slide Morphometric Analysis in human sural nerve biopsies.



![Alt Text](data/graphical_abstract.jpg)



## General Installation
Clone the Hifuku GitHub repository:
   ```python
   git clone https://github.com/onnonuro/hifuku.git
   ```


## Use Hifuku in Google Colab
Google Colab is the simplest way to utilize Hifuku with GPU support. It is particularly useful for those unfamiliar with coding or lacking a local Python environment. To get started:

      *You need a google account and sign in to Google colab.

1. **Download tutoial.ipynb**: Download [tutoial.ipynb](https://github.com/onnonuro/hifuku/blob/main/tutorial.ipynb).

2. **Upload tutoial.ipynb to your Google Drive**: Upload the file to your [Google Drive](https://www.google.com/drive/).

3. **Open tutoial.ipynb with Google Colab**: Sign in [Google Colab](https://colab.research.google.com/) and open tutoial.ipynb with it.

4. **Run Hifuku**: Follow the instructions in the Jupyter Notebook tutorial.


## Dependencies
Hifuku was tested in the following Google Clolab environment on November 21, 2023.

Python (3.10.12), torch (2.1.0+cu118), torchvision (0.16.0+cu118), torchmetrics (1.2.0), pytorch-lightning (2.1.2), segmentation-models-pytorch (0.3.3), timm (0.9.2), opencv-python (4.8.0.76), albumentations (1.3.1)


## Citation
Automated Whole Slide Morphometrics of Sural Nerve Biopsy by Machine Learning
