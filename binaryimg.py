#Script Created by Epic

import sys, argparse, cv2
import numpy as np

def change_brightness(img, value=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the source image")
    parser.add_argument("f", help="the dest text")
    parser.add_argument("b", help="Brightness of the image")

    if(len(sys.argv) < 4):
        parser.print_help()
    else:
        try:
            args = parser.parse_args()
            img = cv2.imread(args.src, 2)
            _, bw_img = cv2.threshold(img, 0,1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            image = cv2.imread(args.src)
            image = change_brightness(image, value=int(args.b))
            #cv2.imshow('f', image)
            #cv2.waitKey(0)
            with open(args.f, 'w') as f:
                f.write('[\n')
                for r in range(0, len(bw_img) - 1):
                    f.write('\t')
                    f.write(str(bw_img[r].tolist()))
                    f.write(',\n')
                f.write('\t')
                f.write(str(bw_img[-1].tolist()))
                f.write('\n]')
        except Exception as e:
            print('Exception happpend')
            print(e)
            
       
main()
