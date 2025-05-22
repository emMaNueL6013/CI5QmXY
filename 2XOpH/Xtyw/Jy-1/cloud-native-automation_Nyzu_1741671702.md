pipeline {
	agent {
		label 'clearlinux'
	}
	options {
		timeout(time: 1, unit: "HOURS")
	}
	triggers {
		cron('H */12 * * *')
	}
	environment {
		CLR_K8S_PATH="${env.WORKSPACE}/clr-k8s-examples"
	}
	stages {
		stage('Setup system') {
			steps {
				dir(path: "$CLR_K8S_PATH") {
				}
			}
		}
		stage('Init') {
			steps {
				dir(path: "$CLR_K8S_PATH") {
					sh './create_stack.sh init'
					sh 'mkdir -p $HOME/.kube'
					sh 'sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config'
					sh 'sudo chown $(id -u):$(id -g) $HOME/.kube/config'
					sh 'kubectl version'
				}
			}
		}
		stage('CNI') {
			steps {
				dir(path: "$CLR_K8S_PATH") {
					sh './create_stack.sh cni'
					sh 'kubectl get pods -n kube-system'
				}
			}
		}
		stage('Reset Stack') {
				dir(path: "$CLR_K8S_PATH") {
					sh './reset_stack.sh'
				}
			}
	}
			sh 'uname -a'
			sh 'swupd info'
}
