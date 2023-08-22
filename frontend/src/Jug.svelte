<script>
    export let value;
    export let max_value;
    $: height = 100 - (value / max_value) * 100;
</script>

<article class="outter_container">
    <div class="jug_container">
        <img src="/jug.png" alt="Jug" />
        <div style="top:{height}%" class="inner_container" />
        <div id="current_content">{value}</div>
    </div>
    <div id="capacity">{max_value} gallons</div>
</article>

<style>
    .jug_container img {
        position: absolute;
        z-index: 10;
    }

    .jug_container {
        height: 200px;
        width: 238px;
        border: 0;
        background-color: white;
        margin: 5px;
        overflow: hidden;
        position: relative;
    }

    .inner_container {
        height: 100%;
        width: 70%;
        border: 0px;
        background-color: lightblue;
        position: absolute;
        transition: top 1s ease-out;
        z-index: 5;
        text-align: center;
    }
    .jug_container #current_content {
        position: absolute;
        top: 50%;
        left: 35%;
        font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
            "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
        font-weight: bold;
        font-size: 25px;
        transform: translate(0, -50%);
        z-index: 6;
    }

    .outter_container #capacity {
        text-align: center;
    }
</style>
