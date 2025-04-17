<script>

</script>

<header class="flex flex-col relative z-20 header-style">
    <div class="max-w-[1400px] mx-auto w-full flex items-center justify-between p-6 py-8">
        <a href="/" class="logo">
            <h1>LoRaTrack</h1>
        </a>
        <nav class="flex items-center gap-8">
            <a href="#about" class="nav-link">About Us</a>
            <a href="/map" class="nav-link">Track Now</a>
        </nav>
    </div> 
</header>

<style>
    :global(body, html) {
        margin: 0;
        padding: 0;
    }

    .header-style {
        position: fixed; /* Make the header fixed */
        top: 0;
        left: 0;
        z-index: 1000; /* Ensure it stays above other elements */
        background-color: #ffc857; /* Keep the original color */
        color: #ffffff; /* White text for contrast */
        font-family: 'Arial', sans-serif; /* Clean, modern font */
        font-weight: bold;
        font-size: 1.5em; /* Keep font size the same */
        width: 100%; /* Ensure it fills the entire width */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        padding: 0.6em 0; /* Reduce vertical padding for a smaller header box */
    }

    .logo h1 {
        margin: 0;
        font-size: 2.5em; /* Increase the font size of the main title */
        color: #084c61; /* Highlighted logo color */
        text-shadow: 3px 3px 6px rgb(255, 255, 255); /* Stronger shadow for emphasis */
    }

    nav {
        margin-left: auto; /* Move the navigation links to the side */
    }

    .nav-link {
        color: #ffffff;
        text-decoration: none;
        padding: 0.8em 2em; /* Add more padding to links */
        border-radius: 8px; /* Add rounded corners to links */
        font-size: 1.2em; /* Increase font size for readability */
        transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transition for hover effect */
    }

    .nav-link:hover {
        color: #084c61; /* Highlight text on hover */
        background-color: rgba(255, 255, 255, 0.1); /* Add subtle background on hover */
    }

    .nav-link:active {
        background-color: rgba(255, 255, 255, 0.2); /* Slightly darker background on click */
    }
</style>