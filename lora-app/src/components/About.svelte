<script>
    import SectionWrapper from "./SectionWrapper.svelte";
</script>

<SectionWrapper>
    <div id="about" class="title-background flex flex-col items-center" style="margin-top: 10em;">
        <h2 class="about-title">ABOUT US</h2>
        <div class="content flex items-start">
            <img src="../LoRaLogo.png" alt="LoRa Logo" class="logo-image">
            <div class="text-content">
                <p>
                    Welcome to <strong>LoRaTrack</strong>, your trusted solution for vehicle tracking. 
                    Our platform leverages cutting-edge LoRa technology to provide seamless, 
                    reliable, and precise tracking services. Whether you're managing a fleet or 
                    ensuring the safety of your personal vehicle, LoRaTrack is here to help.
                </p>
                <p>
                    With a localized database and user-friendly interface, we ensure that you 
                    have complete control and visibility over your vehicles at all times. 
                    Experience the future of vehicle tracking with LoRaTrack.
                </p>
            </div>
        </div>
    </div>
</SectionWrapper>

<style>
    :global(body) {
        background-color: #084c61;
        color: white;
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        scroll-behavior: smooth; /* Ensure smooth scrolling */
    }

    .title-background {
        width: 100%;
        min-height: calc(100vh - 4em); /* Subtract header height */
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        padding: 5em 2em; /* Increase top padding for better spacing */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .about-title {
        font-size: 3em; /* Increase font size for emphasis */
        margin-bottom: 1em; /* Add more space below the title */
        margin-top: 2em;
        font-weight: bold;
        text-transform: uppercase;
        padding: 0.5em 2em;
        border: 3px solid white;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.6);
        color: #084c61; /* Darker text for contrast */
    }

    .content {
        display: flex;
        align-items: flex-start;
        text-align: left;
        max-width: 1200px;
        width: 100%;
        gap: 3em; /* Add more spacing between image and text */
        margin-top: 1em;
    }

    .logo-image {
        width: 45%; /* Adjust image size for better balance */
        height: auto;
        border-radius: 10px; /* Add rounded corners */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Add stronger shadow */
    }

    .text-content {
        flex: 1;
        font-size: 1.4em; /* Increase font size for readability */
        line-height: 2; /* Improve line spacing */
        color: #d1e8e2; /* Softer text color for readability */
        text-align: justify; /* Ensure text is justified */
    }

    p {
        margin-bottom: 2em; /* Add more spacing between paragraphs */
    }

    p strong {
        color: #ffc857; /* Highlight important text */
    }

    @media (max-width: 900px) {
        .content {
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .logo-image {
            width: 80%; /* Adjust image size for smaller screens */
            margin-bottom: 2em;
        }

        .text-content {
            text-align: center;
        }

        .about-title {
            font-size: 3em; /* Adjust title size for smaller screens */
        }
    }
</style>