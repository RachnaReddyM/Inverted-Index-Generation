import os
import operator

index_unigram= {} # Inverted Index for Unigrams
"""index_bigram={} # Inverted Index for Bigrams
index_trigram={} # Inverted Index for Trigrams
unigram_tf={}  # Unigrams term frequencies
bigram_tf={}  # Bigrams term frequencies
trigram_tf={} # Trigrams term frequencies
unigram_df={} # Unigrams Document frequencies
bigram_df={}  # Bigrams Document frequencies
trigram_df={} # Trigrams Document frequencies
uni_tokens={} # Unigrams- no. of tokens in each document
bi_tokens={} # Bigrams- no. of tokens in each document 
tri_tokens={} # Trigrams- no. of tokens in each document"""

# fetch corups from the below path
docs_source_path = "D:\IR\dummypro\corpus"

# filenamelist contains the list of raw HTML file names
filenamelist = os.listdir(docs_source_path)

# to generate an inverted index
def create_inverted_index():

  for filename in filenamelist:
    content=[]
    name_of_file=filename.split('.txt')
    docID=name_of_file[0]
 
    print docID

    f = open(docs_source_path + '\\' + filename, 'r+')
    raw_data=f.read()
    content=raw_data.split()
    
    ## Unigram-Inverted-Index generation

    unigram_token=[]


    for c in content:

      #if c not in unigram_token:

        # to generate the number of tokens in each document
        #unigram_token.append(c)

      if index_unigram.has_key(c):
        # when this term occurs for the first time in a particular document
        if docID not in index_unigram[c]:
          index_unigram[c].update({docID:1})
        
        else:
          index_unigram[c][docID]+=1

      # if term does not exist in the dictionary yet
      else:
        index_unigram[c]={docID:1}


    #uni_tokens[docID]=len(unigram_token)


    #Bigram-Inverted_Index creation

   """ bigrams_token=[]
    for i,c in enumerate(content):
      next=i+1
      if next < len(content):
      
        term=c+' '+content[i+1]

        if term not in bigrams_token:
          # to generate the number of tokens in each document
          bigrams_token.append(term)

        if index_bigram.has_key(term):

          # when this term occurs for the first time in a particular document
          if docID not in index_bigram[term]:
            index_bigram[term].update({docID:1})
        
          else:
            index_bigram[term][docID]+=1

        # if term does not exist in the dictionary yet
        else:
          index_bigram[term]={docID:1}
      bi_tokens[docID]=len(bigrams_token)

    #Trigram_Inverted_Index creation
    
    trigram_token=[]
    for i,c in enumerate(content):
      next=i+2
      if next < len(content):
      
        term=c+' '+content[i+1]+' '+content[i+2]

        if term not in trigram_token:
          # to generate the number of tokens in each document
          trigram_token.append(term)

        if index_trigram.has_key(term):
          # when this term occurs for the first time in a particular document
          if docID not in index_trigram[term]:
            index_trigram[term].update({docID:1})
        
          else:
            index_trigram[term][docID]+=1

        # if term does not exist in the dictionary yet
        else:
          index_trigram[term]={docID:1}

    tri_tokens[docID]=len(trigram_token)


# to generate the term frequency and document frequency table
def generate_tf_df(index_gram,gram_tf,gram_df):

  for key,value in index_gram.iteritems():
    term_frequency=0
    docString=""
    i=0
    for k,v in value.iteritems():
      i+=1
      term_frequency+=v
      docString+=k

      if(i<len(value)):
        docString+=" "

    no_of_docs=len(value)
    
    # dictionary to hold the term frequencies
    gram_tf[key]=term_frequency

    # dictionary to hold the document frequencies
    gram_df[key]={docString:no_of_docs}

# to sort and write the term frequency table to a file
def generate_tf_table(gram_tf,nof):
  sort_dict=sorted(sorted(gram_tf.iteritems()), key=operator.itemgetter(1), reverse=True)
  
  f=open(nof,"w+")
  for k,v in sort_dict:
    f.write(str(k)+" -------------> "+str(v)+"\n")
  f.close()

# to sort and write document frequency table to file
def generate_df_table(gram_df,nof):
  sort_dict=sorted(gram_df.iteritems(), key=operator.itemgetter(0))
  
  f=open(nof,"w+")
  for k,v in sort_dict:
    df_value=""
    for key,value in v.iteritems():
      df_value=str(key)+" -> "+str(value)

    final_string=str(k)+" ------------> "+df_value+"\n"
    f.write(final_string)
  f.close()"""

# to write the inverted index to a file
def write_index_to_file(dict_gram,nof):
  f=open(nof,"w+")
  for k,v in dict_gram.iteritems():
    value_term=""
    i=0
    for key,val in v.iteritems():
      i+=1
      value_term+="("+str(key)+","+str(val)+")"
      if(i<len(v)):
        value_term+=","

      
    final_term=str(k)+" -----> "+value_term+"\n"
    f.write(final_term)

  f.close()

"""# to write ti no. of tokens dictionary to file
def write_tokens_to_file(grams_tokens,nof):
  token_string=""
  f=open(nof,"w+")

  for k,v in grams_tokens.iteritems():
    token_string+=str(k)+"->"+str(v)+"\n"

  f.write(token_string)
  f.close()"""


def _mainindexer():
  create_inverted_index()
  write_index_to_file(index_unigram,"Task_2_Index_Unigram.txt")
  """write_index_to_file(index_bigram,"Task_2_Index_Bigram.txt")
  write_index_to_file(index_trigram,"Task_2_Index_Trigram.txt")
  write_tokens_to_file(uni_tokens,"Task_2_Unigram_tokens.txt")
  write_tokens_to_file(bi_tokens,"Task_2_Bigram_tokens.txt")
  write_tokens_to_file(tri_tokens,"Task_2_Trigram_tokens.txt")
  generate_tf_df(index_unigram,unigram_tf,unigram_df)
  generate_tf_df(index_bigram,bigram_tf,bigram_df)
  generate_tf_df(index_trigram,trigram_tf,trigram_df)
  generate_tf_table(unigram_tf,"Task 3_Unigram_TF.txt")
  generate_tf_table(bigram_tf,"Task 3_Bigram_TF.txt")
  generate_tf_table(trigram_tf,"Task 3_Trigram_TF.txt")
  generate_df_table(unigram_df,"Task 3_Unigram_DF.txt")
  generate_df_table(bigram_df,"Task 3_Bigram_DF.txt")
  generate_df_table(trigram_df,"Task 3_Trigram_DF.txt")"""

_mainindexer()

        





  