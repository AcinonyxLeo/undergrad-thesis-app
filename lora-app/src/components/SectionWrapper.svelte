<script>
    import HeaderMap from "./Header.svelte";
    export let id;
</script>

<section {id} class="min-h-screen flex flex-col">
    <HeaderMap />
    <div class="flex flex-col flex-1 w-full mx-auto" style="margin-top: 10em;">
        <slot />
    </div>
</section>