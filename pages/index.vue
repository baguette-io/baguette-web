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
        				<h6>push your code, we deploy it</h6>
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
						<span class="window-title"></span>
					</div>
					<div class="window-body">
						<ul class="list-unstyled">
							<li><span class="prefix">~/app(master) $</span><span class="command">git push baguette.io master</span></li>
							<li><span class="output">Deploying...</span></li>
							<li><span class="output">App healthy, you can access it using : <u>https://user.app.projects.baguette.io</u></span></li>
							<li><span class="prefix">~/app(master) $</span></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="feature-1 mt-5">
			<div class="bg-fr-blue text-white">
				<div class="container">
					<div class="pt-5">
						<div class="row">
							<h4>Serverless</h4>
						</div>
						<div class="row">
							<p>you don't have to worry anymore about servers</p>
						</div>
						<div class="row">
							<span>Focus on your <b>product</b></span>
						</div>
						<div class="row">
							<span>Use <b>any</b> programming language and framework</span>
						</div>
						<div class="row">
							<span>Use <b>any</b> protocol</span>
						</div>
						<div class="row">
							<span>Service discovery, autoscaling, namespaces are <b>>out of the box</b></span>
						</div>
						<div class="row">
							<span><b>No downtime</b> during upgrade></span>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="feature-2 mt-5">
			<div class="bg-fr-white text-dark">
				<div class="container">
					<div class="pt-5">
						<div class="row">
							<h4>Configuration as a code</h4>
						</div>
						<div class="row">
							<p>Define your workflow using <b>yaml</b>:</p>
						</div>
						<div class="row">
							<span>This is <b>limitless</b> as you can run any command</span>
						</div>
						<div class="row">
							<span><b>Isolate</b> your services per environment or pull request</span>
						</div>
						<div class="row">
							<span><b>Choose</b> to export or not your service to the public</span>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="feature-3 mt-5">
			<div class="bg-fr-red text-white">
				<div class="container">
					<div class="pt-5">
						<div class="row">
							<h4>Much more</h4>
						</div>
						<div class="row">
							<p>baguette.io is fully <b>open source (LGPL 3)</b>:</p>
						</div>
						<div class="row">
							<span>Use our <b>REST API</b></span>
						</div>
						<div class="row">
							<span><b>Host it</b> yourself</span>
						</div>
						<div class="row">
							<span><b>Participate</b></span>
						</div>
					</div>
				</div>
			</div>
		</div>
    </section>
</template>
