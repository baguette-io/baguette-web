<template>
    <section class="main" role="main">
	    <div class="presentation">
        	<div class="container headtitle">
        		<div class="row justify-content-md-center">
	    			<div class="col-12 col-md-auto">
	    				<h1>Continuous Delivery Platform</h1>
	    			</div>
	    		</div>
        		<div class="row justify-content-md-center">
	    			<div class="col-12 col-md-auto">
        				<h6>Just push your code, we cook your recipe</h6>
	    			</div>
	    		</div>
        		<div class="row justify-content-md-center mt-3">
	    			<div class="col-sm-2 btn-group btn-group-justified">
        				<a class="btn btn-fr-blue  btn-block" href="/signup" role="button">Sign up</a>
					</div>
	    			<div class="col-sm-2 btn-group btn-group-justified">
                        <a class="btn btn-fr-red btn-block" href="/login">Log in</a>
	    			</div>
	    		</div>
	    	</div>
		</div>
		<div class="windows mt-4 mb-4">
			<div class="row justify-content-md-center">
				<div class="window">
					<div class="window-header">
						<span class="window-bullet red"></span>
						<span class="window-bullet yellow"></span>
						<span class="window-bullet green"></span>
						<span class="window-title">bash</span>
					</div>
					<div class="window-body">
						<ul class="list-unstyled">
							<li><span class="prefix">[app(master)]$</span><span class="command">baguette app-create</span></li>
							<li><span class="output">app created</span></li>
							<li><span class="prefix">[app(master)]$</span><span class="command">echo "</span></li>
							<li><span class="output">language:python:3</span></li>
							<li><span class="output">commands:</span></li>
							<li><span class="output">- py.test</span></li>
							<li><span class="output">- python run.py</span><span class="command">"> Recette.yaml</span></li>
							<li><span class="prefix">[app(master)]$</span><span class="command">git push baguette.io master</span></li>
							<li><span class="output">App healthy, you can access it using : <u>https://user.app.projects.baguette.io</u></span></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="feature-1 mt-5">
				<div class="bg-fr-blue text-white">
					<div class="container">
						<div class="mt-5">
							<div class="row justify-content-md-center">
								<h3>Serverless</h3>
							</div>
							<div class="row justify-content-md-center">
								<p>Just focus on your code, you don't need to worry on the server side.</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
    </section>
</template>
