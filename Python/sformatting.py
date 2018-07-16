# String formatting
# 1st method '.format()' method
print('this is a string{}'.format(' to be inserted'))
# we can also insert strings in index
print('the {} {} {} {}'.format('brown','fox','quick','jumps over bridge'))
# now we can arrange this using indexing
print('the {2} {0} {1} {3}'.format('brown','fox','quick','jumps over bridge'))
# we can also do this by assigning the keywords and then call using keywords
print('the {q} {b} {f} {j}'.format(b='brown',f='fox',q='quick',j='jumps over bridge')) 