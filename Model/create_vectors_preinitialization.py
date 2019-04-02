import gensim
import codecs, argparse, time

start_time = time.time()


''' GET ARGS '''

parser = argparse.ArgumentParser(description = '')
parser.add_argument('-data_t', type = str, help = "Specify data path")
parser.add_argument('-output', type=str, help="Specify output location")
parser.add_argument('-data_t_minus_1', type = str, help = "")
parser.add_argument('-vectors', type = str, help = "")

parser.add_argument('-sg', type=int, default=1, help="Skipgram or Bag-of-words")
parser.add_argument('-hs', type=int, default=1, help="Hierarchical Softmax")
parser.add_argument('-alpha', type=float, default=0.01, help="Learning Rate")
parser.add_argument('-size', type=int, default=200, help="Vector size")
parser.add_argument('-window', type=int, default=5, help="Window size")
parser.add_argument('-min_count', type=int, default=0, help="Minimum number of occurrences")
parser.add_argument('-iter', type=int, default=5, help="Number of iterations")
args = parser.parse_args()

''' MAIN '''
def Main():
    model = gensim.models.Word2Vec(sg=args.sg, hs=args.hs, alpha=args.alpha, size=args.size, window=args.window, min_count=args.min_count, iter=args.iter)
    print('\nModel initialized')

    print ('\nLoad datat for dataset t-1' )
    sentences_dataset_t = gensim.models.word2vec.LineSentence(codecs.open(args.data_t, 'r', encoding = 'utf-8'))
    '''
    # open and read sentences of the dataset on which vectors for the initializatin where created.
    # NOTE: this has to be done if you want to have a vocabulary in which words of this doc are included
    existing_vecs_file = codecs.open(args.data_existing_vectors, 'r', encoding = 'utf-8')
    sentences_existing_vecs_file = gensim.models.word2vec.LineSentence(existing_vecs_file)
    '''
    # open and read sentences of the General language vocabulary
    # NOTE: this has to be done if you want to have a vocabulary in which words of this doc are included
    sentences_dataset_t_minus_1 = gensim.models.word2vec.LineSentence(codecs.open(args.data_t_minus_1, 'r', encoding = 'utf-8'))

    '''
    # ****** Initialize vocabulary  ******
    # create the voc on the current dataset
    # print('\ninitialize vocabulary on current dataset')
    # model.build_vocab(sentences_current_dataset_file)
    
    # upate the voc on the doc of the existing vecs
    # print('\nupdate voc with file of initialized vectors')
    # model.build_vocab(sentences_existing_vecs_file, update=True)
    '''
    # NOTE: after the meeting with Gemma 23/10,we decided to create the vocabulary only on the base of the words in the general language

    # create the voc ONLY on general langauge
    print('\ncreate the voc ONLY on general langauge')
    model.build_vocab(sentences_dataset_t_minus_1)

    # ****** Train ******

    print ('\nload vecs for pre-initialization' )
    model.intersect_word2vec_format(args.vectors, lockf=1)

    print ('\ntrain' )
    model.train(sentences_dataset_t, total_examples=model.corpus_count, epochs=model.iter)

    # ****** Save ******
    print ('\nsave vectors' )
    model.wv.save_word2vec_format(args.output + args.data_t.split('/')[-1].split('.')[0] + '.w2v')



''' RUN THE CODE '''

if __name__ == "__main__":
    Main()
    print('\nDone! total time elapsed: {0} seconds'.format(time.time() - start_time))