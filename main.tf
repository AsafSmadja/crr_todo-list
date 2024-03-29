provider "aws" {
  region = "us-east-1" # Replace with your desired region
}

# VPC Configuration for Todo-list-webapp
resource "aws_vpc" "todo_list_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "todo-list-webapp-vpc"
  }
}

# Subnet Configuration
resource "aws_subnet" "todo_list_subnet_1" {
  vpc_id            = aws_vpc.todo_list_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "todo-list-webapp-subnet-1"
  }
}

resource "aws_subnet" "todo_list_subnet_2" {
  vpc_id            = aws_vpc.todo_list_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "todo-list-webapp-subnet-2"
  }
}

# Security Groups Configuration
resource "aws_security_group" "todo_list_sg" {
  name        = "todo-list-webapp-sg"
  description = "Security Group for Todo-list-webapp VPC"
  vpc_id      = aws_vpc.todo_list_vpc.id

  # Security group rules here...

  tags = {
    Name = "todo-list-webapp-sg"
  }
}

# EKS Cluster Configuration for Todo-list-webapp
resource "aws_eks_cluster" "todo_list_cluster" {
  name     = "todo-list-webapp-cluster"
  role_arn = aws_iam_role.todo_list_eks_cluster_role.arn

  vpc_config {
    subnet_ids         = [aws_subnet.todo_list_subnet_1.id, aws_subnet.todo_list_subnet_2.id]
    security_group_ids = [aws_security_group.todo_list_sg.id]
  }
}

# IAM Roles Configuration
resource "aws_iam_role" "todo_list_eks_cluster_role" {
  name = "todo-list-webapp-eks-cluster-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "eks.amazonaws.com"
      }
    }]
  })
}

# RDS Instance Configuration for Todo-list-webapp
resource "aws_db_instance" "todo_list_db" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  identifier           = "todolistdb-instance"
  db_name              = "todolistdb"         
  username             = "dbuser"
  password             = "dbpassword"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}

# Output Configuration
output "todo_list_eks_cluster_endpoint" {
  value = aws_eks_cluster.todo_list_cluster.endpoint
}

output "todo_list_rds_instance_address" {
  value = aws_db_instance.todo_list_db.address
}

