document.addEventListener("DOMContentLoaded", function () {


    // Display selected resume filename

    const resumeInput = document.getElementById("resume");
    const fileName = document.getElementById("file-name");


    if (resumeInput) {


        resumeInput.addEventListener(
            "change",
            function () {


                if (this.files.length > 0) {

                    fileName.innerHTML =
                    "Selected: " + this.files[0].name;

                }

                else {

                    fileName.innerHTML =
                    "No file selected";

                }


            }
        );

    }



    // Form loading effect

    const form = document.querySelector("form");


    if (form) {


        form.addEventListener(
            "submit",
            function () {


                const button =
                document.querySelector(".btn");


                if(button){

                    button.innerHTML =
                    "Analyzing Resume... ⏳";


                    button.disabled = true;

                }


            }
        );


    }



});