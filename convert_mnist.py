# The MNIST dataset has labels (which denote the correct value of the
# handwritten digit) and pixel values separate. The images are a 28
# by 28 pixel grid of values that range from 0 (white) to 255 (black)
# with in-between values being shades of gray. 

def convert(image_file, label_file, output_file, num_images):
  labels = open(label_file, "rb")
  images = open(image_file, "rb")
  output = open(output_file, "w")

  # Discard header info
  images.read(16)
  labels.read(8)

  # Outputs label and pixel values in JSON-ish format
  output.write("{\n")
  for i in range(num_images):   # Number of images requested 
    label = ord(labels.read(1)) # Reads label value
    output.write('"' + str(i) + '": {\n  "digit": ' + str(label) + ',\n')
    output.write('  "pixels": [')
    for j in range(784): # 28 * 28 = 784 = number of pixels per image
      value = ord(images.read(1)) # Reads pixel value
      output.write(str(value) + ', ')
    output.write(']\n},\n')
  output.write('\n}')

  # Closes files when read/write operations are finished
  images.close(); output.close(); labels.close()

def main():
  convert("./train-images-idx3-ubyte",
          "./train-labels-idx1-ubyte",
          "mnistTest.json", 3)

if __name__ == "__main__":
  main()
