# pylint: disable = unused-argument
'''
Analyzers for multiple time periods
'''
from qcrit.model_analyzer import model_analyzer

@model_analyzer()
def train_earlymodern_test_modern(data, target, file_names, feature_names, labels_key):
	'''
	Inspecting how a model trained on the early modern corpus will
	perform on the modern corpus
	'''
	print('Test')
