from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import itertools

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

        yield [user_id,list(unique_biz_ids)]

    def aggregate_biz_ids(self,user_id,unique_biz_ids):

        yield ["key", [user_id,list(unique_biz_ids)]]

    def output_jaccard_similarity(self, key, unique_biz_ids):
        pairs = list(itertools.combinations(list(unique_biz_ids),2))
        for p in pairs:
                a = set(p[0][1])
                b = set(p[1][1])
                user_id_1 = p[0][0]
                user_id_2 = p[1][0]
                jaccardCoefficient = (float(len(a&b)))/(float(len(a|b)))
                if jaccardCoefficient >= 0.50:
                        yield [str(user_id_1), str(user_id_2)],jaccardCoefficient

    def steps(self):
        return [self.mr(self.extract_biz_ids, self.count_biz_ids),
                self.mr(self.aggregate_biz_ids, self.output_jaccard_similarity)]

if __name__ == '__main__':
    UniqueReview.run()
