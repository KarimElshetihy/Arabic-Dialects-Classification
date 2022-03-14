# Arabic-Dialects-Classification
### By Karim Elshetihy


###### The Dataset:
The dataset and the dialect identification problem were addressed by Qatar Computing Research Institute, moreover, they published a paper, feel free to get more insights from it Here.

We are given a dataset which has 2 columns, id and dialect.

Target label column is the dialect*, which has 18 classes.
The id column will be used to retrieve the text, to do that, you need to call this API by a POST request.
The request body must be a JSON as a list of strings, and the size of the list must NOT exceed 1000.
The API will return a dictionary where the keys are the ids, and the values are the text, here is a request and response sample.
