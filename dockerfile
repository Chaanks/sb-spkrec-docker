FROM continuumio/miniconda3:4.10.3p0-alpine
LABEL Maintener="jarod.duret@univ-avignon.fr"

WORKDIR /usr/src/app

# Update and install dependencies
RUN apk update && apk add --quiet gcc build-base alpine-sdk

# Create conda env
COPY environment.yml .
RUN . /opt/conda/etc/profile.d/conda.sh \
    && conda env create -f environment.yml --quiet

SHELL ["conda", "run", "-n", "SPKREC", "/bin/bash", "-c"]
RUN echo "Make sure pytorch is installed:"
RUN python -c "import torch; print(torch.__version__)"

# Run TTS server
COPY server .
ENTRYPOINT ["conda", "run", "-no-capture-output", "-n", "SPKREC", "python", "server.py"]