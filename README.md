
# README.md

## Hifuku: Automated Morphometric Analysis of Sural Nerve Biopsies
Hifuku is a machine learning-based opensource software which enables Automated Morphometric Analysis in human sural nerve specimens

Hifuku, means ‘sural’ or “saphenous” in Japanese

### Usage

#### Installation and Setup in Google Colab
Google Colab provides an easy-to-use environment for running Hifuku, especially for those who are not familiar with coding or do not have a local Python environment set up. Follow these steps to get started:

1. **Open Google Colab**: Visit [Google Colab](https://colab.research.google.com/) and sign in with your Google account.

2. **Create a New Notebook**: Click on 'New Notebook' to start a fresh environment.

3. **Install Dependencies**: In a new cell, paste and run the following commands to install necessary dependencies:
   ```python
   !pip install opencv-python albumentations pytorch-lightning segmentation-models-pytorch scikit-image
   ```

4. **Clone the Hifuku Repository**: Clone the Hifuku GitHub repository to your Colab environment using:
   ```python
   !git clone https://github.com/onnonuro/hifuku.git
   ```

5. **Navigate to the Hifuku Directory**: Change the current working directory to the Hifuku folder:
   ```python
   %cd hifuku
   ```

6. **Running the Application**: Follow the instructions in the Jupyter Notebook tutorial provided in the repository to run specific analyses.

#### General Installation
For users who prefer to install Hifuku in their local environment:
- **GitHub Repository**: [Hifuku on GitHub](https://github.com/onnonuro/hifuku.git).
- **Dependencies**: Ensure you have Python installed along with `opencv-python`, `albumentations`, `pytorch-lightning`, `segmentation-models-pytorch`, and `scikit-image`.
