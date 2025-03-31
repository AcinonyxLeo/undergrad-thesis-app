<script>
    import { loraDataStore } from '$lib/stores'; // Import the store
    let loraData = []; // Array to store the table data
    let error = null; // Variable to store errors

    // Function to fetch data from the backend
    async function fetchLoraData() {
        try {
            const response = await fetch('http://localhost:8000/api/data/gps/');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();

            // Update the table data
            data.forEach(newItem => {
                const existingIndex = loraData.findIndex(item => item.plate_number === newItem.plate_number);
                if (existingIndex !== -1) {
                    // If the item exists, update it
                    loraData[existingIndex] = newItem;
                } else {
                    // If the item doesn't exist, add it
                    loraData = [...loraData, newItem];
                }
            });

            // Update the store with the new data
            loraDataStore.set(loraData);

            // Trigger a reactive update
            loraData = loraData;
        } catch (err) {
            error = err.message;
        }
    }

    // Fetch data immediately and every 5 seconds
    fetchLoraData();
    setInterval(fetchLoraData, 5000); // Polling every 5 seconds
</script>


<aside class="data-container ">
    <div id="data" class="flex flex-col w-full" >
        <table class="table-auto w-full border-collapse border border-gray-300">
            <thead class="bg-gray-800 text-white text-lg">
                <tr>
                    <th class="border border-gray-300 px-4 py-2">Timestamp</th>
                    <th class="border border-gray-300 px-4 py-2">Last Name</th>
                    <th class="border border-gray-300 px-4 py-2">Longitude</th>
                    <th class="border border-gray-300 px-4 py-2">Latitude</th>
                    <th class="border border-gray-300 px-4 py-2">Speed (km/h)</th>
                </tr>
            </thead>
            <tbody class="bg-white text-gray-900 text-md">
                {#if error}
                    <tr>
                        <td colspan="5" class="border border-gray-300 px-4 py-2 text-red-500 text-center">
                            Error: {error}
                        </td>
                    </tr>
                {:else if loraData.length === 0}
                    <tr>
                        <td colspan="5" class="border border-gray-300 px-4 py-2 text-center">
                            No data available.
                        </td>
                    </tr>
                {:else}
                    {#each loraData as item}
                        <tr class="hover:bg-gray-100">
                            <td class="border border-gray-300 px-4 py-2">{item.timestamp}</td>
                            <td class="border border-gray-300 px-4 py-2">{item.last_name}</td>
                            <td class="border border-gray-300 px-4 py-2">{item.longitude}</td>
                            <td class="border border-gray-300 px-4 py-2">{item.latitude}</td>
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