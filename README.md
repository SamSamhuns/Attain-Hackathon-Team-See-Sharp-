<img src="https://github.com/SamSamhuns/predemic/blob/master/predemic_logo.jpg" width="400" height="200" />

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2d8205ea39894ef7b3f943c27ff82299)](https://www.codacy.com/app/samhunsadamant/predemic?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SamSamhuns/predemic&amp;utm_campaign=Badge_Grade)

Python scikit based application to make predictions on the likelihood of outbreaks of epidemics based on past epidemic and pandemic data from the WHO.

This project uses a supervised machine learning model that uses a SVM with Radial Basis Function from the scikit library.

All training data and python files are inside src folder.

## Setup and Installation
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Training
The machine learning algorithm has to be trained before being used to predict probability of future outbreaks. All source files in `src`.
```shell
$ python3 svm.py
```

## Testing
```shell
$ python3 clf.py
```

Results are outputted in the terminal from 0 - being least likely to 4 - being most likely.

For a list of all nations, check `dict.json`.

For the list of all regions, check `region.json`.

### Acknowledgments
*   Attain Consulting VA, USA
*   Teammates for this project during the Hackathon Jeanie, Tianchu, and Fang
