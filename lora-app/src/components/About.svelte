<script>
    import SectionWrapper from "./SectionWrapper.svelte";
</script>

<SectionWrapper>
    <div id="about" class="title-background flex flex-col items-center">
        <div class="content flex items-start">
            <img src="../LoRaLogo.png" alt="LoRa Logo" class="logo-image">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
    </div>
</SectionWrapper>

<style>
    .title-background {
        width: 100%;
        height: 100vh; /* Adjust the height as needed */
        color: white; /* Ensure text is readable */
    }

    .content {
        display: flex;
        align-items: flex-start;
        padding-top: 1cm; /* Position the content 1 inch from the top */
    }

    .logo-image {
        width: 4in; /* Set the width to 2 inches */
        height: 4in; /* Set the height to 2 inches */
        margin-right: 1in; /* Add some space between the image and the text */
    }

    p {
        font-family: Georgia;
    }
</style>