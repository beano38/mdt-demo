# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  # config.vm.box = "bento/centos-7"
  config.ssh.insert_key = false

  # Docker Servers
  config.vm.define "docker0" do |docker|
   docker.vm.hostname = "docker0"
   docker.vm.network :private_network, ip: "172.28.128.10"
   docker.vm.network "forwarded_port", guest: 57000, host: 57000
   docker.vm.network "forwarded_port", guest: 3000, host: 3000
   
   docker.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbooks/main.yml"
    ansible.inventory_path = "inventory"
    ansible.galaxy_role_file = "requirements.yml"
    ansible.extra_vars = { 
      ansible_python_interpreter:"/usr/bin/python3"
      }
  end

  end

end
