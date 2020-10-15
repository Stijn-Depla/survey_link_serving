<!-- wp:buttons {"align":"center"} -->
<div class="wp-block-buttons aligncenter"><!-- wp:button -->
<div class="wp-block-button"><a id="Button" class="wp-block-button__link">Start Survey</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:html -->
<script>
let url = "https://hex99zk7wj.execute-api.eu-central-1.amazonaws.com/dev/";

fetch(url, {
        method:'GET'
})
.then(function(response){
console.log(response);
return response.text();
})
.then(function(result){
document.querySelector("#Button").href = result;
});

</script>
<!-- /wp:html -->