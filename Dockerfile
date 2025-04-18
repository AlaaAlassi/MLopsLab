# Use the official Miniconda base image
FROM continuumio/miniconda3:latest

# Set the working directory in the container
WORKDIR /app

# Copy the environment.yaml file into the container
COPY environment.yaml /app/environment.yaml

# Create the conda environment from the environment.yaml file
RUN conda env create -f environment.yaml

# Activate the environment and ensure it is activated by default
RUN echo "source activate udacity" > ~/.bashrc
ENV PATH /opt/conda/envs/udacity/bin:$PATH