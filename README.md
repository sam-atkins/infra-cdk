
# Infra CDK

Playground for experiments with AWS Cloud Development Kit.

## Setup

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

`cdk` commands need to include the profile option along with the profile name if you have more than one AWS profile and don't want to use the default e.g.

`cdk deploy --profile {profileName}`

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 * `cdk destroy`     destroy the deployed stack
