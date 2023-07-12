# Face-Detection-App


The Face Detection App is a Python-based application that utilizes OpenCV and Streamlit to detect and highlight faces in images or video streams. It provides a simple and interactive interface for users to  start video streaming and obtain real-time face detection results.

## Features

- Face detection: Automatically detects and highlights faces in  video streams.
- Real-time processing: Performs face detection in real-time for video streams.
- User-friendly interface: Uses Streamlit to create an intuitive and interactive user interface.
- Easy setup and usage: Written in Python, OpenCV, and Streamlit, making it easy to install and run on compatible systems.


## Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/face-detection-app.git
```

2. Navigate to the project directory:

```shell
cd face-detection-app
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Start the application:

```shell
streamlit run main.py
```

2. The application will open in your default web browser.

3. If you select the "Video Stream" option:
   - Click the "lets go" button to begin video streaming using your device's camera.
   - The application will continuously analyze the video stream and highlight detected faces in real-time.

## Customization

You can customize the behavior of the app by modifying the following parameters in the `main.py` file:

- `DETECTION_CONFIDENCE`: Adjust the face detection confidence threshold (between 0.0 and 1.0) to control the sensitivity of face detection.
- `BOX_COLOR`: Define the color of the bounding boxes around the detected faces. Use RGB values (e.g., `(255, 0, 0)` for red).
- `BOX_THICKNESS`: Set the thickness of the bounding box lines (in pixels).

Feel free to experiment and adapt the app to suit your needs.

## Contributing

Contributions are welcome! If you have any ideas, enhancements, or bug fixes, please submit a pull request. Any contributions you make are greatly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Face Detection App was developed using the following technologies and libraries:
  - [Python](https://www.python.org/)
  - [OpenCV](https://opencv.org/)
  - [Streamlit](https://streamlit.io/)


## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out to the project maintainer:

Somanshu Dubey
- Email: Dubey.somanshu18@gmail.com
