from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from itertools import combinations_with_replacement, combinations
import json
import math

class BusinessSim(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    # go through each review - if the business category is in businesses dict, yield the business_id and the word.
    def get_words(self, _, record):
        #record = json.loads(record)
        if record['type'] == 'review':
            words = record['text'].split()
            for word in words:
                yield record['business_id'], word

    # create word set for each business_id
    def get_word_set(self, business_id, words):
        words_list = set(words)
        #yield str(business_id), str(set(words_list))
        yield business_id, list(words_list)
  
    
    # combine both inputs into output value     
    def combine_review_words(self, business_id, review_words):
        yield 'foo', [business_id, review_words]             
            
    # compare word lists for each business       
    def compare_businesses(self, _, business_reviews):

        for biz1, biz2 in combinations(business_reviews, 2):
            
            all_words = (set(biz1[1] + biz2[1]))
            jaccard_denom = len(all_words)           
            
            common_words = (set(biz1[1]) & set(biz2[1]))            
            jaccard_numer = len(common_words)
            
            jaccard_coefficient = float(jaccard_numer) / jaccard_denom
       
   	    yield 'foo', jaccard_coefficient		
    
    
    def steps(self):
               
        return [self.mr(mapper=self.get_words, reducer=self.get_word_set), 
                self.mr(mapper=self.combine_review_words, reducer=self.compare_businesses)]
   
if __name__ == '__main__':
	BusinessSim.run()
