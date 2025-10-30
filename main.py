import os
import datetime
from PIL import ImageGrab, ImageFont, ImageDraw, Image
import time
import csv
import pyautogui

class imageSave:
    def __init__(self, imageList : list, path : str = './my_captures', log : str = 'image_log.csv'):
        self.fontSize = 12
        self.imgTextList = []
        self.name = "CAM"
        self.path = path
        self.log = log
        # self.checkDir('./my_captures')
        for i in range(len(imageList)):
            imgText = self.imageAddText(imageList[i])
            self.imgTextList.append(imgText)
        self.image2Dir()
        self.imageNote()
        
    def imageAddText(self, img):
        w, h = img.size
        font = ImageFont.truetype('arial.ttf', self.fontSize)
        draw = ImageDraw.Draw(img)

        current_time = datetime.datetime.now()
        display_time = current_time.strftime("%Y-%m-%d_%H:%M:%S.%f")[:-3]
        filename_time = current_time.strftime("%Y-%m-%d_%H-%M-%S.%f")[:-3]

        text_bbox = draw.textbbox((0, 0), display_time, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        margin = 10
        x = w - text_width - margin
        y = h - text_height - margin
        draw.rectangle([x, y, x + text_width, y + text_height], fill='white')
        draw.text((x, y),  display_time, fill=(0, 0, 0), font=font)
        # img.save('./ok.jpg')     
        # img.show()  
        # self.img2Dir('./my_captures', now)
        ans = {
            "time": filename_time,
            "image": img}
        
        return ans
    
    def image2Dir(self):
        path = self.path + '/' + self.name

        for i in range(len(self.imgTextList)):
            camPath = path + str(i)
            if not os.path.exists(camPath):
                os.makedirs(camPath)
            self.imgTextList[i]['image'].save(camPath + '/' + self.imgTextList[i]['time'] + '.jpg')

    def imageNote(self):
        csv_path = os.path.join(self.path, self.log)
        
        file_exists = os.path.isfile(csv_path)

        with open(csv_path, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            if not file_exists:
                csv_writer.writerow(['timestamp', 'camera_id', 'file_path'])

            for i, item in enumerate(self.imgTextList):
                # print(self.imgTextList[i]['image'])
                # print(self.imgTextList[i]['time'])
                # pass
                camera_id = self.name + str(i)
                file_path = item['time'] + '.jpg'
                csv_writer.writerow([item['time'], camera_id, file_path])

def cutimg(img):
    w,h = img.size
    if w % 2 == 0:
        cut1 = int(w/2)
    else:
        cut1 = int((w-1)/2)
    if h % 2 == 0:
        cut2 = int(h/2)
    else:
        cut2 = int((h-1)/2)
    img_top_left = img.crop((0, 0, cut1, cut2))
    img_top_right = img.crop((cut1, 0, w, cut2))
    img_bottom_left = img.crop((0, cut2, cut1, h))
    img_bottom_right = img.crop((cut1, cut2, w, h))
    
    return [img_top_left, img_top_right, img_bottom_left, img_bottom_right]
    
   



if __name__ == "__main__":
    testList = []
    myScreenshot = pyautogui.screenshot()
    testList = cutimg(myScreenshot)
    imageSave(testList, './my_captures')
  