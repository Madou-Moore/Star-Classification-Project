#Star, Galaxy, and Quasar Classification
Overview

This project uses machine learning to classify astronomical objects as stars, galaxies, or quasars using data from the Sloan Digital Sky Survey (SDSS). The goal is to build an end-to-end classification pipeline that includes data collection, preprocessing, feature engineering, model training, and performance evaluation.

This is a supervised multi-class classification problem. The model uses numerical measurements from astronomical survey data and predicts one of three object classes:

STAR
GALAXY
QSO
Project Motivation

Large astronomical surveys collect data for millions of objects in the sky. Manually classifying each object is not practical, so machine learning can be used to automate the process. This project explores how well traditional machine learning models can classify objects using photometric and spectroscopic measurements.

Dataset

The data comes from the Sloan Digital Sky Survey (SDSS), a public astronomical survey database.

The dataset includes features such as:

u, g, r, i, z: photometric magnitude bands
redshift: redshift measurement
class: target label, either STAR, GALAXY, or QSO

The raw data is collected using SQL queries from SDSS. Separate datasets for stars, galaxies, and quasars are merged into one combined dataset. Star-Classification-Project

Feature Engineering

In addition to the original magnitude values, this project creates color-index features by subtracting one magnitude band from another:

u_g = u - g
g_r = g - r
r_i = r - i
i_z = i - z

These features compare brightness across different light filters and may help the model better distinguish between stars, galaxies, and quasars.
