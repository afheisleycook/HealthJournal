function isValid() {
    let title = document.querySelector("title");
    let description = document.querySelector("description");
    if(title.value == "") {
        alert("Please enter a title");
    }
    if(description.value == "") {
        alert("Please enter a description");

    }
    else {
        alert("post not empty");
    }
    
}