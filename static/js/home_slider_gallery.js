
let i = 0;
let images = [];
let slideTime = 10000; // 3 seconds

images[0] = '../static/image/1.jpg';
images[1] = '../static/image/main.jpg';
images[2] = '../static/image/3.jpg';
images[3] = '../static/image/main33.jpg';
function changePicture() {
  document.querySelector('.main-img').style.background = "linear-gradient(180deg, rgba(1, 83, 134, 0.37), rgba(1, 83, 134, 0.37)),url(" + images[i] + ") center/cover no-repeat #034771";

    if (i < images.length - 1) {
        i++;
    } else {
        i = 0;
    }
    setTimeout(changePicture, slideTime);
}
window.onload = changePicture;
function next(){
  document.querySelector('.main-img').style.background = "linear-gradient(180deg, rgba(1, 83, 134, 0.37), rgba(1, 83, 134, 0.37)),url(" + images[i] + ") center/cover no-repeat #034771";
  if (i < images.length - 1) {
    i++;
} else {
    i = 0;
}
}
