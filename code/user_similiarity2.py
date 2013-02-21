from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re

WORD_RE = re.compile(r"[\w']+")

class UniqueReview(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def extract_biz_ids(self, _, record):
        """Take in a record, filter by type=review, yield <user_id, business_id>"""
        if record['type'] == 'review':
        	yield str(record['user_id']),str(record['business_id'])

    def count_biz_ids(self,user_id, biz_ids):
	unique_biz_ids = set(biz_ids)

	yield [str(unique_biz_ids),str(user_id)],[str(unique_biz_ids),str(user_id)]

    def calc_jaccard_similarity(self, set1, set2):
	
	for s in set2:
		a = set(set1[0])
		b = set(set2[0])
		jaccardSimilarity  = (float(len(a & b)) / float(len(a|b)))
		if jaccardSimilarity >= 0.50:
			yield [set1[1],set2[1]],jaccardSimilarity
	
    def output_jaccard_similarity(self, user_ids, jaccardSimilarity):
	yield [str(user_ids[0]),str(user_ids[1])],str(jaccardSimilarity)

    def steps(self):
    	return [self.mr(self.extract_biz_ids, self.count_biz_ids),
		self.mr(self.calc_jaccard_similarity),
		self.mr(self.output_jaccard_similarity)]

if __name__ == '__main__':
    UniqueReview.run()
