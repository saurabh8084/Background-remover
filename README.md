# Django Background Remover

This Django project allows you to remove the background from images using the `rembg` library and PIL (Python Imaging Library).

## Installation

Clone the repository:
Create a virtual environment:

Activate the virtual environment:
- For Windows:
  ```
  env\Scripts\activate
  ```

* Install the dependencies:

## Usage

1. Start the Django development server:

2. Open your web browser and go to `http://localhost:8000/`.

3. Upload an image file using the provided form.

4. Click the "Submit" button to remove the background from the uploaded image.

5. The processed image will be displayed, and you can also find it saved in the `path/to/save/processed/` directory.

## Configuration

- If you want to change the location where uploaded and processed images are saved, modify the `image_path` and `output_path` variables in the `remover/utils.py` file.

- You can customize the Django project settings in the `background_remover/settings.py` file.

## Credits

- This project uses the `rembg` library (https://github.com/danielgatis/rembg) for background removal.
- The Django framework (https://www.djangoproject.com/) is used for the web application.



