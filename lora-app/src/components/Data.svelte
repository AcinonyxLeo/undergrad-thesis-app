<script lang="ts">
    import { loraDataStore } from '../lib/stores';
    import { onMount } from 'svelte';

    let error: string | null = null;

    async function fetchLoraData() {
    try {
        const response = await fetch('http://localhost:8000/api/data/gps/');
        if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        loraDataStore.set(data); // Update the store with new data
    } catch (err) {
        error = err.message;
    }
    }

    onMount(() => {
      fetchLoraData(); // Fetch data immediately when the component mounts
      const interval = setInterval(fetchLoraData, 1000); // Fetch data every 10 seconds
      return () => clearInterval(interval); // Cleanup on component destruction
    });
</script>

<aside class="data-container">
    <div id="data" class="w-full">
    <table class="table-auto w-full border-collapse border border-gray-300">
        <thead class="bg-gray-800 text-white text-lg">
        <tr>
            <th class="border border-gray-300 px-4 py-2">Last Name</th>
            <th class="border border-gray-300 px-4 py-2">Latitude</th>
            <th class="border border-gray-300 px-4 py-2">Longitude</th>
            <th class="border border-gray-300 px-4 py-2">Speed (km/h)</th>
        </tr>
        </thead>
        <tbody class="bg-white text-gray-900 text-md">
        {#if error}
            <tr>
            <td colspan="4" class="border border-gray-300 px-4 py-2 text-red-500 text-center">
                Error: {error}
            </td>
            </tr>
        {:else}
            {#each $loraDataStore as item}
            <tr class="hover:bg-gray-100">
                <td class="border border-gray-300 px-4 py-2">{item.last_name}</td>
                <td class="border border-gray-300 px-4 py-2">{item.latitude}</td>
                <td class="border border-gray-300 px-4 py-2">{item.longitude}</td>
                <td class="border border-gray-300 px-4 py-2">{item.speed}</td>
            </tr>
            {/each}
        {/if}
        </tbody>
    </table>
    </div>
</aside>

<style>
    .data-container {
    width: 100%;
    height: 100%;
    background-color: white;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    justify-content: center;
    align-items: center;
    }
</style>