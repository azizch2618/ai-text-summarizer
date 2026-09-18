document
    .getElementById("summarization-form")
    .addEventListener("submit", async (e) => {

        // Prevent normal form submission
        // so the browser does not reload the page.
        e.preventDefault();


        // =========================================
        // GET HTML ELEMENTS
        // =========================================

        const dialogueInput =
            document.getElementById("dialogue-input");

        const summaryText =
            document.getElementById("summary-text");

        const submitButton =
            e.target.querySelector("button");

        const buttonText =
            submitButton.querySelector(".btn-text");


        // =========================================
        // GET USER INPUT
        // =========================================

        const dialogue =
            dialogueInput.value.trim();


        // =========================================
        // VALIDATE INPUT
        // =========================================

        if (!dialogue) {

            summaryText.innerText =
                "Please enter some content to summarize.";

            dialogueInput.focus();

            return;
        }


        // =========================================
        // LOADING STATE
        // =========================================

        summaryText.innerText =
            "Generating summary...";

        submitButton.disabled = true;

        buttonText.innerText =
            "Generating Summary...";


        try {

            // =========================================
            // SEND REQUEST TO FASTAPI
            // =========================================

            const response = await fetch("/summarize/", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    dialogue: dialogue
                })
            });


            // =========================================
            // HANDLE HTTP ERRORS
            // =========================================

            if (!response.ok) {

                let errorMessage =
                    `Server error: ${response.status}`;

                try {

                    const errorData =
                        await response.json();

                    if (errorData.detail) {

                        if (typeof errorData.detail === "string") {

                            errorMessage =
                                errorData.detail;

                        } else {

                            errorMessage =
                                "Invalid request. Please check your input.";
                        }
                    }

                } catch {
                    // Keep default error message
                }

                throw new Error(errorMessage);
            }


            // =========================================
            // READ JSON RESPONSE
            // =========================================

            const data =
                await response.json();


            // =========================================
            // DISPLAY SUMMARY
            // =========================================

            summaryText.innerText =
                data.summary || "No summary returned.";


        } catch (err) {

            // =========================================
            // ERROR HANDLING
            // =========================================

            console.error(
                "Summarization error:",
                err
            );

            summaryText.innerText =
                `Error: ${err.message}`;


        } finally {

            // =========================================
            // RESTORE BUTTON
            // =========================================

            submitButton.disabled = false;

            buttonText.innerText =
                "Summarize Content";
        }

    });