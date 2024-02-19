FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install basic packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libffi-dev \
    libjpeg-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    nodejs \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    unzip \
    vim \
    wget \
    zlib1g-dev

# Install Python packages
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade \
    numpy \
    pandas \
    scipy \
    "scikit-learn<1.4" \
    matplotlib \
    seaborn \
    jupyterlab \
    pyyaml \
    h5py \
    nltk \
    xgboost \
    lightgbm \
    catboost \
    plotly \
    statsmodels \
    opencv-python \
    wordcloud \
    optuna \
    tqdm \
    colorama \
    missingno \
    beautifulsoup4 \
    peewee \
    python-dotenv \
    pillow \
    msal \
    tokenizers \
    imblearn
# Download data for NLTK
RUN python3 -c "import nltk; nltk.download(['names', 'stopwords', 'state_union', 'twitter_samples', 'movie_reviews', 'averaged_perceptron_tagger', 'vader_lexicon', 'punkt'])" \
    && mv /root/nltk_data /usr/local/share/nltk_data

# Skip cache for following
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN rm skipcache

# Frequently updated packages
RUN python3 -m pip install --no-cache-dir --upgrade \
    langchain \
    openai \
    langchain-google-genai \
    codeinterpreterapi \
    langchain_openai
# A simple installation of CoML without Jupyter extensions
RUN git clone -b model-family-support https://github.com/ultmaster/CoML /CoML
RUN python3 -m pip install --no-cache-dir -e /CoML

# Assume the current user to be 1000.
RUN adduser --uid 1000 --disabled-password defaultuser
