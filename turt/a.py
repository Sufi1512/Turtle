from vpython import *
my_sphere=sphere(pos=vector(0,0,0,),radius=0.25,color=vector(1,2,4),shininess=1)
wall1 = box(pos=vector(2,0,0),size=vector(0.1,1,1), color=vector(3,4,4))
wall2 = box(pos=vector(-2,0,0),size=vector(0.1,1,1), color=vector(3,4,4))
edge1=wall1.pos.x-wall1.size.x/2
edge2=wall2.pos.x-wall2.size.x/2
i=1
dx=0.1
while(i<=1000):
    rate(10)
    if(my_sphere.pos.x+my_sphere.radius>=edge1)or(my_sphere.pos.x-my_sphere.radius<=edge2):
        dx=-dx
    my_sphere.pos.x=my_sphere.pos.x+dx
    i=i+1