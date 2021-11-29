
# Fake News Detection
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)<br>
The primary objective of this project is simple, flagging fake news. This is done utilising various Deep Learning algorithms and generic classifiers. The best performing algorithm is then deployed using Flask.


## Authors

- [@shinjondas](https://github.com/shinjondas/)
- [@akshatvid](https://github.com/akshatvid)
- [@akashshukla09](https://github.com/AkashShukla09)


## Models Used

- [Logistic Regression](https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc)
- [Random Forest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)
- [Decision Tree](https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052)
- [ANN](https://www.datasciencecentral.com/profiles/blogs/artificial-neural-network-ann-in-machine-learning) (Artificial Neural Network)
- [LSTM](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21) (Long Short Term Memory)
## Dataset

The [dataset](https://github.com/shinjondas/fake-news-detection/tree/main/data) consists of   23481 fake news articles and 21417 true news articles which can be combined to create the training dataset for the algorithm. 
## Requirements
- Tensorflow
- scikit-learn (v0.22.1)
- Pandas
- Numpy
- Flask
