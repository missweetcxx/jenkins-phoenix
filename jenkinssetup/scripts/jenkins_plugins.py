import jenkins
import jenkins_plugins_list

# cf: https://updates.jenkins-ci.org/download/plugins/

j = jenkins.Jenkins('http://jenkins:8080')
pluins = jenkins_plugins_list.plugins
plugins = (
	"git",
	"github",
	"urltrigger",
	"docker-plugin",
	"docker-commons",
	"docker-build-step",
)
print 'Installing plugins starting: ' + str(plugins)
for p in plugins:
	j.install_plugin(p)
print 'Plugins requested. Wait for install.'

