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
							<li><span class="output">App healthy, you can access it using : <u>https://user.app.master.projects.baguette.io</u></span></li>
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
								<span><b>No</b> downtime during deployments</span>
							</div>
							<div class="row">
								<span>REST api, auto discovery, auto scaling, health checks, ...</span>
							</div>
						</div>
						<div class="col-md-6">
							<div class="row">
								<span class="border rounded border-white ml-3">
									<img src="/images/python.png" width="75" height="75" class="" alt="python" />
								</span>
								<span class="border rounded border-white ml-3">
									<img src="/images/js.png" width="75" height="75" class="" alt="js" />
								</span>
								<span class="border rounded border-white ml-3">
									<img src="/images/netcore.png" width="75" height="75" class="" alt=".netcore" />
								</span>
								<span class="border rounded border-white ml-3">
									<img src="/images/go.png" width="75" height="75" class="" alt="go" />
								</span>
							</div>
							<div class="row pt-3">
								<span class="border rounded border-white ml-3">
									<img src="/images/java.png" width="75" height="75" class="" alt="java" />
								</span>
								<span class="border rounded border-white ml-3">
									<img src="/images/ruby.png" width="75" height="75" class="" alt="ruby" />
								</span>
								<span class="border rounded border-white ml-3">
									<img src="/images/rust.png" width="75" height="75" class="" alt="rust" />
								</span>
								<span class="border rounded border-white ml-3">
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
					<div class="pt-5">
						<div class="row">
							<h4>Configuration as a code</h4>
						</div>
						<div class="row">
							<p>Define <b>any</b> workflow using <b>yaml</b>:</p>
						</div>
						<div class="row">
							<span>Execute <b>any</b> command</span>
						</div>
						<div class="row">
							<span><b>Isolate</b> your services per environment or pull request</span>
						</div>
						<div class="row">
							<span><b>Choose</b> to expose or not your services to the public</span>
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
							<h4>Libre</h4>
						</div>
						<div class="row">
							<p>baguette.io is <b>fully</b> open source(LGPL 3):</p>
						</div>
						<div class="row">
							<span><b>Powerfull</b> REST API</span>
						</div>
						<div class="row">
							<span><b>Help</b> us improving baguette.io</span>
						</div>
						<div class="row">
							<span>Host it <b>yourself</b></span>
						</div>
						<div class="row">
							<span><b>Fork</b> it</span>
						</div>
					</div>
				</div>
			</div>
		</div>
    </section>
</template>
