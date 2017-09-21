<template>
    <div class="row">
        <ol class="breadcrumb">
            <template v-for="(item, index) in items">
                <template v-if="index === items.length - 1">
                    <li class="breadcrumb-item active">{{ item.name }}</li>
                </template>
                <template v-else>
                    <li class="breadcrumb-item">
                        <nuxt-link :to="item.url">{{ item.name }}</nuxt-link>
                    </li>
                </template>
            </template>
        </ol>
    </div>
</template>

<script>
export default {
  props: ['items']
}
</script>
