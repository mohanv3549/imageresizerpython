import cv2

src=cv2.imread("imgres.jpg",cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)
#cv2.waitKey(0)
scale_per=50
wd=int(src.shape[1]*scale_per/100)
ht=int(src.shape[0]*scale_per/100)
desize=(wd,ht)
output=cv2.resize(src,desize)
cv2.imwrite('newim.png',output)
cv2.waitKey(0)
