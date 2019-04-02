import gensim
import codecs, argparse, time

start_time = time.time()


''' GET ARGS '''


parser = argparse.ArgumentParser()
parser.add_argument('-data', type = str, help = "Specify data path")
parser.add_argument('-output', type=str, help="Specify output location")
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
    print ('\nModel initialized' )

    print('\nInitialize vocabulary on whole corpus')
    try:
        vocab_file = codecs.open(args.data, 'r', encoding='utf-8')
    except (IOError, OSError):
        print('The file doesn\'t exist!')
        raise SystemExit

    vocab_sentences = gensim.models.word2vec.LineSentence(vocab_file)
    model.build_vocab(vocab_sentences)
    print ('\nVocabulary is ready')

    sentences = gensim.models.word2vec.LineSentence(args.data)
    print ('\nStart training')
    model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
    print ('\nTraining done')

    print('\nSave Vectors')
    model.wv.save_word2vec_format(args.output + args.data.split('/')[-1].split('.')[0] + '.w2v')

    print('\nSave Model')
    model.init_sims(replace=True)
    model.save('{}.model'.format(args.data.split('/')[-1].split('.')[0]))



''' RUN THE CODE '''

if __name__ == "__main__":
    Main()
    print('\nDone! total time elapsed: {0} seconds'.format(time.time() - start_time))