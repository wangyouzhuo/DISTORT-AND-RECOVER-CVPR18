from PIL import Image, ImageEnhance
"""
ImageEnhance库 介绍
https://blog.csdn.net/icamera0/article/details/50753705
"""
import numpy as np

"""
	Actions: image constrast, color vividness(?), color temperature, brightness, edge enhancer(?)
#PIL image temperature change : http://stackoverflow.com/questions/11884544/setting-color-temperature-for-a-given-image-like-in-photoshop
http://www.vendian.org/mncharity/dir3/blackbody/

调整 对比 明暗 色温 对比

"""
import time

kelvin_table = [
       (255,243,239) , # 6000K
       (227,233,255) , # 8000K
       (204,219,255) , # 10000K
	   (191,211,255) , # 12000K
	   (182,224,255)   # 14000K
	]

def take_action(image_np, action_idx):
	#image_pil = Image.fromarray(np.uint8(image_np))
	image_pil = Image.fromarray(np.uint8((image_np+0.5)*255))

	# enhance contrast 对比度
	if action_idx == 0:
		enh = ImageEnhance.Contrast(image_pil)
		image_enh = enh.enhance(0.7) # 减对比
	elif action_idx == 1:
		enh = ImageEnhance.Contrast(image_pil)
		image_enh = enh.enhance(1.3)  # 加对比

	# enhance color 饱和度
	elif action_idx == 2:
		enh = ImageEnhance.Color(image_pil)
		image_enh = enh.enhance(0.7)  # 降饱和
	elif action_idx == 3:
		enh = ImageEnhance.Color(image_pil)
		image_enh = enh.enhance(1.3)   # 加饱和

	# color brightness  亮度
	elif action_idx == 4:
		enh = ImageEnhance.Brightness(image_pil)
		image_enh = enh.enhance(0.7)   # 变暗
	elif action_idx == 5:
		enh = ImageEnhance.Brightness(image_pil)
		image_enh = enh.enhance(1.3)   # 变亮

	# color temperature : http://stackoverflow.com/questions/11884544/setting-color-temperature-for-a-given-image-like-in-photoshop

	elif action_idx == 6:  # 色温6000K
		r,g,b = kelvin_table[0]
 		matrix = ( 	r / 255.0, 0.0, 0.0, 0.0,
               		0.0, g / 255.0, 0.0, 0.0,
               		0.0, 0.0, b / 255.0, 0.0 )
		image_enh = image_pil.convert('RGB', matrix)  # 6000K
	elif action_idx == 7:  # 色温8000k
		r,g,b = kelvin_table[1]
 		matrix = ( 	r / 255.0, 0.0, 0.0, 0.0,
               		0.0, g / 255.0, 0.0, 0.0,
               		0.0, 0.0, b / 255.0, 0.0 )
		image_enh = image_pil.convert('RGB', matrix)  # 8000K
	elif action_idx == 8:
		r,g,b = kelvin_table[2]
 		matrix = ( 	r / 255.0, 0.0, 0.0, 0.0,
               		0.0, g / 255.0, 0.0, 0.0,
               		0.0, 0.0, b / 255.0, 0.0 )
		image_enh = image_pil.convert('RGB', matrix)  # 10000K
	elif action_idx == 9:
		r,g,b = kelvin_table[3]
 		matrix = ( 	r / 255.0, 0.0, 0.0, 0.0,
               		0.0, g / 255.0, 0.0, 0.0,
               		0.0, 0.0, b / 255.0, 0.0 )
		image_enh = image_pil.convert('RGB', matrix)  # 12000K
	elif action_idx == 10:
		r,g,b = kelvin_table[4]
 		matrix = ( 	r / 255.0, 0.0, 0.0, 0.0,
               		0.0, g / 255.0, 0.0, 0.0,
               		0.0, 0.0, b / 255.0, 0.0 )
		image_enh = image_pil.convert('RGB', matrix)  # 14000K
	else:
		print("error")
	

	return (np.asarray(image_enh)/255.0-0.5)


