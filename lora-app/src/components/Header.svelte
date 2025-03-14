<script>

</script>

<header class="flex flex-col relative z-20 header-style">
    <div class="max-w-[1400px] mx-auto w-full flex items-center justify-between p-4 py-6">
        <a href="/">
            <h1>Track your Car!</h1>
        </a>
        <nav class="flex items-center gap-4 lg:gap-6">
            <a href="#about" class="duration-200 hover:text-indigo-400 cursor-pointer">About Us</a>
            <a href="/map" class="duration-200 hover:text-indigo-400 cursor-pointer">Track Now</a>
        </nav>
    </div> 
</header>

<style>
    :global(body, html) {
        margin: 0;
        padding: 0;
    }

    .header-style {
        background-color: #ffc857;
        color: #323031;
        font-family: Georgia, serif;
        font-weight: bold;
        font-size: 1.5em;
        width: 100%;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
    }

    .header-style a {
        color: #323031;
        text-decoration: none;
        padding: 0.5em 1em; /* Add padding to links */
        border-radius: 4px; /* Add rounded corners to links */
        transition: background-color 0.3s ease; /* Smooth transition for hover effect */
    }

    .header-style a:hover {
        color: #084c61;
        background-color: rgba(255, 255, 255, 0.2); /* Add background color on hover */
    }

    .header-style h1 {
        margin: 0;
        font-size: 2em; /* Increase the font size of the main title */
    }

    nav {
        margin-left: auto; /* Move the navigation links to the side */
    }
</style>