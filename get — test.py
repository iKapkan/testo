import random
import fake as fake
import pytest
import requests
import json
from faker import Faker

Fake = Faker()


def main():
    pass


def get_servers():
    """just Get"""
    r = requests.get('https://*****/api/v1/servers/',
                     headers={'Authorization': '***********',
                              'Content-Type': 'application/json',
                              'User-Agent': 'PostmanRuntime/7.26.5'})
    print("Get servers: ", r.status_code, r.json())


get_servers()


def creat_vcd(group_id, datacenter='skolkovo'):
    """создать ВЦОД через АПИ"""
    network = {"network_name": Fake.catch_phrase(), "cidr": "172.**.**.**/**",
               "dns_nameservers": ["8.8.8.8", "8.8.4.4"],
               "enable_dhcp": True}

    jumphost = {'skolkovo': False, 'datapro': True}

    data = {"project": {"ir_group": "vdc", "type": "vdc", "ir_type": "vdc_openstack", "virtualization": "openstack",
                        "name": Fake.name(), "group_id": group_id,
                        "datacenter": datacenter,
                        "jump_host": jumphost[datacenter], "network": network}}  # jump host is out

    p = requests.post("https://*************/api/v1/projects", data=json.dumps(data),
                      headers={"Authorization": "***********",
                               "Content-Type": "application/json",
                               "User-Agent": "PostmanRuntime/7.26.5"})
    print("Создаем ВЦОД: ", p.status_code, p.json())
    # return p.json()


creat_vcd(group_id="****************************")


def creat_vm(group_id, project_id):
    """Create VM (RHEL)"""
    data = {"server": {"group_id": group_id, "service_name": Fake.name(),
                       "virtualization": "openstack", "ir_group": "vm", "os_name": "rhel", "os_version": "8.1",
                       "fault_tolerance": "Stand-alone", "project_id": project_id,
                       "disk": 50,
                       "zone": "internal", "domain": "sigma",
                       "network_uuid": None,
                       "flavor": "m1.tiny"}, "count": 1}

    vm = requests.post("https://******************/api/v1/servers", data=json.dumps(data),
                       headers={"Authorization": "Token *********************",
                                "Content-Type": "application/json",
                                "User-Agent": "PostmanRuntime/7.26.5"})
    print("Создаем ВМ rhel: ", vm.status_code, vm.json())


creat_vm(group_id="*************************",  project_id=creat_vcd())


def del_vm():
    """Delete VM"""
    pass


del_vm()

main()

