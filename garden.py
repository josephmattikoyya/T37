import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_sentence1 = 'The cotton clothing is made of grows in Mississippi'
nlp_gps1 = nlp(garden_path_sentence1)
#print([(token, token.orth_, token.orth) for token in nlp_gps1])
print([(i, i.label_, i.label) for i in nlp_gps1.ents])


garden_path_sentence2 = 'Mary gave the child the dog bit a Band-Aid'
nlp_gps2 = nlp(garden_path_sentence2)
#print([(token, token.orth_, token.orth) for token in nlp_gps2])
print([(i, i.label_, i.label) for i in nlp_gps2.ents])

garden_path_sentence3 = 'When Fred eats food gets thrown'
nlp_gps3 = nlp(garden_path_sentence3)
#print([(token, token.orth_, token.orth) for token in nlp_gps3])
print([(i, i.label_, i.label) for i in nlp_gps3.ents])

garden_path_sentence4 = 'That Jill is never here hurts'
nlp_gps4 = nlp(garden_path_sentence4)
#print([(token, token.orth_, token.orth) for token in nlp_gps4])
print([(i, i.label_, i.label) for i in nlp_gps4.ents])

garden_path_sentence5 = 'Helen is expecting tomorrow to be a bad day'
nlp_gps5 = nlp(garden_path_sentence5)
#print([(token, token.orth_, token.orth) for token in nlp_gps5])
print([(i, i.label_, i.label) for i in nlp_gps5.ents])

#It is unusual that Helen was assigned 'GPE' and not 'PERSON'
#It is also unusual that 'a bad day' was assigned 'DATE'