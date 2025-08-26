import imageio.v3 as iio 
filenames = ['img1.png','img2.png']
images=[]
for filename in filenames:
    images.append(iio.imread(filename)) #imread() method allows to load an image based on the filepath
iio.imwrite('team.gif',images, duration = 500, loop=0)
#teamgif is the name of the new file, images is the list containing image data, duration = 500 is the time in miliseconds and loop=0 means it keeps looping forever

