# DiaControl
Prediction risk of re-hospitalization in diabetic patients
## Table of Content:
1)  Motivation and solution - Decrease the potentially preventable hospital stays by chornic diabetes control.
2)	Getting the data - Fliter the Diabetes 130-US hospitals for years 1999-2008 Data Set to fit the motivation.
3)	Data preprocessing – Date cleanning and feature engineering.
4)	Exploratory data analysis – some insights.
5)	Make predictions – Whether or not a diabetic patient will have further hospital stay.
6)	Conclusions and discussions.
## 1.	Motivation and solution - Decrease the potentially preventable hospital stays by chornic diabetes control.
Every year, trillions of dollars have been spent on hospital care in united states. However, among this huge amount of money, aobut 10% of it should probably be avoided. Among the potential preventable hospital stay, nearly about 2/3 are caused by chornic diseases. This is quite intutive that chornic diseases persit for longer time and therefore is more difficult to be controlled. In all, if both the health providers and the patients can pay moreattention on chronic disease control like setting more regular checks, huge amount of money and lives can be saved.
There is a lot of information we can infer from the electronic health records(EHR) , but on the other side, EHR is always complex and dirty. I cleaned the data and also did feature engineering. At last, I compared several classifiers to predict whether or not a diabetic patient will have further hospital stay. Similar strategy can be applied to other diseases.
## 2.	Getting the data - Extract the interested data from orignial dataset.
Diabetes 130-US hospitals for years 1999-2008 Data Set is publicly accessible from [UCI](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008) machine learning repository. This dataset represents 10 years (1999-2008) of clinical care at 130 US hospitals and integrated delivery networks. Once any kind of diabetes was entered to the system as a diagnosis for the patients, the encounter recodes will be extracted. However, detailed diagnostic information(the meaning and catalog for ICD-9 code) is lacking, which can be found in ICD9 database - [ICD9data.com](http://www.icd9data.com/2015/Volume1/default.htm). Therefore, I used this database to map ICD codes into specfic diseasesa and catalogs. More specifically, a diabetic patient might visit hospital with other reason (heart disease, ect) and our purpose is predicting the risk of re-admission for diabeitc patient. Therefore, we extracted all the encounter recodes that have diabetic diagnosis(ICD-9 code: 250.*)for our specific purpose. In addition, we also download the categorical prevention tips from [HealthDate.gov](https://www.healthdata.gov/dataset/diabetes-type-2-prevention-tips) for further construction of interactive apps. Ipython notebook used to interpret and fliter data can be found [here](https://github.com/zhihuaqi/DiaControl/blob/master/ipython_notebook/getting_the_data.ipynb). All the data can be found [here](https://github.com/zhihuaqi/DiaControl/tree/master/data)
## 3. Data preprocessing – Date cleanning and feature engineering.
Before we move action to actual modeling, preproessing with the data is always required. We applied several types of methods here:

1. Cleaning tasks such as dropping bad data, dealing with missing values.
2. Creation new features from existing ones
3. Modification of existing features e.g. standardization, log transforms etc.
4. remove 19 medications, but remain insulin.

Ipython notebook used to preprocess data can be found [here](https://github.com/zhihuaqi/DiaControl/blob/master/ipython_notebook/data_processing.ipynb).
## 4. Exploratory data analysis – some insights.
Before we using our data for the model training, we visualized some statistical results  with the preprocessed data,, in order to find further hints on feature engineering.
Inpatient visits last year have different behaviors in different admission groups
Ipython notebook used to preprocess data can be found [here](https://github.com/zhihuaqi/DiaControl/blob/master/ipython_notebook/data_processing2.ipynb).
## 5. Make predictions – Whether or not a diabetic patient will have further hospital stay.
After balancing data by downsampling the marjority class, I fitted the model using Random Forest, and got reasonal precision and recall.
Ipython notebook used to fit model can be found [here](https://github.com/zhihuaqi/DiaControl/blob/master/ipython_notebook/prediction.ipynb).

