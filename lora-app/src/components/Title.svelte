<script>
  import { goto } from '$app/navigation';

  function handleClick() {
      goto('/map'); // Navigate to the /map route
  }
</script>

<div class="title-container">
    <!-- Left Side - Text -->
    <div class="text-content">
        <h1 class="main-title">LoRaTrack</h1>
        <p class="subtitle">
            Revolutionizing vehicle tracking with cutting-edge technology.
        </p>
        <button class="cta-button" on:click={handleClick}>
            Track Your Vehicle Now
        </button>
    </div>

    <!-- Right Side - Image -->
    <div class="image-container">
        <img src="/LoraTitle.png" alt="LoRa Logo" class="logo-image">
    </div>
</div>

<style>
  :global(html, body) {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow-y: auto;
      box-sizing: border-box;
      font-family: 'Arial', sans-serif; /* Use a clean, professional font */
  }

  :global(*),
  :global(*::before),
  :global(*::after) {
      box-sizing: inherit;
  }

  .title-container {
      display: flex;
      justify-content: flex-start; /* Align content to the left */
      align-items: center;
      width: 100%;
      height: calc(100vh - 4em); /* Subtract header height */
      background: linear-gradient(135deg, #084c61, #1e81b0); /* Professional gradient */
      color: white;
      padding: 0; /* Remove horizontal padding */
  }

  .text-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      padding-left: 2em; /* Add left padding for proper placement */
  }

  .main-title {
      font-size: 5em; /* Larger, bold title */
      margin: 0;
      margin-left: 2em;
      font-weight: bold;
      color: #ffc857; /* Highlighted title color */
      text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.5); /* Stronger shadow for emphasis */
  }

  .subtitle {
      font-size: 2em; /* Increase font size for better readability */
      margin-top: 0.5em;
      margin-left: 5em;
      line-height: 1.8; /* Improve readability */
      color: #ffffff; /* Softer text color for contrast */
      font-style: italic; /* Add a professional touch */
  }

  .cta-button {
      background-color: #ffc857;
      color: #323031;
      padding: 1.2em 3em; /* Larger button for emphasis */
      font-size: 1.5em; /* Increase button text size */
      margin-left: 6em;
      border: none;
      border-radius: 50px; /* Rounded button for a modern look */
      cursor: pointer;
      margin-top: 2em;
      font-weight: bold;
      transition: transform 0.2s ease, background-color 0.3s ease;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Add a stronger shadow */
  }

  .cta-button:hover {
      background-color: #f4a261;
      transform: translateY(-4px); /* Slight lift on hover */
  }

  .image-container {
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      height: 100%; /* Ensure the container fills the height */
  }

  .logo-image {
      width: 100%; /* Ensure the image fills the container width */
      height: 100%; /* Ensure the image fills the container height */
      object-fit: cover; /* Cover the entire container */
      object-position: center;
  }

  @media (max-width: 900px) {
      .title-container {
          flex-direction: column;
          text-align: center;
          height: auto;
      }
      .text-content {
          align-items: center;
          padding-left: 0; /* Remove left padding for smaller screens */
      }
      .main-title {
          font-size: 6em; /* Adjust font size for smaller screens */
      }
      .subtitle {
          font-size: 1.8em; /* Adjust font size for smaller screens */
      }
      .cta-button {
          font-size: 1.3em; /* Adjust button text size for smaller screens */
      }
      .image-container {
          width: 100%;
          margin-top: 2em;
      }
      .logo-image {
          width: 100%;
          height: auto;
      }
  }
</style>