
provider "aws" {
  region     = "eu-west-1"
}


variable "key_name" {
  description = "Name of the existing key pair"
  type        = string
  default     = "stan"
}

resource "aws_instance" "stan_instance" {
  ami           = "ami-0c38b837cd80f13bb"
  instance_type = "t2.micro"
  key_name      = var.key_name

  tags = {
    Name = "stan_instance"
  }

  connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("C:/Users/NOC2-NODE3/Downloads/stan.pem")
      host        = self.public_ip
    }
  # provisioner "remote-exec" {
  #   

  #   inline = [
  #     "sudo apt-get update -y",
  #     "sudo apt-get install -y docker.io",
  #     "sudo systemctl enable docker",
  #     "sudo systemctl start docker",
  #     "curl -sfL https://get.k3s.io | sh -",
  #     "sudo docker volume create jenkins_data",
  #     "sudo docker pull jenkins/jenkins:lts",
  #     "sudo docker run -d -p 8080:8080 --name jenkins -v jenkins_data:/var/jenkins_home jenkins/jenkins:lts",
  #   ]
  # }
}
 

output "instance_public_ip" {
  value = aws_instance.stan_instance.public_ip
}
