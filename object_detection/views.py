# from django.shortcuts import render
# from .yolov8_model import get_model

# def detect_objects(request):
#     if request.method == 'POST':
#         image = request.FILES['image']
#         model = get_model()
#         results = model.predict(image)
#         # Process results and render the template with detected objects
#     return render(request, 'object_detection/detect.html')

from django.shortcuts import render
from PIL import Image
from .yolov8_model import get_model
from .forms import ImageForm

def detect_objects(request):
    if request.method == 'POST':

        model = get_model()

        results = model.predict("cats_dogs_1.jpg")
        result = results[0]
        print(result.boxes)
        raise SystemExit

        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     image = form.cleaned_data['image']

        #     model = get_model()

        #     results = model.predicts("cats_dogs_1.jpg")
        #     print(results)
        #     raise SystemExit
            
        #     # Load a pretrained YOLO model (recommended for training)
        #     # model = YOLO('yolov8n.pt')

        #     # Train the model using the 'coco128.yaml' dataset for 3 epochs
        #     results = model.train(data='coco128.yaml', epochs=3)

        #     # Evaluate the model's performance on the validation set
        #     results = model.val()

        #     # Perform object detection on an image using the model
        #     results = model(image)

        #     # Export the model to ONNX format
        #     success = model.export(format='onnx')

        #     # results = model.predict(image)
        #     # Process results and render the template with detected objects
    else:
        form = ImageForm()

    return render(request, 'object_detection/detect.html', {'form': form})