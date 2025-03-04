<script>
    export let id;
    import Header from "./Header.svelte";
</script>

<section {id} class={"min-h-screen flex flex-col px-4 "}>
    <Header />
    <div class="flex flex-col flex-1 max-w-[1400px] mx-auto">
        <slot />
    </div>
</section>