<script>
    import Data from "../../components/Data.svelte";
    import Map from "../../components/Map.svelte";
    import SectionWrapperMap from "../../components/SectionWrapper_Map.svelte";
</script>

<SectionWrapperMap>
    <div class="layout">
        <section></section>
        <section id="gps">
            <Map />
        </section>
        <section class="table-container">
            <Data />
        </section>
        <section></section>
    </div>
</SectionWrapperMap>

<style>
    .layout {
        display: grid;
        grid-template-columns: 5% 50% 40% 5%;
        width: 98%;
        gap: 0em 2em 0em;
        margin: 2em;
    }

    .table-container {
        height: 100%; /* Match the height of the map */
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
