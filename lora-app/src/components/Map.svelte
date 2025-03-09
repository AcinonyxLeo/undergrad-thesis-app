<script lang="ts">
  import { DefaultMarker, MapLibre, Popup } from 'svelte-maplibre';
  import { loraDataStore } from '$lib/stores'; // Adjust the import path as needed
  import { onMount } from 'svelte';

  // Constant marker for the database
  const databaseMarker = {
    lngLat: [125.612333, 7.072362] as [number, number],
    label: 'CDB',
    name: 'CENTRALIZE DATABASE',
  };

  // Dynamic markers for LoRa data
  let markers: Array<{
    lngLat: [number, number];
    label: string;
    name: string;
  }> = [databaseMarker]; // Initialize with the database marker

  // Subscribe to the store and update markers when data changes
  loraDataStore.subscribe((data) => {
    markers = [
      databaseMarker, // Always include the database marker
      ...data.map((item) => ({
        lngLat: [item.longitude, item.latitude] as [number, number],
        label: item.last_name,
        name: item.last_name,
      })),
    ];
  });
</script>

<div id="map">
  <MapLibre
    center={[125.612333, 7.072362]}
    zoom={16}
    class="map"
    standardControls
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json">

    <!-- Dynamically render markers -->
    {#each markers as { lngLat, name }}
      <DefaultMarker {lngLat}>
        <Popup offset={[0, -10]}>
          <div class="text-lg font-bold">{name}</div>
        </Popup>
      </DefaultMarker>
    {/each}
  </MapLibre>
</div>

<style>
  :global(.map) {
    height: 800px;
  }
</style>