const upload_image_form = document.getElementById("upload_image_form");
const upload_image = document.getElementById("upload_image");

function submitForm() {
  alert("form submitted")
    upload_image_form.submit();

}
function importData() {
    // let input = document.createElement('input');
    // input.type = 'file';
    // input.onchange = _ => {
    //           let files =   Array.from(input.files);
    //       };
    upload_image.onchange = submitForm;
    upload_image.click();
    
  }

  // export default importData;
  upload_image.addEventListener('change', submitForm);
