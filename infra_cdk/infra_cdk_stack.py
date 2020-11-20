from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import core


class InfraCdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "VPC",
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", subnet_type=ec2.SubnetType.PUBLIC
                )
            ],
        )

        ami_amazon_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        role = iam.Role(
            self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ami_amazon_linux,
            vpc=vpc,
            role=role,
        )

        security_group = aws_ec2.SecurityGroup(
            self,
            "EC2SecurityGroup",
            vpc=vpc,
            description="EC2 security group via CDK",
            security_group_name="CDK SecurityGroup",
        )
        security_group.add_ingress_rule(
            aws_ec2.Peer.ipv4("10.0.0.0/16"),
            aws_ec2.Port.tcp(22),
            "allow ssh access from the VPC",
        )
