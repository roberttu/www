/*!
  * Bootstrap v4.0.0-beta (https://getbootstrap.com)
  * Copyright 2011-2017 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
  */
 

var fileindex=0;
function fileSelected() {
  var file = document.getElementById('fileToUpload').files[fileindex];
  if (file) {
    var fileSize = 0;
    if (file.size > 1024 * 1024)
      fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
    else
      fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';
          
    document.getElementById('fileName').innerHTML = 'Name: ' + file.name;
    document.getElementById('fileSize').innerHTML = 'Size: ' + fileSize;
    document.getElementById('fileType').innerHTML = 'Type: ' + file.type;
  }
}
function uploadFile() {
  filesarr=document.getElementById('fileToUpload').files

/*  for (var i = 0; i < filesarr.length; i++) {
    fd.append("fileToUpload", document.getElementById('fileToUpload').files[i]);
  }*/
  for (var i = 0; i < filesarr.length; i++) {
  var fd = new FormData();
  fileindex=i;
  fd.append("fileToUpload", document.getElementById('fileToUpload').files[fileindex]);
  var xhr = new XMLHttpRequest();

  /* event listners */
  xhr.upload.addEventListener("progress", uploadProgress, false);
  xhr.addEventListener("load", uploadComplete, false);
  xhr.addEventListener("error", uploadFailed, false);
  xhr.addEventListener("abort", uploadCanceled, false);
  /* Be sure to change the url below to the url of your upload server side script */
  xhr.open("POST", "../cgi-bin/Upload2.py"); 
  xhr.send(fd);
  fileSelected();
  }
}

function uploadProgress(evt) {
  if (evt.lengthComputable) {
    var percentComplete = Math.round(evt.loaded * 100 / evt.total);
    document.getElementById('progressNumber').innerHTML = percentComplete.toString() + '%';
  }
  else {
    document.getElementById('progressNumber').innerHTML = 'unable to compute';
  }
}

function uploadComplete(evt) {
  /* This event is raised when the server send back a response */
/*  alert(evt.target.responseText); */
}

function uploadFailed(evt) {
  alert("There was an error attempting to upload the file.");
}

function uploadCanceled(evt) {
  alert("The upload has been canceled by the user or the browser dropped the connection.");
}  

function signin() {
  var fd = new FormData();
  fd.append("inputEmail", document.getElementById('inputEmail').value);
  fd.append("inputPassword", document.getElementById('inputPassword').value);
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function() {
    if (xhr.readyState===4) {
/*         alert("on ready"+xhr.response);*/
         document.getElementById('errormessage').innerHTML=xhr.response;
    }
  }
  xhr.open("POST", "../cgi-bin/signin.py"); 
  xhr.send(fd);
}
   
