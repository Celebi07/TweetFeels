# TweetUpLift
Chrome extension to analyze and perform sentiment analysis of  your twitter profile and give points accordingly.

# Twitter Sentiment Analyzer Chrome Extension

This Chrome extension allows users to analyze and perform sentiment analysis of their Twitter posts. It provides sentiment labels of the user's tweets, which can be used to assess their mental health.

## Features

- Analyze the sentiment of a user's Twitter profile.
- Give Sentiment Labels to the user based on the sentiment of their tweets.
- Provide an overall mental health assessment based on the accumulated points.

## Prerequisites

Before using the extension, you need to have the following:

- Google Chrome browser installed on your computer.

## Utilities

The Twitter Sentiment Analyzer Chrome Extension utilizes several utility libraries and tools for data analysis, visualization, and machine learning. Here are the key utilities used in this project:

- **NumPy**: A powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

- **Pandas**: A popular data manipulation and analysis library. It provides data structures like DataFrames for efficient data handling, along with a wide range of functions for data cleaning, transformation, and exploration.

- **Seaborn**: A Python data visualization library based on Matplotlib. Seaborn provides a high-level interface for creating informative and visually appealing statistical graphics.

- **WordCloud**: A library for generating word clouds from text data. Word clouds are visual representations of text, where the size of each word corresponds to its frequency or importance.

- **Matplotlib**: A comprehensive plotting library in Python. Matplotlib allows you to create a wide variety of static, animated, and interactive visualizations.

- **NLTK**: The Natural Language Toolkit (NLTK) is a library for working with human language data. It provides various tools and resources for tasks such as tokenization, stemming, lemmatization, part-of-speech tagging, and more.

- **LogisticRegression**: A classifier model from the scikit-learn library. Logistic regression is a common algorithm used for binary classification tasks, where the goal is to predict one of two possible outcomes.

- **TfidfVectorizer**: A feature extraction technique used to convert text data into numerical representations. The TfidfVectorizer calculates the Term Frequency-Inverse Document Frequency (TF-IDF) value for each word in the text, which helps to capture the importance of each word in the document.

These utilities are essential for performing sentiment analysis, data visualization, and machine learning tasks within the Twitter Sentiment Analyzer Chrome Extension.


## Installation

To install the Twitter Sentiment Analyzer Chrome Extension, follow these steps:

1. Clone the repository:
   ```bash
   git clone (https://github.com/Celebi07/TweetFeels.git)
   ```

2. Open Google Chrome and navigate to `chrome://extensions`.

3. Enable "Developer mode" by toggling the switch at the top right corner of the page.

4. Click on the "Load unpacked" button.

5. Select the cloned repository folder (`twitter-sentiment-analyzer`) and click "Open".

6. The extension should now be added to Chrome, and you should see its icon in the toolbar.

## Configuration

To configure the extension and set up your Twitter API credentials, follow these steps:

1. Open the extension by clicking on its icon in the toolbar.

2. Click on the "Settings" button.

3. Enter your Twitter API credentials:
   - Consumer Key
   - Consumer Secret
   - Access Token
   - Access Token Secret

4. Click "Save" to store the credentials.

## Usage

To analyze your Twitter profile and assess your mental health, follow these steps:

1. Make sure you are logged into your Twitter account in the browser.

2. Click on the extension icon in the toolbar.

3. Click on the "Analyze Profile" button.

4. The extension will fetch your tweets and perform sentiment analysis.

5. Once the analysis is complete, the extension will assign points to each tweet based on sentiment and calculate an overall mental health score.

6. The mental health score will be displayed along with a summary of the analysis.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.

2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:
   ```bash
   git commit -m "Add your commit message"
   ```

4. Push your changes to the forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request on the original repository and describe your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The sentiment analysis algorithm used in this extension is [Logistic Regression]

Feel free to customize and enhance the extension to suit your needs. If you have any questions or encounter any issues, please submit them to the GitHub repository's issue tracker.
