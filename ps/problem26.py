n = 0 
def get_high_score(n):
    return max(n) 

scores = [50, 80, 95, 70]
final_score=get_high_score(scores)


# at break point 

with open("files/Hi-score.txt" , "w") as f :
    f.write(str(final_score)) 

 
