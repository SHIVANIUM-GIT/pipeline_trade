resource "aws_key_pair" "key_pair" {
  key_name = "${var.project_name}"
  public_key = file("${var.key_path_file}") 
}