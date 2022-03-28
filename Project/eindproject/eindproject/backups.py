import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_events as event,
    aws_backup as bk,
    aws_ec2 as ec2,
    Tags,
)


class BackupStack(cdk.NestedStack):

    def __init__(self, scope: Construct, id: str, ManagementServer: ec2.Instance, asg: autoscaling.AutoScalingGroup, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        web_tags_environment = environments.get("webserver_tags")
        web_tag_key = web_tags_environment.get("tag_key")
        web_tag_value = web_tags_environment.get("tag_value")

        web_bk_environment = environments.get("webserver_backup")
        web_bk_backup = web_bk_environment.get("name")
        web_bk_name = web_bk_environment.get("backup_plan_name")
        web_bk_vault = web_bk_environment.get("backup_vault_name")
        web_bk_rule = web_bk_environment.get("backup_rule_name")
        web_bk_del = web_bk_environment.get("delete_backup_after_days")
        web_bk_min = web_bk_environment.get("cron_minute")
        web_bk_hour = web_bk_environment.get("cron_hour")
        web_bk_month = web_bk_environment.get("cron_month")
        web_bk_week = web_bk_environment.get("cron_week_day")
        web_bk_select = web_bk_environment.get("backup_selection_name")

        man_bk_environment = environments.get("managementserver_backup")
        man_bk_backup = man_bk_environment.get("name")
        man_bk_name = man_bk_environment.get("backup_plan_name")
        man_bk_vault = man_bk_environment.get("backup_vault_name")
        man_bk_rule = man_bk_environment.get("backup_rule_name")
        man_bk_del = man_bk_environment.get("delete_backup_after_days")
        man_bk_min = man_bk_environment.get("cron_minute")
        man_bk_hour = man_bk_environment.get("cron_hour")
        man_bk_month = man_bk_environment.get("cron_month")
        man_bk_week = man_bk_environment.get("cron_week_day")
        man_bk_select = man_bk_environment.get("backup_selection_name")

        Tags.of(asg).add(web_tag_key, web_tag_value)

        # Webserver backup creation.

        web_backup_plan = bk.BackupPlan(
            self, web_bk_backup,
            backup_plan_name=web_bk_name
        )

        backup_vault_name = web_bk_vault
        bk_vault = bk.BackupVault(
            self, web_bk_vault,
            backup_vault_name=backup_vault_name,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        web_backup_plan.add_rule(
            rule=bk.BackupPlanRule(
                backup_vault=bk_vault,
                rule_name=web_bk_rule,
                delete_after=cdk.Duration.days(web_bk_del),
                schedule_expression=event.Schedule.cron(
                    minute=web_bk_min,
                    hour=web_bk_hour,
                    month=web_bk_month,
                    week_day=web_bk_week
                )
            )
        )

        web_backup_plan.add_selection(
            web_bk_name,
            backup_selection_name=web_bk_select,
            resources=[
                bk.BackupResource.from_tag(
                    web_tag_key,
                    web_tag_value
                )
            ]
        )

        # Management server backup creation.

        man_backup_plan = bk.BackupPlan(
            self, man_bk_backup,
            backup_plan_name=man_bk_name
        )

        backup_vault_name = man_bk_vault
        second_bk_vault = bk.BackupVault(
            self, man_bk_vault,
            backup_vault_name=backup_vault_name,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        man_backup_plan.add_rule(
            rule=bk.BackupPlanRule(
                backup_vault=second_bk_vault,
                rule_name=man_bk_rule,
                delete_after=cdk.Duration.days(man_bk_del),
                schedule_expression=event.Schedule.cron(
                    minute=man_bk_min,
                    hour=man_bk_hour,
                    month=man_bk_month,
                    week_day=man_bk_week
                )
            )
        )

        man_backup_plan.add_selection(
            man_bk_name,
            backup_selection_name=man_bk_select,
            resources=[
                bk.BackupResource.from_ec2_instance(ManagementServer)
            ]
        )