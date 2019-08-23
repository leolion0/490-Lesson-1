in_sent = input("Please input a sentence containing the word \"Python\": ")
# in_sent = "hello python man"
new_out = ""
ind = in_sent.find("python")
while ind is not -1:
    ind = in_sent.find("python ")
    subs = in_sent[ind: ind + 6]
    if ind is not -1:
        temp = in_sent[:ind + 6] + "s" + in_sent[ind + 6:]
        new_out = new_out + temp
    old_ind = ind
    ind = new_out[old_ind + 7:].find("python")

print(new_out)
