<template>
    <nav class="navbar navbar-expand-lg navbar-light">
	    <div class="container">
            <nuxt-link class="navbar-brand" to="/">
                baguette.io
            </nuxt-link>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <a class="btn btn-danger" href="#" role="button">Get started</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Pricing</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Documentation</a>
                    </li>
                </ul>
                <ul class="navbar-nav navbar-right">
                    <li class="">
                        <a class="nav-link" href="/login">Log in</a>
                    </li>
                    <li class="">
                        <a class="btn btn-danger" href="/signup" role="button">Sign up</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
