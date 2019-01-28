"""Troposphere template for deployment."""
import os, json
from troposphere import Template, Parameter, Ref, GetAtt, Join, events
from troposphere.constants import STRING
from troposphere.iam import Role, PolicyType, Policy, ManagedPolicy

class iamPolicies(object):
    """Class to instantiate Template."""

    def __init__(self):
        """Instantiate troposphere template."""
        self.template = Template()
        self.template.add_description("repo: ")
        self.addParameters()
        self.createReadOnlyPolicies()
    
    def addParameters(self):
        """Customisable Parameters for Cloudformation Template."""
        self.environmentName = self.template.add_parameter(
            Parameter(
                "environmentName",
                Type=STRING,
                Description="The name for the environment."
            )
        )

    def createReadOnlyPolicies(self):
        policies = os.listdir('policies')
        for policy in policies:
            with open('policies/' + policy) as data_file:
                policyData = json.load(data_file)
                self.template.add_resource(ManagedPolicy(
                    policy.replace('.json', ''),
                    PolicyDocument=policyData
                ))

print(iamPolicies().template.to_yaml())
