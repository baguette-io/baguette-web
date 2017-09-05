<template>
    <div>
	    <div class="container">
            <div class="alert" role="alert" v-bind:class="{ 'alert-success': isSuccess, 'alert-danger': isError }">
                {{ prefix }}
                <a href="#" class="alert-link">{{ obj }}</a>
                {{ suffix }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: ['isSuccess', 'isError', 'obj', 'prefix', 'suffix']
}
</script>
