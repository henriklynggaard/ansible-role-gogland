import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


desktop_file_location = "/root/.local/share/applications/gogland-171.4694.61.desktop"


def test_desktop_file_exists(File):
    f = File(desktop_file_location)

    assert f.exists
    assert f.is_file


def test_desktop_file_contains_fullpath(File):
    f = File(desktop_file_location)

    assert f.contains("/root/Tools/Gogland-171.4694.61/bin/gogland.png")
    assert f.contains("/root/Tools/Gogland-171.4694.61/bin/gogland.sh")


def test_desktop_file_contains_right_name(File):
    f = File(desktop_file_location)

    assert f.contains("Gogland 171.4694.61")


def test_start_file_exists(File):
    f = File('/root/Tools/Gogland-171.4694.61/bin/gogland.sh')

    assert f.exists
    assert f.is_file
