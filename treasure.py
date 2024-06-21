
import numpy as np
from os import listdir, system
from os.path import exists
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity

def extract_image_vector(image_path):
    # Load pre-trained ResNet50 model
    model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Get the image features (vector representation)
    features = model.predict(img_array)
    return features.flatten()  # Flatten to make it a 1D vector

def main():
    highest_score = -1
    highest_number = None
    print(f"[INFO] Finding your treasure...")
    image1_vector = extract_image_vector("user.png")
    equality_list = []
    for folder in listdir("data"):
        path = f"data\\{folder}\\"
        if not exists(f"{path}vector.txt"):
            print(f"Processing {folder}...")
            image2_vector = extract_image_vector(f"{path}treasure.png")
            np.savetxt(f"{path}vector.txt", image2_vector, delimiter=",")

        image2_vector = np.loadtxt(f"{path}vector.txt", delimiter=',')

        similarity_score = cosine_similarity(image1_vector.reshape(1, -1), image2_vector.reshape(1, -1))

        equality_list.append({"score": similarity_score[0][0]*100, "number": folder})

    for item in equality_list:
        score = item["score"]
        number = item["number"]

        if score > highest_score:
            highest_score = score
            highest_number = number


    if highest_number is not None:
        print(f"[INFO] Equality: {highest_score}")
        return f"data\\{highest_number}\\map.png"
    else:
        print(f"[INFO] An error occurred.")

if __name__ == '__main__':
    path_to_result = main()
    system(f"start {path_to_result}")
