
function open_menu(){
    document.querySelector('.menus').style.display ='block';
}
function close(){
    document.querySelector('.menus').style.display ='none';
 
}
function eventoner(a){
a.addEventListener("mouseover", mouseOver);
a.addEventListener("mouseout", mouseOut);
}
function mouseOver(){
    let i=0;
    let eded= 0;
    if(i < 20) {
        i+5;
        eded=i;
        document.getElementById("linkarrow").style.opacity =`${eded}`; 
        document.getElementById("linkarrow").style.transform ="translate3d("+ eded +"px, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)";
        document.getElementById("linkarrow").style.transformStyle="preserve-3d";
    }
   
}

function mouseOut(){
    document.getElementById("linkarrow").style.opacity =" 0"; 
    document.getElementById("linkarrow").style.transform ="translate3d(-20px, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)";
    document.getElementById("linkarrow").style.transformStyle="preserve-3d";
}