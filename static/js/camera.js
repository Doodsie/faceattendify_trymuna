// static/camera.js
document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('videoElement');

    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                video.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing camera:', error);
            });
    } else {
        console.error('getUserMedia is not supported');
    }
});