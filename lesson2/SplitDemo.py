x = 'blue,red,green'
a, b, c = x.split(",")
print(a, b, c)

score = "國文=100;數學=80;英文=90"
for item in score.split(";"):
    print(item.split("=")[0], item.split("=")[1])

score_dict = dict(item.split("=") for item in score.split(";"))
print(score_dict)
print(score_dict.get('國文'))



