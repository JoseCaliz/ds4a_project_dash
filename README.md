# Analysing Crime Trends in Colombia

Codebase of the DS4A Final Project, by Team-79 * Cáliz José, De la Cruz Camilo, Garzón Carolina, Portela Cristian, Toledo-Cortés Santiago. "Analyzing crime trends in Colombia". Bogotá, Colombia 2020.


## Abstract

Crime and violence are undoubtedly two of the main concerns of all citizens around the world, these acts that harm not only the victim but also the community and the Nations.  It generates a great impact on our society, so one of the main challenges of different governments and societies is to combat and improve statistics on the subject improving public policies and police action.

Unfortunately in Colombia the situation is not far away, the high levels of crime and violence have been for a long time making it one of the most violent countries in the region, these issues have also been one of the main challenges of governance for the country over time.  The explanation of the different factors that influence this problem can provide us with a complete view of the behaviour of security problems in the country, thus generating great importance in the development and study of the subject.


## Requirements


Python requirements:

- Python >= 3.6
- Prophet
- Scikit-learn >= 0.23.1


## Preprocessing and EDA

We used data provided by the police department that includes multiple crimes from 2010-2019 by city and neighborhood. The data can be found here: https://www.policia.gov.co/grupo-informaci%C3%B3n-criminalidad/estadistica-delictiva. For each crime, you need to download every CSV file from 2010 to 2019. Preprocessing and Exploratory Data Analisis procedure is detailed in the notebooks from `EDA` folder

 
## Hybrid model for Crime Probability Estimation

The Hybrid model for Crime Probability Estimation is based on Time Series forecasting using Prophet (https://facebook.github.io/prophet/) and probability estimation using Multinomial Naive Bayes (https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html). Training procedure and evaluation details can be found in `models` folder. In that folder, you will also find experiments performed with Kernel Density Estimation, although it was not used in the final model.


## Web App

Web were developed using flask and dash using CSS to customize all related aspects like colors and the way the items are displayed to ensure a good user experience. Dashboard scripts are available at `pages` folder.