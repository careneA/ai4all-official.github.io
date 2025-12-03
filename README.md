# Ethical Investment - INVESTHIC

INVESTHIC is an AI-powered tool designed to help investors make ethical, socially responsible, and data-driven trading decisions. Using financial news sentiment analysis, ESG (Environmental, Social, Governance) metrics, and ROI projections, INVESTHIC provides a transparent, interactive platform to evaluate companies for responsible investing.

This project was developed as part of the AI4ALL Ignite Accelerator, where we applied Python, NLP, supervised machine learning, and financial modeling to create a comprehensive ESG + ROI analysis pipeline.


## Problem Statement <!--- do not change this line -->

With increasing awareness of the societal and environmental impacts of financial decisions, investors need tools that go beyond profit maximization. Current trading models often ignore ethical considerations and fail to integrate ESG performance into financial decision-making.

Objective: To develop a supervised learning-based system that evaluates companies for ESG compliance and predicts potential ROI, helping investors align financial returns with ethical responsibility.

## Key Results <!--- do not change this line -->

1. Successfully cleaned and aggregated financial news headlines, sentiment data, and ESG metrics for 1,000+ companies over 2008–2024.

2. Engineered NLP-based features from headlines, including:

   - ESG keyword counts

   - TF-IDF + dimensionality reduction via SVD

3. Developed a mapping system to connect headlines to company entities using literal and fuzzy string matching.

4. Built df_features_ready.csv, a unified dataset combining:

   - ESG scores

   - Financial metrics

   - NLP-based ethical signals

5. Created an interactive Gradio application for:

   - ESG score checking

   - ROI prediction with user-defined investment parameters

6. Established a preliminary ROI model integrating profit margin, growth rate, and ESG adjustment, projecting future investment returns.

## Methodologies <!--- do not change this line -->

(UPDATE IN README.md)

*EXAMPLE:*
*To accomplish this, we utilized the OpenAI API to interact with ChatGPT, and we designed a custom Python script to generate diverse prompts and collect corresponding responses. The data was then processed and analyzed using pandas, enabling us to detect patterns and biases in the AI model's outputs.*
*Engineered a Python script to generate over 1,000 prompts and elicit their responses from ChatGPT, utilizing pandas to collect the data. When prompted for solutions to this specific relevant crisis, nearly 80% of ChatGPT's responses promoted a certain worldview.*


To build INVESTHIC, we followed a data science and machine-learning workflow, combining financial datasets, ESG records, and large-scale news text into a unified predictive and ethical analysis engine.

The process began with collecting and cleaning three core datasets: historical S&P 500 news headlines, company ESG performance metrics, and sentiment-labeled financial text. Each dataset required extensive preprocessing. Headlines were cleaned, normalized, and transformed using natural language processing techniques. ESG data was standardized to ensure consistent company identifiers, while sentiment text was mapped into numerical signals.

Next, we engineered features that could quantify both financial signals and ethical indicators. Using TF-IDF and dimensionality reduction (SVD), we converted raw headlines into 50 dense semantic features. We also computed ESG-specific keyword frequencies and headline-level metadata such as length and sentiment. These features were then aggregated by date or by company-date, depending on the ability to match companies reliably through literal and fuzzy text matching.

To merge ethical and financial perspectives, we integrated the engineered NLP features with ESG performance records, enabling the model to capture how sustainability practices and news narratives jointly influence market outlook.

For the predictive component, we built an optional supervised model that estimates a company’s 21-day forward stock return using LightGBM and time-series cross-validation. When price data is not available, the pipeline instead produces a ready-to-use feature table for further modeling.

Finally, we built an interactive user interface using Gradio. Users can check a company’s ESG score or calculate projected ROI based on financial fundamentals, growth expectations, and ESG-adjusted risk factors. This interface makes the model accessible, interpretable, and directly actionable for ethical retail investors.

Throughout the project, ChatGPT served as a technical assistant for code suggestions, debugging, and architectural refinement. Which allowed rapid iteration and increased reliability in the design workflow.

## Data Sources <!--- do not change this line -->

   - S&P 500 Financial News Headlines
   
   - Sentiment Analysis of Financial News
   
   - S&P 500 ESG & Financial Performance
   
   - Additional ESG Metrics Dataset

## Technologies Used <!--- do not change this line -->

(UPDATE IN README.md)
List the technologies, libraries, and frameworks used in your project.

   - Programming & Data Analysis: Python, pandas, numpy
   
   - Natural Language Processing: NLTK, scikit-learn (TF-IDF, SVD)
   
   - Machine Learning: LightGBM, TimeSeriesSplit
   
   - String Matching: RapidFuzz
   
   - Visualization: matplotlib, seaborn
   
   - Interactive UI: Gradio
   
   - AI Assistance: ChatGPT (for project guidance, code suggestions, and debugging)
   
   - Model Persistence: joblib

## Authors <!--- do not change this line -->

(UPDATE IN README.md)
List the names and contact information (e.g., email, GitHub profiles) of the authors or contributors.

*EXAMPLE:*
*This project was completed in collaboration with:*
- *Carene Kouassi (aakoua27@colby.edu)*
- *Glory Ndubuisi Oluavu ([gloryn1@umbc.edu])*
