''' Write a function, select_subject_by_id(id,dict_list), which accepts an id number and a list of dictionary items about subjects in an experiment and returns the item with the specified id. If there are no subjects with that id or there are more than one subjects, then it should return the value False<div><br></div><div>So if dict_list is the following:</div><div>[ {'id':1442, 'age':21, 'score':93},<br></div><div> {'id':1102, 'age':19, 'score':89},<br></div><div> {'id':1998, 'age':20, 'score':97},<br></div><div> {'id':1995, 'age':21, 'score':83}</div><div>]<br></div><div><br></div><div>The call select_subects(1102,dict_list) will return</div><div>{'id':1102, 'age':19, 'score':89}<br></div><div><br></div><div>The select_subects(1103,dict_list) will return<br></div><div>False</div><div><br></div><div>Hint: use a list comprehension.</div><div><br></div><div></div>
''' 
import doctest
import math
def select_subject_by_id(id,ds):
	'''
	Here are some unit tests:
	>>> select_subject_by_id(2184, [{'id': 8440, 'age': 22, 'score': 90}, {'id': 7712, 'age': 30, 'score': 90}, {'id': 2184, 'age': 27, 'score': 83}])
	{'id': 2184, 'age': 27, 'score': 83}
	>>> select_subject_by_id(4800, [{'id': 2016, 'age': 21, 'score': 84}, {'id': 1320, 'age': 18, 'score': 80}, {'id': 3496, 'age': 30, 'score': 99}, {'id': 4800, 'age': 21, 'score': 88}, {'id': 1192, 'age': 23, 'score': 80}, {'id': 6480, 'age': 18, 'score': 90}, {'id': 1184, 'age': 29, 'score': 85}])
	{'id': 4800, 'age': 21, 'score': 88}
	>>> select_subject_by_id(5672, [{'id': 2408, 'age': 19, 'score': 100}, {'id': 3440, 'age': 23, 'score': 90}, {'id': 8728, 'age': 23, 'score': 89}, {'id': 2320, 'age': 27, 'score': 99}, {'id': 5672, 'age': 21, 'score': 80}, {'id': 4168, 'age': 25, 'score': 98}, {'id': 5400, 'age': 25, 'score': 90}])
	{'id': 5672, 'age': 21, 'score': 80}
	>>> select_subject_by_id(6328, [{'id': 9536, 'age': 29, 'score': 100}, {'id': 6720, 'age': 21, 'score': 95}, {'id': 6328, 'age': 28, 'score': 86}, {'id': 8000, 'age': 21, 'score': 95}, {'id': 7632, 'age': 25, 'score': 85}, {'id': 1272, 'age': 27, 'score': 84}, {'id': 6856, 'age': 21, 'score': 96}])
	{'id': 6328, 'age': 28, 'score': 86}
	>>> select_subject_by_id(3560, [{'id': 5936, 'age': 23, 'score': 86}, {'id': 3560, 'age': 25, 'score': 82}, {'id': 4376, 'age': 29, 'score': 92}])
	{'id': 3560, 'age': 25, 'score': 82}
	>>> select_subject_by_id(3688, [{'id': 3688, 'age': 24, 'score': 86}, {'id': 4040, 'age': 27, 'score': 82}, {'id': 5712, 'age': 30, 'score': 99}, {'id': 1464, 'age': 25, 'score': 86}, {'id': 5408, 'age': 30, 'score': 92}, {'id': 3680, 'age': 29, 'score': 86}, {'id': 4888, 'age': 20, 'score': 90}])
	{'id': 3688, 'age': 24, 'score': 86}
	>>> select_subject_by_id(2240, [{'id': 4176, 'age': 18, 'score': 85}, {'id': 2240, 'age': 21, 'score': 93}, {'id': 4344, 'age': 18, 'score': 87}])
	{'id': 2240, 'age': 21, 'score': 93}
	>>> select_subject_by_id(6328, [{'id': 6328, 'age': 18, 'score': 99}, {'id': 2816, 'age': 21, 'score': 93}, {'id': 7880, 'age': 24, 'score': 100}, {'id': 1408, 'age': 21, 'score': 89}, {'id': 4848, 'age': 27, 'score': 81}, {'id': 9504, 'age': 25, 'score': 85}])
	{'id': 6328, 'age': 18, 'score': 99}
	>>> select_subject_by_id(4096, [{'id': 5328, 'age': 19, 'score': 84}, {'id': 9464, 'age': 30, 'score': 89}, {'id': 9224, 'age': 21, 'score': 90}, {'id': 7936, 'age': 30, 'score': 82}, {'id': 4096, 'age': 26, 'score': 81}])
	{'id': 4096, 'age': 26, 'score': 81}
	>>> select_subject_by_id(5208, [{'id': 5208, 'age': 26, 'score': 96}, {'id': 6848, 'age': 24, 'score': 100}, {'id': 5496, 'age': 26, 'score': 92}, {'id': 7288, 'age': 26, 'score': 97}, {'id': 6032, 'age': 18, 'score': 90}])
	{'id': 5208, 'age': 26, 'score': 96}
	'''
	# your code goes here ...
if (__name__=="__main__"):
	doctest.testmod()  # this runs the unit tests listed in the docstring.
	print('all tests have been run')