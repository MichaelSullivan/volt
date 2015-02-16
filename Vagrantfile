# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

THIS_FILE_DIR_NAME = File.dirname(File.expand_path(__FILE__)).split(File::SEPARATOR)[-1]

##  config.vm.synced_folder ".", "/vagrant", nfs: true
##  config.vm.synced_folder ".", "/mnt/vagrant", type: 'rsync', rsync__exclude: ".git/, .DS_Store, .idea", rsync__args: ['-avz', '--copy-links', '--progress', '-e']

  config.vm.provider "virtualbox" do |vb, override|
    override.vm.box = "#{ENV['VOLT_VIRTUALBOX_BOX']}"

    # TODO: switch over to dhcp to make thinks a bit more dynamic
    # TODO: make it fail quickly and loudly with... , auto_config: false
    # override.vm.network :private_network, type: "dhcp"
    override.vm.network :private_network, ip: "#{ENV['VOLT_NETWORK_IP']}"

    vb.customize ['modifyvm', :id, '--cpus', '2']
    vb.customize ['modifyvm', :id, '--ioapic', 'on']
    vb.customize ['modifyvm', :id, '--memory', '4000']

    # https://github.com/mitchellh/vagrant/issues/1807
    # whatupdave: my VM was super slow until I added these:
    # seems to be safe to run with: https://github.com/griff/docker/commit/e5239b98598ece4287c1088e95a2eaed585d2da4
     vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
     vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]

    # THIS IS A POTENTIAL SECURITY ISSUE
    # allow synlinks on shared folders
    # TODO: get nfs folders with symlinks
    # vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate//mnt/vagrant", "1"]
  end

  # The vagrant-awsinfo plugin: https://github.com/johntdyer/vagrant-awsinfo
  # The vagrant-aws plugin: mitchellh/vagrant-aws
  config.vm.provider :aws do |aws, override|
    override.vm.box = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    override.vm.synced_folder '.', '/vagrant', disabled: true

    aws.subnet_id = "#{ENV['VOLT_AWS_SUBNET_ID']}"
    aws.security_groups = "#{ENV['VOLT_AWS_SECURITY_GROUPS']}"
    aws.ami = "#{ENV['VOLT_AWS_AMI']}"
    aws.instance_type = "#ENV{'VOLT_AWS_INSTANCE_TYPE'}"
    aws.keypair_name = "#ENV{'VOLT_AWS_KEYPAIR_NAME'}"

    aws.access_key_id = "#{ENV['VOLT_AWS_ACCESS_KEY']}"
    aws.secret_access_key = "#{ENV['VOLT_AWS_SECRET_KEY']}"

    override.ssh.username = "#{ENV['VOLT_SSH_USERNAME']}"
    override.ssh.private_key_path = "#{ENV['VOLT_SSH_PRIVATE_KEY_PATH']}"

    aws.tags = {
      'Name' => "#{ENV['VOLT_AWS_INSTANCE_NAME']}", # 'Development Machine',
      'Spun Up By' => ENV['USER']
    }
  end

  config.vm.provision :ansible do |ansible|
    ansible.sudo = true
    ansible.playbook = 'ansible/docker_host.yml'
    ansible.limit = 'all'
    ansible.verbose = 'v'
  end

end
