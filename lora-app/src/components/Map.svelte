<script lang="ts">
  import { DefaultMarker, MapLibre, Popup } from 'svelte-maplibre';
  import Data from './Data.svelte';
  import HeaderMap from './Header_Map.svelte';
    import SectionWrapper from './SectionWrapper.svelte';
  
 const markers: Array<{
    lngLat: [number, number];
    label: string;
    name: string;
    }> = [
      {
      lngLat: [125.612333, 7.072362],
      label: 'CDB',
      name: 'CENTRALIZE DATABASE',
    },
  ];
</script>

<div id="map">
  <MapLibre 
    center={[125.612333, 7.072362]}
    zoom={16}
    class="map"
    standardControls
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json">

    <!--Code for Marker-->
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