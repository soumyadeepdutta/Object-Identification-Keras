from django.shortcuts import render
from .form import ImageUploadingForm

# Model Dependencies
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# binary image
def handle_upload(file):
    with open('img.jpg','wb+') as save_image:
        for chuck in file.chunks():
            save_image.write(chuck)

# render image upload page
def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'image-process/input.html')

def imageProcess(request):
    form = ImageUploadingForm(request.POST, request.FILES)
    if form.is_valid():
        handle_upload(request.FILES['image'])

        # if image valid, create model
        model = ResNet50(weights='imagenet')

        img_path = 'img.jpg'

        # predicting image
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        # print('Predicted:', decode_predictions(preds, top=3)[0])

        res = []
        for result in decode_predictions(preds, top=3)[0]:
            res.append((result[1], np.round(result[2]*100, 2)))
        
        # print(res)

    return render(request, 'image-process/output.html', {'res':res})
