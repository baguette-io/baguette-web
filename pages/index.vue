<template>
    <section class="main" role="main">
	    <div class="presentation">
        	<div class="container headtitle">
        		<div class="row justify-content-md-center">
	    			<div class="col-12 col-md-auto">
	    				<h1>Continuous integration and deployment platform</h1>
	    			</div>
	    			<div class="col-12 col-md-auto">
        				<h6>Test and deploy your code, micro service, docker, simply</h6>
	    			</div>
	    		</div>
	    	</div>
        	<div class="container windows">
                <div class="row justify-content-md-center">
                    <div class="window">
                        <div class="window-header">
                            <span class="window-bullet red"></span>
                            <span class="window-bullet yellow"></span>
                            <span class="window-bullet green"></span>
                            <span class="window-title">~/code/my-project/</span>
                        </div>
                        <div class="window-body">
                            <ul class="list-unstyled">
                                <li><span class="prefix">[my-project(master)]$</span><span class="command">baguette app-create</span></li>
                                <li><span class="output">my-project created</span></li>
                                <li><span class="output">Push to baguette.io remote to deploy your app</span></li>
                                <li><span class="prefix">[my-project(master)]$</span><span class="command">git push baguette.io master</span></li>
                                <li><span class="output">deploying my-project(master)</span></li>
                                <li><span class="output">App healthy, you can access it using : <u>https://user.my-project.projects.baguette.io</u></span></li>
                            </ul>
                        </div>
                    </div>
	    		</div>
	    	</div>
	    </div>
	    <div class="mainfeatures">
        	<div class="container-fluid">
        		<div class="row justify-content-md-center">
                    <h2>Use cases</h2>
                    <h2>Simple and powerful platform as a service</h2>
	    		</div>
        		<div class="row">
                    <div class="col-sm-1 info text-right"><i class="fa fa-cogs fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Automation</h3>
                        <p>Simply test and deploy your services by doing a <b>git push baguette.io</b></p>
                    </div>
                    <div class="col-sm-1 info"><i class="fa fa-code fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Language agnostic</h3>
                        <p>Use your prefered language: node, ruby, perl, java, python. We don't care.</p>
                    </div>
                    <div class="col-sm-1 info text-right"><i class="fa fa-sun-o fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Protocols</h3>
                        <p>We support not only HTTP[S], but also TCP and UDP services</p>
                    </div>
	    		</div>
        		<div class="row">
                    <div class="col-sm-1 info"><i class="fa fa-heartbeat fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Healthchecks</h3>
                        <p>detect errors on your services using our simple heartbeat system</p>
                    </div>
                    <div class="col-sm-1 info text-right"><i class="fa fa-sitemap fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Scalability</h3>
                        <p>services auto scale given your choices(cpu/memory/network usage)</p>
                    </div>
                    <div class="col-sm-1 info text-right"><i class="fa fa-tachometer fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Monitoring</h3>
                        <p>real time data and logging give you infos about your services status</p>
                    </div>
	    		</div>
	    	</div>
	    </div>
	    <div class="companyfeatures">
        	<div class="container-fluid">
        		<div class="row justify-content-md-center">
                    <h2>Simple and built for companies</h2>
	    		</div>
        		<div class="row">
                    <div class="col-sm-1 info text-right"><i class="fa fa-users fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Organizations</h3>
                        <p>Each app belongs to an organization. And you can manage them using granulary permissions</p>
                    </div>
                    <div class="col-sm-1 info"><i class="fa fa-ban fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Network isolation</h3>
                        <p>Each organization is isolated from others, and every app belongs to a VPC, you can create as you need</p>
                    </div>
                    <div class="col-sm-1 info text-right"><i class="fa fa-globe fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Regions</h3>
                        <p>Choose on which cloud provider/region you want to create your VPC, and then your apps</p>
                    </div>
	    		</div>
        		<div class="row">
                    <div class="col-sm-1 info"><i class="fa fa-star fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>API</h3>
                        <p>You can use baguette.io using a web interface, a CLI tool but also using our open API</p>
                    </div>
                    <div class="col-sm-1 info text-right"><i class="fa fa-code-fork fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>PaaS/Host it</h3>
                        <p>If you want to host our solution, instead of using our paas, you just can. Our code will also be available for you (GPL 3.0)</p>
                    </div>
                    <div class="col-sm-1 info text-right"><i class="fa fa-rocket fa-5x text-danger" aria-hidden="true"></i></div>
                    <div class="col-sm-3 info">
                        <h3>Secure deployment</h3>
                        <p>By default we are using the blue/green strategy, but you can use the canary one</p>
                    </div>
	    		</div>
	    	</div>
	    </div>
    </section>
</template>
