<template>
    <div>
	    <div class="container">
            <div class="alert alert-dismissible fade show" role="alert" v-show="show" v-bind:class="{ 'alert-success': isSuccess, 'alert-danger': isError }">
                <button type="button" class="close" @click="$emit('hide')" >
                    <span aria-hidden="true">&times;</span>
                </button>
                {{ prefix }}<strong>{{ obj }}</strong>{{ suffix }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: ['isSuccess', 'isError', 'obj', 'prefix', 'show', 'suffix']
}
</script>
