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
							<li>
								<span class="output">
								<span>App healthy, you can access it using :</span>
								<span class="bt-link">https://user.app.master.projects.baguette.io</span>
								</span>
							</li>
							<li><span class="prefix">~/app(master) $</span></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="feature-1 mt-5">
			<div class="bg-fr-blue text-white">
				<div class="container">
					<div class="row pt-5">
						<div class="col-md-6">
							<div class="row">
								<h4>
									Serverless
									<small class="pl-3 font-weight-light font-italic" style="font-size:14px;">Focus on your product</small>
								</h4>
							</div>
							<div class="mt-4 mb-4 row">
								<ul class="list-group list-group-flush">
									<li class="list-group-item no-border bg-fr-blue"><i class="fa fa-flag fa-fw" aria-hidden="true"></i> Use any programming language and framework</li>
									<li class="list-group-item no-border bg-fr-blue"><i class="fa fa-road fa-fw" aria-hidden="true"></i> Use any protocol</li>
									<li class="list-group-item no-border bg-fr-blue"><i class="fa fa-clock-o fa-fw" aria-hidden="true"></i> No downtime during deployments</li>
									<li class="list-group-item no-border bg-fr-blue"><i class="fa fa-wrench fa-fw" aria-hidden="true"></i> REST api, auto discovery, auto scaling, health checks, ...</li>
								</ul>
							</div>
						</div>
						<div class="col-md-6">
							<div class="mt-5 row">
								<span class="ml-3">
									<img src="/images/python.png" width="75" height="75" class="" alt="python" />
								</span>
								<span class="ml-3">
									<img src="/images/js.png" width="75" height="75" class="" alt="js" />
								</span>
								<span class="ml-3">
									<img src="/images/netcore.png" width="75" height="75" class="" alt=".netcore" />
								</span>
								<span class="ml-3">
									<img src="/images/go.png" width="75" height="75" class="" alt="go" />
								</span>
							</div>
							<div class="row pt-3">
								<span class="ml-3">
									<img src="/images/java.png" width="75" height="75" class="" alt="java" />
								</span>
								<span class="ml-3">
									<img src="/images/ruby.png" width="75" height="75" class="" alt="ruby" />
								</span>
								<span class="ml-3">
									<img src="/images/rust.png" width="75" height="75" class="" alt="rust" />
								</span>
								<span class="ml-3">
									<img src="/images/php.png" width="75" height="75" class="" alt="php" />
								</span>
							</div>
						</div>
					</div>
					
				</div>
			</div>
		</div>
		<div class="feature-2 mt-5">
			<div class="bg-fr-white text-dark">
				<div class="container">
					<div class="row pt-5">
						<div class="col-md-6">
							<div class="row">
								<h4>
									Configuration as a code
									<small class="pl-3 font-weight-light font-italic" style="font-size:14px;">Define any workflow using yaml</small>
								</h4>
							</div>
							<div class="mt-4 mb-4 row">
								<ul class="list-group list-group-flush">
									<li class="list-group-item bg-fr-white"><i class="fa fa-terminal fa-fw" aria-hidden="true"></i> Execute any command</li>
									<li class="list-group-item bg-fr-white"><i class="fa fa-lock fa-fw" aria-hidden="true"></i> Isolate your services per environment or pull request</li>
									<li class="list-group-item bg-fr-white"><i class="fa fa-cloud fa-fw" aria-hidden="true"></i> Choose to expose or not your services to the public</li>
								</ul>
							</div>
						</div>
						<div class="col-md-6">
							<div class="mt-5 row">
							</div>
						</div>	
					</div>
				</div>
			</div>
		</div>
		<div class="feature-3 mt-5">
			<div class="bg-fr-red text-white">
				<div class="container">
					<div class="row pt-5">
						<div class="col-md-6">
							<div class="row">
								<h4>
									Libre
									<small class="pl-3 font-weight-light font-italic" style="font-size:14px;">baguette.io is fully open source</small>
								</h4>
							</div>
							<div class="mt-4 mb-4 row">
								<ul class="list-group list-group-flush">
									<li class="list-group-item no-border bg-fr-red"><i class="fa fa-server fa-fw" aria-hidden="true"></i> Host it yourself</li>
									<li class="list-group-item no-border bg-fr-red"><i class="fa fa-code-fork fa-fw" aria-hidden="true"></i> Fork it</li>
									<li class="list-group-item no-border bg-fr-red"><i class="fa fa-handshake-o fa-fw" aria-hidden="true"></i> Help us improving baguette.io</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
    </section>
</template>
