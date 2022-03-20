import cv2  #import library

#read the image
img=cv2.imread("galaxy.jpg",0) # 0 is for grey scale

print(type(img))  #print the type of img
print(img)  #print the pixels/array
print(img.shape) #print the resolution
print(img.ndim) #print the dimentions

#resized_image = cv2.resize(img,(500,1000)) #first the object, second (the new dimentions)


#puting the new dimentions as the resolution of the photo divided by 2
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Galaxy",resized_image)  #call the image to be shown
cv2.imwrite("Galaxy_resized.jpg",resized_image)  #create new img file (name,object)
cv2.waitKey(0)   #define the time for closing window  eg when 0 the user can close whenever the window
cv2.destroyAllWindows()  #method to decide what to do next, closes the window




