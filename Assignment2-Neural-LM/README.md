## READ ME

* Source code: src/language_model.ipynb

* Data used: brown.txt in /data folder

* Language Models:
> On brown corpus

>>  LM 1 : tokenization + 4-gram LM + Kneyser Ney smoothing (From previous assignment)
  
>> LM 2 : tokenization + 4-gram LM + Witten Bell smoothing (From previous assignment) 

>> LM 3 : tokenization + 5-gram LM + LSTM model

* Outputs: of above mentioned LMs, when run on test and train corpora, are in  /output_files


**Directions to run the code**

> Open the notebook in Jupyter notebook or Google Colab.

> Split the data (brown.txt) using create_dataset.py.

> Upload the created text files (if you are using google colab)

> Run each cell till the end.

**Output of the code**

> 2 Files will be created; lstm_test and lstm_train

> These contain the perplexity of each sentence in the test dataset and train dataset respectively.

Other details regarding the NN model, its parameters, and computation of perplexity are written in the report along with the
results obtained.

