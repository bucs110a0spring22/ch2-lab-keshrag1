import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = (cost_per_week / classes_per_week)
print("cost_per_class:", cost_per_class, "dollars per class")
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))
#Part B
random_list=1,2.0,3.5,6.3,9,11.27,12,13.336,"15"
print(random.choice(random_list))
