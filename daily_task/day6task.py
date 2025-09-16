sum=0
total=0
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
for x in blog_views :
    if (x>1000):
        print(f"{x}: Trending")
        sum=sum+1

    elif (x>500 and x<1000):
        print (f"{x}: Average")
    else:
        print(f"{x}: Low traffic")
    total=total+x
print(f"no of posts were trending:{sum}")
print(f" total number of views:{total}")
