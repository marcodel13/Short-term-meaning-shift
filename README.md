# Short-Term Meaning Shift: A Distributional Exploration


## Overview  

This directory contains the code and data used for the experiments prensented in the paper [Short-Term Meaning Shift: A Distributional Exploration](https://arxiv.org/abs/1809.03169), to appear in the Proceedings of NAACL-HLT 2019. 

We release the following material:

- Our implementation of the model introduced by [Kim et. al (2014)](https://www.aclweb.org/anthology/W14-2517) for creating time dependent word representations, see `./Model/`. 
- The dataset annotated by users of the subbredit [r/LiverpoolFC](https://www.reddit.com/r/LiverpoolFC/) that we used for our experiments, see `./Dataset/`.

###  Requirements:

In order to run the model, Python 3 is required. You can install all the required packages using the following command:

    $ pip install -r requirements.txt


###  Running the code:

To create word embeddings without any kind of pre-initialization use the following command:     

    python3 create_vectors.py -data <data_file> -output <output_directory>

In order to initialize the word embeddings for time bin _t_ with those in _t-1_ use this command:

    python3 create_vectors_preinitialization.py -data_t <data_file_for_time_t> -data_t_minus_1 <data_file_for_time_t-1> -vectors <vectors computed for t-1> -output <output_directory> 

For both files, it is possible to pass as arguments the hyperparameters of the model.

###  Dataset:

The dataset is provided in the in two files: 


- `./Dataset/annotated_words.xls`: the annotation by the redditors. For each word, there are two columns: change/no change/ 
- `./Dataset/contexts.txt`: the examples showed to the redditors. 
 


## References
If you use this code or dataset, please cite the following paper:
~~~~
@booktitle{del2019short-term,
  title={{S}hort-{T}erm {M}eaning {S}hift: {A} {D}istributional {E}xploration},
  author={Del Tredici, Marco and Fern{\'a}ndez, Raquel and Boleda, Gemma},
  journal={in Proceedings of NAACL-HLT 2019 (Annual Conference of the North American Chapter of the Association for Computational Linguistics)},
  year={2019},
  note = {To appear}
}
~~~~