###################################
# Mutation vs. assignment


################
# Look alike, but different

a = [4, 5, 6]
b = [4, 5, 6]
print "Original a and b:", a, b

a[1] = 20
print "New a and b:", a, b

################
# Aliased

c = [2, 9, 0]
d = c
print "Original c and d:", c, d

c[2] = 10
print "New c and d:", c, d

################
# Copied

e = ["a", "b", "c"]
f = list(e)
print "Original e and f:", e, f

e[0] = "z"
print "New e and f:", e, f


###################################
# Interaction with globals


a = [4, 5, 6]

def modify_part(x):
    """Change part of global a to be x."""
    a[0] = x

def modify_whole(x):
    """Change global a to be x."""
    a = x

modify_part(100)
print a

modify_whole(100)
print a


###################################
# Lists (mutable) vs. tuples (immutable)


print [4, 5, 6]

print (4, 5, 6)

print type([4, 5, 6])

print type((4, 5, 6))

a = [4, 5, 6]
a[1] = 100
print a

b = (4, 5, 6)
b[1] = 100
print b
