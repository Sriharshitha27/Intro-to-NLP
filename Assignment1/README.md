# READ ME

* Source code: src/language_model.py

* Data used: Health corpus and Technical corpus in /data folder

* Language Models:
> On Health domain corpus

>>  LM 1 : tokenization + 4-gram LM + Kneyser Ney smoothing
>> LM 2 : tokenization + 4-gram LM + Witten Bell smoothing

>  On Technical domain corpus
>> LM 3 : tokenization + 4-gram LM + Kneyser Ney smoothing
>> LM 4 : tokenization + 4-gram LM + Witten Bell smoothing

* Outputs: of above mentioned LMs when run on test and train corpuses are in  /output_files

**Directions to run the code**

```
$ python3 language_model.py <smoothing_type> <path_corpus>
```

* 'Smoothing type' takes only 2 values: k for Kneyser-Ney model and w for Witten-Bell model
for eg: ./Health_English.txt

* After running the code: A prompt appears to enter the sentence to be modelled. Give an
input sentence.

**Output of the code**

```
The code outputs the number of unigrams, bigrams, trigrams, and quadgrams in the
given corpus. It gives the probability of the sentence. It also computes and
outputs the perplexity of the sentence.
```
## Libraries used

```
regex
string
itertools
sys
```

Other details regarding the formulae used for the implementation of Kneyser-Ney and
Witten-bell and computation of perplexity are written in the report along with the
experiments conducted, parameters chosen, and results obtained.


