#!/usr/bin/python
import sys
# append facerec to module search path
sys.path.append("../../facerec/")
# import facerec stuff
from facerec.dataset import DataSet
from facerec.feature import Fisherfaces
from facerec.distance import EuclideanDistance, CosineDistance
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.validation import KFoldCrossValidation
from facerec.visual import subplot
from facerec.util import minmax_normalize
import PIL.Image as Image
# import numpy
import numpy as np
# import matplotlib colormaps
import matplotlib.cm as cm
# import for logging
import logging,sys
class recdb:
	def __init__(self):
# set up a handler for logging
		self.handler = logging.StreamHandler(sys.stdout)
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.handler.setFormatter(self.formatter)
# add handler to facerec modules
		self.logger = logging.getLogger("facerec")
		self.logger.addHandler(self.handler)
		self.logger.setLevel(logging.DEBUG)
# load a dataset (e.g. AT&T Facedatabase)
		self.dataSet = DataSet("/root/libface/img/yalefaces")
# define Fisherfaces as feature extraction method
		self.feature = Fisherfaces()
# define a 1-NN classifier with Euclidean Distance
		self.classifier = NearestNeighbor(dist_metric=EuclideanDistance(), k=1)
# define the model as the combination
		self.model = PredictableModel(feature=self.feature, classifier=self.classifier)
# show fisherfaces
		self.model.compute(self.dataSet.data, self.dataSet.labels) 
#try to recgonize
	def recpeo(self, filename):
		im = Image.open(filename)
		im = im.convert("L")
		ar = []
		ar.append(np.asarray(im, dtype=np.uint8))
		return self.dataSet.names[self.model.predict(ar)]
# turn the first (at most) 16 eigenvectors into grayscale
# images (note: eigenvectors are stored by column!)

"""
E = []
for i in xrange(min(model.feature.eigenvectors.shape[1], 16)):
	e = model.feature.eigenvectors[:,i].reshape(dataSet.data[0].shape)
	E.append(minmax_normalize(e,0,255, dtype=np.uint8))
# plot them and store the plot to "python_fisherfaces_fisherfaces.pdf"
subplot(title="Fisherfaces", images=E, rows=4, cols=4, sptitle="Fisherface", colormap=cm.jet, filename="fisherfaces.pdf")
# perform a 10-fold cross validation
cv = KFoldCrossValidation(model, k=10)
cv.validate(dataSet.data, dataSet.labels)
print cv
"""