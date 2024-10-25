import colorgram

color=colorgram.extract('colors.jpeg',30)

rgb_color=[]

for color in color:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    c_tuple=(r,g,b)

    rgb_color.append(c_tuple)


print(rgb_color)

