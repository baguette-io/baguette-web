<template>
    <nav class="navbar navbar-expand-lg navbar-light">
	    <div class="container">
            <nuxt-link class="navbar-brand" to="/">
                baguette.io
            </nuxt-link>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mr-auto"></ul>
                <ul class="navbar-nav navbar-right">
                    <li class="">
                        <a class="btn btn-danger" href="/logout" role="button">Log out</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
