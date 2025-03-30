# Realtime Deep Learning - Action Recognition System CV

**Why Deep Learning?**
| **Feature** | **Traditional Methods** | **Deep Learning Methods** |
|---|---|---|
| Feature Extraction | Handcrafted features (e.g., optical flow, HOG) | Deep neural networks (e.g., CNNs, RNNs) |
| Classification | SVM, KNN | Deep neural networks |
| Data Requirements | Relatively low | High |
| Computational Cost | Lower | Higher |
| Performance | Good, but limited by feature engineering | State-of-the-art |
| Robustness | Less robust to variations | More robust |

## What is Action Recognition?
To classification the target(one people or a group of people).
E.g. Determine whether a person in the video is "taking a product" or "resetting a product".

## Main methods
Three common main methods:

1. Frame-based Methods (Dựa trên khung hình):
- Description: Use CNN or Vision Transformer (ViT) to classify actions from each frame independently.
- For example: Use CNN ResNet-50 will recognize actions such as "throwing", "hitting", "running" from each frame. Then the classification results of each frame can then be aggregated to give a classification result for the entire video.
- Disadvantages: Does not take advantage of time information.

2. Temporal-based Methods (Dựa trên chuỗi thời gian):
- Description: Use 3D CNN models (like I3D, C3D) or combine with RNN/LSTM to exploit information between consecutive frames.
- For example: I3D (Inflated 3D ConvNet) extends 2D CNN to 3D to learn temporal information.
- Disadvantages: Demand significant computational resources and processing time.

3. Skeleton-based Methods (Dựa trên xương):
- Description: Use a Pose Estimation based model like OpenPose or MediaPipe to recognize skeletal gestures.
- For example: Analyzing gait to detect health problems by using OpenPose to extract skeletal data from walkers then analyzing features from skeletal data (e.g., joint angles, joint velocities) to detect gait abnormalities, using machine learning or deep learning models to analyze gait characteristics.
- Disadvantages: Requires the system to estimate pose accurately.

## Models used
- Two-Stream Convolutional Networks:
    - Combine information from RGB images and optical flow to recognize actions.
- I3D (Inflated 3D ConvNet)
    - Extend 2D CNN to 3D to learn spatiotemporal features from videos.
- SlowFast Networks
    - Run two networks in parallel: one slow (captures spatial detail) and one fast (captures motion detail).


# Next Development:

- Real-Time Human Action Recognition Using Pose Estimation on Multiple Persons [Link]()
- Sign Language Detection Using Action Recognition [Link]()

# Reference: 
[Human action recognition -- SlowFast Networks](https://www.youtube.com/watch?v=J3xIp0x_6jA)