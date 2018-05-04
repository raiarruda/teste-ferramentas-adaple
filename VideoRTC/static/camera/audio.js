function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {

        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));

    }
});



// capture camera and/or microphone


navigator.mediaDevices.getUserMedia({ audio: true }).then(function (mic) {

    var recorder;

    document.getElementById('iniciar').onclick = (function (){
        this.disabled = true;

        document.getElementById('your-audio-id').muted = true;
        setSrcObject(mic, document.getElementById('your-audio-id'));
        recorder = RecordRTC(mic, { type: 'audio'});
        recorder.startRecording();

        document.getElementById('terminar').disabled =false;
    });

   
    //iniciar a funcao de graavar video apos apertar botao terminar
    document.getElementById('terminar').onclick = (function () {

        recorder.stopRecording(function () {

            // get recorded blob
            var blob = recorder.getBlob();
            // generating a random file name
            var fileName = getFileName('mp3');
            // we need to upload "File" --- not "Blob"
            var fileObject = new File([blob], fileName, {
                type: 'audio/mp3'
            });
            var formData = new FormData();
            // recorded data
            formData.append('audio_file', fileObject);
            // file name
            formData.append('audio-filename', fileObject.name);
            // document.getElementById('h').innerHTML = 'Uploading to PHP using jQuery.... file size: (' + bytesToSize(fileObject.size) + ')';
            // upload using jQuery
            $.ajax({
                url: '', // replace with your own server URL
                data: formData,
                cache: false,
                contentType: false,
                processData: false,
                type: 'POST',
                success: function (response) {

                    alert(response); // error/failure
                }
            });
            // release camera
            document.getElementById('your-audio-id').srcObject = document.getElementById('your-audio-id').src = null;
            camera.getTracks().forEach(function (track) {
                track.stop();
            });
        });
        // }, milliSeconds);
    }); //fecha a função de gravar o video
});


























// this function is used to generate random file name
function getFileName(fileExtension) {
    var d = new Date();
    var year = d.getUTCFullYear();
    var month = d.getUTCMonth();
    var date = d.getUTCDate();
    return 'RecordRTC-' + year + month + date + '-' + getRandomString() + '.' + fileExtension;
}
function getRandomString() {
    if (window.crypto && window.crypto.getRandomValues && navigator.userAgent.indexOf('Safari') === -1) {
        var a = window.crypto.getRandomValues(new Uint32Array(3)),
            token = '';
        for (var i = 0, l = a.length; i < l; i++) {
            token += a[i].toString(36);
        }
        return token;
    } else {
        return (Math.random() * new Date().getTime()).toString(36).replace(/\./g, '');
    }
}
