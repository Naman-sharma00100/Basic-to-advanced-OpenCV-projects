import cv2
 
image = cv2.imread('testQRCode-1.jpg')
 
qrCodeDetector = cv2.QRCodeDetector()


decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
points = points[0].astype(int)
print(points)
if points is not None:

    nrOfPoints = len(points)
    for i in range(nrOfPoints):
        nextPointIndex = (i+1) % nrOfPoints
        cv2.line(image, tuple(points[i]), tuple(points[nextPointIndex]), (255,0,0), 5)
 
    print(decodedText)    
    cv2.imwrite("result.png",image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
 
else:
    print("QR code not detected")