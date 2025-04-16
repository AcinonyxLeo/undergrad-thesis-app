<script lang="ts">
  import { DefaultMarker, MapLibre, Popup } from 'svelte-maplibre';
  import { loraDataStore } from '$lib/stores';
  import { onMount } from 'svelte';

  // Constant marker for the database
  const databaseMarker = {
    lngLat: [125.53666975271284, 7.039988214206031] as [number, number],
    label: 'CDB',
    name: 'CENTRALIZED DATABASE',
  };

  // Use database marker's position as center point
  const mapCenter = databaseMarker.lngLat;
  const initialZoom = 16;

  // Dynamic markers for LoRa data
  let markers: Array<{
    lngLat: [number, number];
    label: string;
    name: string;
  }> = [databaseMarker];

  // Subscribe to the store and update markers when data changes
  loraDataStore.subscribe((data) => {
    markers = [
      databaseMarker,
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
    center={mapCenter} 
    zoom={initialZoom}
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