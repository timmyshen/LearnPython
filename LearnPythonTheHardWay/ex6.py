x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# one
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Note %r is formatter
# two
print "I said: %r." % x
# This is %s and single quote here
# three
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

# four
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e