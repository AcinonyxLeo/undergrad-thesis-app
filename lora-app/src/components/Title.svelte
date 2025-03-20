<script>
  import SectionWrapper from "./SectionWrapper.svelte";
  import { goto } from '$app/navigation';

  function handleClick() {
    goto('/map'); // Navigate to the /map route
  }
</script>

<SectionWrapper>
  <div class="title-container">
    <!-- Left Side - Text -->
    <div class="text-content">
      <h2>LoRa-Based Infrastructure with Localized Database</h2>
      <p class="subtitle">Track your vehicle anytime, anywhere!</p>
      <button class="cta-button" on:click={handleClick}>Track Now</button>
    </div>

    <!-- Right Side - Image -->
    <div class="image-container">
      <img src="/LoraTitle.png" alt="LoRa Logo" class="logo-image">
    </div>
  </div>
</SectionWrapper>

<style>
  /* Remove default margin/padding */
  :global(html, body) {
      margin: 0;
      padding: 0;
      width: 100vw;
      height: 100vh;
      overflow-x: hidden;
  }

  /* FLEX CONTAINER FOR TEXT + IMAGE */
  .title-container {
      display: flex;
      width: 100vw;
      height: 100vh;
  }

  /* LEFT SIDE - TEXT */
  .text-content {
      flex: 1;
      padding: 2em;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      color: white;
      width: 50vw; /* Ensures it only takes half the screen */
  }

  h2 {
      font-size: 2.5em;
      margin: 0;
  }

  .subtitle {
      font-size: 1.25em;
      margin-top: 0.5em;
  }

  .cta-button {
      background-color: #ffc857;
      color: #323031;
      padding: 0.8em 1.5em;
      font-size: 1em;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      margin-top: 1em;
      font-weight: bold;
      transition: background-color 0.3s ease;
  }

  .cta-button:hover {
      background-color: #f4a261;
  }

  /* RIGHT SIDE - IMAGE */
  .image-container {
      width: 50vw; /* Ensures it only takes half of the screen */
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
  }

  /* Fix image scaling issues */
  .logo-image {
      width: 100%;
      height: auto;
      object-fit: contain; /* Ensures it fits nicely */
      object-position: center; /* Centers the image */
  }

  /* RESPONSIVE DESIGN */
  @media (max-width: 900px) {
      .title-container {
          flex-direction: column;
          text-align: center;
          height: auto;
      }
      .text-content {
          text-align: center;
          width: 100%;
          align-items: center;
      }
      .image-container {
          width: 100%;
          height: auto;
      }
      .logo-image {
          width: 100%;
          height: auto;
      }
  }
</style>