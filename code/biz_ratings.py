from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

class AverageStars(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol
   
    #Map
    def extract_category(self, _, record):
        """Take in a record, filter by type=review, yield <category, [stars, review_count]>"""
        if record['type'] == 'business':
		for c in record['categories']:
                	yield c, [record['stars'],record['review_count']]

    #Reduce
    def average_stars(self,category, stars):
	"""Take in the category and stars, yield <category, average review stars>"""
	star_list = list(stars)	
	
	'''The value in the key, value pair is the output of this equation: 
	sum(stars*review_count)/sum(review_count) which is the average stars of all 
	reviews for a particular category'''
	yield category, str(sum([s[0]*s[1] for s in star_list])/sum([s[1] for s in star_list]))

    #MapReduce Steps
    def steps(self):
	return [self.mr(self.extract_category, self.average_stars)]

if __name__ == '__main__':
    AverageStars.run()
