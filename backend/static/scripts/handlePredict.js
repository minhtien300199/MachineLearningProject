window.addEventListener('DOMContentLoaded',(event)=>{
    document.querySelector('#exampleFormControlFile1').addEventListener('onChange',(event)=>{
        console.log(event.target.value);

    })
});

const renderImage = (e) =>{
    console.log("load Image!");
    var imgTag = document.getElementById("user-img");
    imgTag.src = URL.createObjectURL(e.target.files[0]);
    imgTag.width="200px";
    imgTag.height="200px";
};

