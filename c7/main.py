import base64

with open("unknown", "rb") as image_file:
    encoded_string = eval(str(base64.b64encode(image_file.read())).replace('/',''))
image_result = open('deer_decode.gif', 'wb') # create a writable image and write the decoding result 
image_result.write(encoded_string)
image_result.close()
