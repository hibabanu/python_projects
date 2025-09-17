
python={"riya","safa","manu","hanna","chinnu"}
datascience={"afra","hanna","manu","jasmine","siya","nervin"}
print(f"Total number of students:{python | datascience}")
print(f"No of students who opted python only:{python - datascience}")
print(f"No of students who opted datascience only:{datascience - python}")
print(f"No of students who opted both :{datascience & python}")

course=dict([
    ("python",len(python)),
    ("datascience",len(datascience))
])
print(f"for {course.items} the number of students enrolled are {course.values}")