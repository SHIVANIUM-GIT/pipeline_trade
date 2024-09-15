resource "aws_instance" "aws_ec2" {
  instance_type          = var.instance_type
  ami                    = var.ami
  key_name               = "${aws_key_pair.key_pair}"
  vpc_security_group_ids = []
  user_data              = file("${path.module}/install.sh")

  tags = {
    Name = "${var.project_name}-ec2"
  }

  root_block_device {
    volume_size = 40
  }

}