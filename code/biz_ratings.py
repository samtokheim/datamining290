from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

class AverageStars(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol
   
    #Map
    def extract_category(self, _, record):
        """Take in a record, filter by type=review, yield <category, stars>"""
        if record['type'] == 'business':
		"""Yield each category in the category list"""
		for c in record['categories']:
                	yield c, record['stars']

    #Reduce
    def average_stars(self,category, stars):
	"""Take in the category and stars, yield <category, average stars>"""
	star_list = list(stars)
        yield str(category), str(sum(star_list)/len(star_list))
    
    #MapReduce Steps
    def steps(self):
	return [self.mr(self.extract_category, self.average_stars)]
	
if __name__ == '__main__':
    AverageStars.run()
