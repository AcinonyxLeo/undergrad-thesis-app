<script>
    import SectionWrapper from "./SectionWrapper.svelte";
</script>

<SectionWrapper>
    <div id="about" class="title-background flex flex-col items-center">
        <h2 class="about-title">ABOUT US</h2>
        <div class="content flex items-start">
            <img src="../LoRaLogo.png" alt="LoRa Logo" class="logo-image">
            <div class="text-content">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
        </div>
    </div>
</SectionWrapper>

<style>
    :global(body) {
        background-color: #084c61;
        color: white;
        font-family: Georgia, serif;
        margin: 0;
        padding: 0;
    }

    .title-background {
        width: 100%;
        height: 100vh; /* Adjust the height as needed */
        color: white; /* Ensure text is readable */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start; /* Align content to the top */
        text-align: center;
        padding: 2em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
        padding-top: 80px; /* Add padding to account for the header height */
    }

    .about-title {
        font-size: 2.5em; /* Increase the font size of the title */
        margin-bottom: 1em; /* Add space below the title */
        font-weight: bold;
        text-transform: uppercase; /* Make the text all caps */
        padding: 0.5em 1em; /* Add padding around the title */
        border: 2px solid white; /* Add a border around the title */
        border-radius: 8px; /* Add rounded corners */
        background-color: rgba(255, 255, 255, 0.5); /* Fill the border with white but transparent */
        color: black; /* Change the font color to black */
    }

    .content {
        display: flex;
        align-items: flex-start;
        text-align: left; /* Align text to the left */
        max-width: 1200px; /* Limit the width of the content */
        width: 100%;
        padding: 1em;
        margin-top: 2em; /* Add space between the title and the content */
    }

    .logo-image {
        width: 6in; /* Set the width to 6 inches */
        height: auto; /* Maintain aspect ratio */
        margin-right: 1in; /* Add some space between the image and the text */
    }

    .text-content {
        flex: 1; /* Allow the text content to take up remaining space */
    }

    p {
        font-family: Georgia, serif;
        font-size: 1.25em; /* Increase the font size of the paragraph */
        line-height: 1.6; /* Increase line height for better readability */
    }
</style>