FROM continuumio/miniconda3:latest

WORKDIR /app

# Copy environment.yml
COPY environment.yml .

# Create the conda environment
RUN conda env create -f environment.yml && conda clean -a -y

# Copy the app
COPY . .

# Activate the environment and set PATH
ENV PATH /opt/conda/envs/LLM_qattan/bin:$PATH

# Verify the environment is set up correctly
RUN echo "Python path: $(which python)" && \
    echo "Python version: $(python --version)" && \
    python -c "import requests; print('requests is available')"

EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]