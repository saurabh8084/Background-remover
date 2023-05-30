const submit_btn = document.getElementById("submit_btn");
const upload_img = document.getElementById("upload_img");
const upload_url = document.getElementById("upload_url").value;

function setCookie(name, value, exdays = 7, path = "/") {
  var exdate = new Date();
  exdate.setDate(exdate.getDate() + exdays);
  var c_value = value + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString() + `; path=${path}`);
  document.cookie = name + "=" + c_value;
}


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function onClickHandler(ev) {
  // var el = window._protected_reference = document.createElement("input");
  var el = window._protected_reference = upload_img;
  el.type = "file";
  el.accept = "image/*";
  el.multiple = "multiple";
    
    // (cancel will not trigger 'change')
  el.addEventListener('change', function(ev2) {
      // access el.files[] to do something with it (test its length!)
      
      // add first image, if available
    if (el.files.length) {
      document.getElementById('out').src = URL.createObjectURL(el.files[0]);
      submit_btn.classList.remove("d-none");
      submit_btn.classList.add("d-inline-block");
      upload(el.files[0]);
    }
  
  
      // test some async handling
    new Promise(function(resolve) {
      setTimeout(function() { console.log(el.files); resolve(); }, 1000);
    })
    .then(function() {
        // clear / free reference
      el = window._protected_reference = undefined;
    });
  
  });
  
  el.click(); // open
}

// This will upload the file after having read it
const upload = (file) => {
  const csrfToken = getCookie('csrftoken');
  var data = new FormData()
  data.append("img", file)
  const headers = new Headers({
    // 'Content-Type': 'multipart/form-data;',
    'X-CSRFToken': csrfToken
}); 
  fetch(upload_url, { // Your POST endpoint
    method: 'POST',
    headers: headers,
    body: data // This is your file object
  }).then(
    response =>{
      // console.log(response)
      // console.log(response.blob())
      response.blob().then(blob => download(blob, "sample.png"));
      
    }  // if the response is a JSON object
  ).catch(
    error => console.log(error) // Handle the error response object
  );

  // then(
  //   response => response.json() // if the response is a JSON object
  // ).then(
  //   success => console.log(success) // Handle the success response object
  // ).catch(
  //   error => console.log(error) // Handle the error response object
  // );
};

function download(blob, filename) {
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  // a.style.display = 'none';
  a.innerHTML = "Download Now"
  a.href = url;
  // the filename you want
  a.download = filename;
  document.body.appendChild(a);
  // a.click();
  // document.body.removeChild(a);
  // window.URL.revokeObjectURL(url);
}