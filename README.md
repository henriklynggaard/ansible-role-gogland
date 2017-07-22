Gogland (https://www.jetbrains.com/go/)
=========

This role installs Gogland and configured plugins. It has been tested on Linux Mint 18 but should work on most 
distributions. By default it installs Gogland Early build  171.4694.61 and no additional plugins

By default Gogland is installed under the user's home directory and _become_ is not needed.

Requirements
------------

None


Role Variables
--------------

    gogland_version: 171.4694.61
    gogland_download_mirror: https://download.jetbrains.com/go/
    gogland_plugin_download_mirror: "https://plugins.jetbrains.com/plugin/download?updateId="
    gogland_plugins: []
    gogland_download_directory: /tmp
    gogland_user_dir: "~{{ (gogland_install_user is defined) | ternary(gogland_install_user, ansible_user_id) }}"
    gogland_install_directory: "{{ gogland_user_dir | expanduser  }}/Tools"
    gogland_install_user: <undefined>

    # calculated
    gogland_install_file: "gogland-{{ gogland_version }}.tar.gz"
    gogland_download_url: "{{ gogland_download_mirror }}{{ gogland_install_file }}"
    gogland_location: "{{ gogland_install_directory }}/Gogland-{{ gogland_version }}"
    gogland_desktop_file_location: "{{ gogland_user_dir | expanduser  }}/.local/share/applications/gogland-{{ gogland_version }}.desktop"


* gogland_plugins is a list of names which get appended to gogland_plugin_download_mirror to form a full download
* Defining gogland_install_user allows the role to install under a different user, however become is required 


Dependencies
------------

None

Example 
-------

__Example playbook__


    - hosts: localhost
      connection: local
    
    roles:
      - henriklyngaard.gogland
      
__Exmaple inventory for plugins__

The below IDs have been found by going to https://plugins.jetbrains.com/gogland and searching for the plugin. 
Once found copy the link location for the desired version and use the _updateId=XXXXX_ part at the end        
      
    gogland_plugins:
      # ignore 1.7.6
      - 32828
      # bash support 1.6.5.171
      - 31610
      # ansible 0.9.4
      - 27616
      # docker 2.5.3
      - 33621
      # markdown 2017.1.20170302
      - 33092      
      
 Alternatively upload the required plugins to a webserver and adjust _gogland_plugin_download_mirror_ and 
 _gogland_plugins_ accordingly
      
      
License
-------

MIT

Change log
----------

* 1.1: Allow installation under another user
* 1.0: Initial version
