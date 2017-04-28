import random
import string
import time


def id_generator(size=4, chars=string.ascii_letters):
   return ''.join(random.choice(chars) for _ in range(size))

start_time = time.time()
print("---input_list begin %s seconds ---" % (time.time() - start_time))
# input_list = random.sample(range(1000000000, 9999999999),
#                            1000000000)
print("---input_list end %s seconds ---" % (time.time() - start_time))
i = 0.1
start_time = time.time()
temp_list = []
# Open a input file to store these numbers
with open('input_file_large.txt', 'a') as f_input:
    # Write numbers to input_file
    #for temp_list in input_list.pop(10000):
    for i in range(1000):
        for line in range(10**6):
            temp_list.append(str(random.getrandbits(32)) + ',' + id_generator() + '\n')
            # temp_word = id_generator()
            # f_input.write(temp_word + '\t' + temp_word * random.randrange(1, 9) + '\n')
            if line % 999999 == 0 and line != 0:
                print("--- %f%% end in %s seconds ---" % (i, time.time() - start_time))
                i += 0.1
                start_time = time.time()

        start_time = time.time()
        print("--- %s begin in %s seconds ---" % ('write file begin', time.time() - start_time))
        f_input.writelines(temp_list)
        print("--- %s begin in %s seconds ---" % ('write file end', time.time() - start_time))