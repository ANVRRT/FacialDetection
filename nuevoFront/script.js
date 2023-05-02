const video = document.createElement('video');
const canvas = document.getElementById('canvas');
const photo = document.getElementById('photo');
const captureButton = document.getElementById('capture');
const cameraView = document.getElementById('camera');
const constraints = {
	video: true,
	audio: false
};

navigator.mediaDevices.getUserMedia(constraints)
.then((stream) => {
	video.srcObject = stream;
	video.play();
	cameraView.appendChild(video);
})
.catch((error) => {
	console.error(`Error al acceder a la cámara: ${error}`);
});

captureButton.addEventListener('click', () => {
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
	canvas.getContext('2d').drawImage(video, 0, 0);
	photo.src = canvas.toDataURL('image/png');
	photo.style.display = 'block';
	video.style.display = 'none';
	captureButton.style.display = 'none';


    
    // Solicitar al usuario el nombre del archivo
    const fileName = prompt("Ingrese un nombre para la foto:");

    // Crear un enlace temporal para descargar el archivo
    const link = document.createElement("a");
    link.download = fileName || "photo.png";
    link.href = canvas.toDataURL("image/png");
    link.target = "_blank";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    // Mostrar una ventana emergente indicando que la foto se guardó correctamente
    alert("La foto se ha guardado con éxito en la carpeta 'fotos'"); 
});