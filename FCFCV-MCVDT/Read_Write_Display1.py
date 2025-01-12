import cv2
img = cv2.imread('laziestant.jpg') #imread နဲ့ image တစ်ခုကို ယူ
cv2.imshow("cv2.started",img) #imshow နဲ့ image ကို ထုတ်ပြ
cv2.waitKey(0) #key တစ်ခုမရိုက်မချင်း ပြနေစေချင်လို့
cv2.imwrite("laziestant.png", img) #imwrite နဲ့ File type ပြောင်း