in_sent = input("Please input a sentence containing the word \"python\": ")

new_out = ""
ind = in_sent.find("python")
counter = 1

while ind is not -1:
    if ind is not -1:
        in_sent = in_sent[:ind] + "pythons " + in_sent[ind + 7:]
    old_ind = ind
    counter += 1
    ind = in_sent.find("python ")

print(in_sent)
