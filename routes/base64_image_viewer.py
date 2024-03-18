from flask import Blueprint, render_template, request
import base64

route = Blueprint('base64_image_viewer', __name__)

@route.route('/tools/base64_image_viewer', methods=['GET', 'POST'])
def base64_image_viewer():
    if request.method == 'POST':
        # Retrieve the base64 image data from the form

        base64_image = request.form['base64_image']
        
        # Create the image source for rendering
        image_src = f"data:image/png;base64,{base64_image}"

        return render_template("/base64_image_viewer.html", image_src=image_src)

    return render_template("base64_image_form.html")