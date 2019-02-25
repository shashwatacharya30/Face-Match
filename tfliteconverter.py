import tensorflow as tf

graph_def_file = "facenet_model.pb"
input_arrays = ["input"]
output_arrays = ["embeddings"]

converter = tf.contrib.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays,input_shapes={'input':[1,160,160,3]})

tflite_model = converter.convert()
open("frozen.tflite", "wb").write(tflite_model)
