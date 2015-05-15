

Girls = ["A", "B", "C"];
Girls_Answer = ["a", "a", "a"];

Boys = ["A", "B", "C"];
Boys_Answer = ["a", "b", "b"];

Result = "B";

def makeMatch(Girls,Girls_Answer,Boys,Boys_Answer,Result):
	names = len(Girls);
	answers = len(Girls_Answer[0]);	
	
	Girls_Combine = sorted(zip(Girls,Girls_Answer));
	Boys_Combine = sorted(zip(Boys,Boys_Answer));
	
	taken = [0]*names;
	match_sum_array = [0]*names;
	big_match_array = [0]*names;
	#iterate over each name 
	for x in xrange(names):
		#fetch the answers from first girl
		answer_g = Girls_Combine[x][1];
		found = "false";
		for x2 in xrange(names):
			#iterate first girl over each boy
			answer_b = Boys_Combine[x2][1];
			count = 0;
			match_array = [0]*answers
			for x3 in answer_b:
				#iterate girls answer over boys answer
				if(x3==answer_g[count]):
					match_array[count] = 1;
				count+=1;
			big_match_array[x2] = sum(match_array);
		found=1;	
		while(found):
			match_sum_array[x] = big_match_array.index(max(big_match_array));
			print x,match_sum_array;
			if(x==0):
				taken = match_sum_array[x];
				found=0;			
			else:
				for i in xrange(x):
					if(match_sum_array[x]==match_sum_array[i]):
						big_match_array[big_match_array.index(max(big_match_array))] = -1;
						match_sum_array[x] = big_match_array.index(max(big_match_array));
					else:
						found=0;			
	for x in xrange(names):
		if(Girls_Combine[x][0]==Result):
			girl = x;	
	return Boys_Combine[match_sum_array[girl]][0];

print makeMatch(Girls,Girls_Answer,Boys,Boys_Answer,Result);
