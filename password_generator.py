counter = 0
characters = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
f = open('wordlist.txt','w')
for i in characters:
    for j in characters:
        for k in characters:
            for l in characters:
                guess = str(i) + str(j) + str(k) + str(l)
                f.write(guess)
                f.write('\n')
                counter += 1
print('Wordlist of {} passwords generated.'.format(counter))