#Blue/Green Deployment

It's a description of deploying an app without disrupting the running of the existing app. It's a great method for webapps because it reduces downtime to a minimum.

The basic idea is that you run two instances of your whole app. One continues to run while you deploy to the other. When you have finished deploying (and that might include some tests) you can switch the live one over to the newly deployed version.

[See Martin Fowler's blog for more details.][blue-green]


[blue-green]: http://martinfowler.com/bliki/BlueGreenDeployment.html